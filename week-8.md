# Week 8 — Operation Paper Trail

- **Topic:** Adversary emulation plan with MITRE ATT&CK
- **Date:** 28 October 2026
- **Platform:** Windows 11 lab computer / virtual machine
- **Status:** The plan and a limited local demonstration are complete. CALDERA and Splunk were not used. The CALDERA stages below are a plan and have not been executed.

## 1. Goal and scope

This report describes a controlled three-stage emulation plan: initial access, persistence, and data exfiltration. Each stage is mapped to a MITRE ATT&CK technique and includes evidence a defender can review.

The plan is limited to systems owned by the tester or explicitly authorized for testing. It uses a dedicated test account and fictional data. It does not use real credentials, personal files, malware, or an external destination.

## 2. Scenario and assumptions

A test operator uses a pre-created local test account to access a Windows lab endpoint. The operator creates a visible scheduled task that writes a harmless marker file. In the planned CALDERA stage, a CALDERA agent already running on the endpoint sends a separate fake data file to the CALDERA server over its existing command-and-control (C2) channel.

The endpoint and CALDERA server must be on an isolated host-only lab network. The network must not have a route to the public Internet. Before the test, the operator records the host name, test account, time zone, and start time. Windows event auditing and Sysmon configuration are checked in advance because they affect which evidence is available.

The files use unique markers so the defender can identify them:

- Persistence marker: `PAPER-TRAIL-W8-TASK`
- Exfiltration file marker: `PAPER-TRAIL-W8-7Q4M`

These are fictional strings, not credentials or tracking links.

## 3. Safety and cleanup rules

- Use a lab VM or computer that you own or are authorized to test; take a snapshot before the exercise.
- Use only the dedicated test account and the two marker files described here.
- Keep the endpoint and CALDERA server on an isolated host-only network; do not use public servers, cloud storage, or personal data.
- Use a visible task with a harmless action. Do not hide it, elevate privileges, or run downloaded programs.
- Stop if the CALDERA agent communicates outside the isolated lab or if any unexpected system is reached.
- After evidence collection, delete the test task and marker files, stop the CALDERA operation, and revert the VM snapshot if needed.

## 4. Emulation plan and ATT&CK mapping

