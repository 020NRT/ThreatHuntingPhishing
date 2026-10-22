# Week 7 — Sysmon Logs, Splunk, CAR and MITRE ATT&CK

**Date:** 22 October 2026  
**Tools:** Windows 11, Sysmon, Splunk Enterprise  
**Result:** I uploaded a CSV file to Splunk and found **120 events**.

## 1. Goal

The goal of this lab was to check Windows security logs, view them in Splunk, choose a CAR detection idea, and connect it to MITRE ATT&CK techniques.

## 2. Checking Sysmon

First, I checked the Splunk and Sysmon services in Windows PowerShell:

```powershell
Get-Service Splunkd, Sysmon64
```

Both services were running. Then I checked the Sysmon log:

```powershell
Get-WinEvent -ListLog "Microsoft-Windows-Sysmon/Operational" | Select-Object LogName, RecordCount, IsEnabled
```

The log was enabled and had **3,919 records** during my earlier check.

At first, Splunk showed **0 events** when I tried to search the Windows Sysmon log directly. I also found an access error (`errorCode=5`). I did not confirm that this problem was fixed.

## 3. Uploading Logs to Splunk

Next, I uploaded the sample file `week7_windows_sysmon_sample.csv` to Splunk Enterprise. I opened **Search & Reporting**, selected **All time**, and used this search:

```spl
source="week7_windows_sysmon_sample.csv" sourcetype="csv"
```

**Splunk showed 120 events.** I could see these types of events:

| Event ID | Meaning |
| --- | --- |
| 1 | A new process started |
| 3 | A network connection was made |
| 11 | A file was created |
| 22 | A DNS request was made |

Some events showed programs such as `cmd.exe`, `powershell.exe`, `chrome.exe`, and `notepad.exe`.

This shows that Splunk can read my uploaded CSV file. It does not show that Splunk is receiving live Sysmon logs from Windows.

### Screenshot: 120 Events in Splunk

![Uploading week7-splunk-success.png…]()


## 4. CAR Detection Idea

I chose a simple detection idea: **find PowerShell or Command Prompt processes in Sysmon logs**. Sysmon Event ID 1 records new processes.

This is an example Splunk search for this idea:

```spl
source="week7_windows_sysmon_sample.csv" sourcetype="csv" EventID=1
| search (Image="*\\powershell.exe" OR Image="*\\cmd.exe" OR CommandLine="*powershell*" OR CommandLine="*cmd*")
| table _time Computer Image CommandLine ParentImage
```

I wrote this search as an example. I have not confirmed its results in Splunk. The field names may need changes for my CSV file.

## 5. MITRE ATT&CK Mapping

I connected the detection idea to two MITRE ATT&CK techniques:

| Technique | ID | Why it is related |
| --- | --- | --- |
| PowerShell | T1059.001 | Attackers can use PowerShell to run commands |
| Windows Command Shell | T1059.003 | Attackers can use `cmd.exe` to run commands |

These programs are also used for normal tasks. Seeing them in logs does not mean there was an attack.

## 6. Results

- Sysmon and Splunk services were running during my earlier Windows check.
- The local Sysmon log was enabled and had 3,919 records.
- The first direct log search in Splunk showed 0 events.
- I uploaded a sample CSV file to Splunk.
- Splunk successfully showed **120 events**.
- I selected a detection idea and connected it to two MITRE ATT&CK techniques.
- I did not confirm a live Windows log connection or a detection alert.

## 7. Conclusion

In Week 7, I checked Sysmon logs and used Splunk Enterprise. At first, I could not see events from the Windows log directly. After that, I uploaded a sample CSV file. Splunk showed **120 events**, and I could search them. I also prepared a CAR-style detection idea and connected it to MITRE ATT&CK techniques T1059.001 and T1059.003. This lab helped me understand how a SIEM can show and search security logs.

## 8. AI Usage

I used AI to help me understand the theory and write this report in simple English. I did the practical work and took the Splunk screenshot myself.
