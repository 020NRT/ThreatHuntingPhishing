# Week 7 — Sysmon Logs, Splunk, CAR and MITRE ATT&CK

**Date:** 22 October 2026  
**Tools:** Windows 11, Sysmon, Splunk Enterprise  
**Result:** I uploaded 120 events and found 37 PowerShell and CMD events using an SPL search.

## 1. Goal

The goal of this lab was to check Windows security logs, use Splunk to find process activity, study a MITRE CAR detection idea, and connect the results to MITRE ATT&CK techniques.

## 2. Checking Sysmon

First, I checked the Splunk and Sysmon services in Windows PowerShell:

```powershell
Get-Service Splunkd, Sysmon64
```

Both services were running.

Then I checked the Sysmon log:

```powershell
Get-WinEvent -ListLog "Microsoft-Windows-Sysmon/Operational" | Select-Object LogName, RecordCount, IsEnabled
```

The Sysmon log was enabled and contained records.

At first, Splunk showed **0 events** when I tried to search Windows Sysmon logs directly. I also found an access error (`errorCode=5`).

## 3. Uploading Logs to Splunk

Next, I uploaded a CSV file named `week7_windows_sysmon_sample.csv` to Splunk Enterprise.

I opened Search & Reporting, selected **All time**, and used this search:

```spl
source="week7_windows_sysmon_sample.csv" sourcetype="csv"
```

Splunk successfully showed **120 events**.

I found these event types:

| Event ID | Description |
|---|---|
| 1 | Process Creation |
| 3 | Network Connection |
| 11 | File Creation |
| 22 | DNS Query |

Some events showed programs such as `cmd.exe`, `powershell.exe`, `chrome.exe`, and `notepad.exe`.

This confirmed that Splunk could read and search my uploaded CSV logs.

### Screenshot — 120 Events in Splunk

[View Splunk Screenshot](https://github.com/020NRT/ThreatHuntingPhishing/blob/main/screenshots/week7-splunk-success.png)

## 4. CAR Detection and SPL Search

For this part, I studied a detection idea related to PowerShell and Command Prompt activity.

Sysmon Event ID 1 records when a new process starts.

I used this SPL search in Splunk:

```spl
source="week7_windows_sysmon_sample.csv" sourcetype="csv" EventID=1
| search (Image="*\\powershell.exe" OR Image="*\\cmd.exe" OR CommandLine="*powershell*" OR CommandLine="*cmd*")
| table _time Computer Image CommandLine ParentImage
```

### Search Results

The search was successful and Splunk found **37 events**.

I could see:

- The time of each event.
- The computer name.
- The process name.
- The command line.
- The parent process.

The results included PowerShell and CMD processes.

For example, I found commands such as:

- `cmd.exe /c whoami`
- `powershell.exe -NoProfile -Command Get-Process`

These results show that Splunk can find command-line activity in the uploaded logs.

The search is a simple detection example based on process creation events. It is not yet confirmed as an implementation of a specific MITRE CAR analytic.

### Screenshot — 37 Events Found

![CAR Detection - 37 Events](screenshots/week7.png)

## 5. MITRE ATT&CK Mapping

I connected the detection results to two MITRE ATT&CK techniques:

| Technique | ID | Description |
|---|---|---|
| PowerShell | T1059.001 | Attackers can use PowerShell to execute commands |
| Windows Command Shell | T1059.003 | Attackers can use CMD to execute commands |

Both techniques are related to the **Execution** tactic (TA0002).

PowerShell and CMD are also normal Windows tools. Finding these processes does not always mean an attack happened.

## 6. Results

During Week 7, I completed the following work:

1. Checked Sysmon and Splunk services.
2. Checked Windows Sysmon logs.
3. Uploaded a CSV file into Splunk Enterprise.
4. Successfully found **120 events**.
5. Ran an SPL search to find PowerShell and CMD activity.
6. Successfully found **37 matching events**.
7. Connected the detection results to MITRE ATT&CK techniques T1059.001 and T1059.003.

I successfully tested the SPL search using uploaded sample logs.

However, I did not confirm live Sysmon log collection or create a detection alert.

## 7. Conclusion

In Week 7, I learned how to use Sysmon logs and Splunk Enterprise to find Windows process activity.

First, Splunk showed 0 events. After uploading a sample CSV file, I found **120 events**.

Then I used an SPL search and found **37 PowerShell and CMD events**.

I also connected these results to MITRE ATT&CK techniques.

This lab helped me understand how security analysts use SIEM tools to search logs and find possible security threats.

## 8. AI Usage

I used ChatGPT to understand MITRE CAR, MITRE ATT&CK, Sysmon, and Splunk.

AI helped me prepare the SPL search and organize the report in simple English.

I ran the commands, checked the results, and took the screenshots myself.