| Order | Stage | ATT&CK technique | Planned action | Expected evidence / success check |
| --- | --- | --- | --- | --- |
| 1 | Initial access | [Valid Accounts — T1078.003 (Local Accounts)](https://attack.mitre.org/techniques/T1078/003/) | From the lab console, sign in to the endpoint with the pre-created test local account. This emulates use of valid credentials; it does not emulate how an adversary obtained them. | Windows Security Event ID 4624 with the test account, endpoint, logon type, and time. Confirm those event details in the event record. |
| 2 | Persistence | [Scheduled Task — T1053.005](https://attack.mitre.org/techniques/T1053/005/) | Create a clearly named task, `W8-PaperTrail-Lab`, triggered at the next sign-in of the test account. Its only action is to write `PAPER-TRAIL-W8-TASK` to a file in the test user's Temp folder. Do not hide the task or run an executable. | Confirm the task definition and trigger; confirm the marker file appears after the next sign-in. Review Task Scheduler history, Security Event ID 4698 if task-creation auditing is enabled, and Sysmon Event ID 1 if process creation is logged. |
| 3 | Data exfiltration | [Exfiltration Over C2 Channel — T1041](https://attack.mitre.org/techniques/T1041/) | In a separate planned CALDERA operation, use an installed and reviewed CALDERA ability that transfers only `lab-note.txt` from the endpoint to the CALDERA server over the agent's existing C2 channel. Do not start a separate file-transfer service or send the file to another destination. If no suitable ability is installed and reviewed, mark this stage “not executed” rather than substituting a different transfer method. | CALDERA operation record showing the ability and agent; receiver-side confirmation that the expected marker arrived; Sysmon Event ID 3 if configured. Verify the received file's contents or hash against the source. |

### Planned execution sequence

1. Confirm authorization, VM snapshot, isolated network, test account, event logging, and marker file contents.
2. Record the start time, then sign in with the test account and verify the relevant 4624 event.
3. Create the visible scheduled task, sign out and back in, then check whether the task action created its marker file. If it does not, record the failure and do not claim successful persistence execution.
4. Only after the CALDERA server, agent, and ability have been reviewed, run the separate file-transfer operation over the existing C2 channel. Confirm the transfer at both ends.
5. Stop the operation, collect logs, and perform the cleanup steps above.

The CALDERA ability must be selected from the abilities actually installed in the lab and reviewed before execution. This report does not claim a particular ability was installed or run.

## 5. Local demonstration results

I ran a small PowerShell demonstration. It was not a CALDERA operation and did not complete all three planned stages.

### Windows logon

The Windows Security log shows Event ID 4624 at **28 October 2026, 14:52:15**. The screenshot does not show the event details, so the account name and logon type are not confirmed. The selected event is ID 5379 at 14:52:26; it records a read from Credential Manager. This evidence does not establish that the 4624 event belongs to the test account.

![Windows Security log](screenshots/week8-security-log.png)

### Scheduled task

The task `W8-PaperTrail-Lab` was created. PowerShell showed it in state `Queued`, with a last run time of **14:59:17** and result code `0`. A later check did not find the expected marker file. A second run also did not find it within 20 seconds.

The Task Scheduler screenshot shows the task under the `user` account, in state `Queued`; task history is disabled. This confirms task creation, but not that the action completed or persistence succeeded.

![Scheduled task](screenshots/week8-task-scheduler.png)

### Local file transfer

The PowerShell script sent the fake file `lab-note.txt` to `127.0.0.1:8765`. The receiver showed the marker `PAPER-TRAIL-W8-7Q4M` and saved the file in the user's Temp folder.

![PowerShell test output](screenshots/week8-lab-run.png)

![Local receiver output](screenshots/week8-local-transfer.png)

This local transfer is not a C2 transfer and does not demonstrate T1041. No Sysmon network event or Splunk result is included.

## 6. Defender review plan

For a full lab run, review a narrow time window around the recorded start and end times. Correlate the account, endpoint, task name, process, destination, and CALDERA operation. Event IDs are evidence to investigate; no single event alone proves malicious activity.

1. **Account use:** inspect Security Event ID 4624 and verify the account, logon type, workstation, and timestamp.
2. **Task creation:** inspect Task Scheduler history and Security Event ID 4698 if the relevant audit policy is enabled. Compare the task name, trigger, action, and account with the approved plan.
3. **Task execution:** inspect Sysmon Event ID 1, if available, and confirm whether the expected marker file was created. A created task without the marker is not a successful execution.
4. **C2-channel transfer:** correlate the CALDERA operation and agent with Sysmon Event ID 3, if available, and the CALDERA server's receiver record. Confirm the destination is the lab server and the received file matches the approved test file.
5. **Close-out:** confirm the task and marker files were removed and that the test agent/operation was stopped.

Splunk was not used for this demonstration. In a full exercise, the analyst should adapt searches to the local index, field extractions, and logging configuration, then save the search window and results as evidence.

## 7. Limitations

- CALDERA was not run; the planned T1041 stage remains unexecuted.
- Splunk was not used to search the events.
- The 4624 screenshot does not show enough detail to confirm the test account or logon type.
- The scheduled task was created, but its marker action was not confirmed.
- The file transfer stayed on the same computer and was not a C2 transfer.
- Windows audit policy and Sysmon configuration affect which events are recorded.

## 8. Conclusion

The plan maps valid local-account use to T1078.003, scheduled-task persistence to T1053.005, and the planned transfer over an existing CALDERA C2 channel to T1041. The local demonstration confirmed that a fake file reached a receiver on the same computer and that a scheduled task was created. It did not confirm task execution or perform C2-channel exfiltration. CALDERA and Splunk results are not claimed.

## 9. AI use

ChatGPT helped prepare the plan, local test scripts, and this report. I ran the local demonstration and took the screenshots. I did not run CALDERA or search the results in Splunk.

## References

- MITRE ATT&CK, [Valid Accounts (T1078)](https://attack.mitre.org/techniques/T1078/) and [Local Accounts (T1078.003)](https://attack.mitre.org/techniques/T1078/003/)
- MITRE ATT&CK, [Scheduled Task (T1053.005)](https://attack.mitre.org/techniques/T1053/005/)
- MITRE ATT&CK, [Exfiltration Over C2 Channel (T1041)](https://attack.mitre.org/techniques/T1041/)
- MITRE CALDERA, [Documentation](https://caldera.readthedocs.io/en/stable/)
- [Local practical runbook](Week8-Practical/README.md)
