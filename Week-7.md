# Sysmon and Splunk Enterprise — Practical Lab Report

**Date:** 21 October 2026  
**Environment:** Windows 11, Sysmon64, Splunk Enterprise  
**Result:** Partially completed

## 1. Objective

The goal of this practical task was to check Sysmon event logging and try to collect Sysmon events in Splunk Enterprise for security monitoring.

## 2. Practical Work

I used Windows PowerShell as Administrator to check the status of the Sysmon and Splunk services:

```powershell
Get-Service Splunkd, Sysmon64
```

Both services showed the status **Running**.

Next, I checked the Sysmon Operational event log:

```powershell
Get-WinEvent -ListLog "Microsoft-Windows-Sysmon/Operational" | Select-Object LogName, RecordCount, IsEnabled
```

The output showed that the log was enabled (`IsEnabled: True`) and contained **3,919 records**. This confirmed that Sysmon was recording events locally.

### Screenshot 1 — PowerShell verification

![PowerShell showing both running services and 3,919 Sysmon records](screenshots/powershell_verification.png)

I then opened Splunk Enterprise and ran this search:

```spl
index=main source="WinEventLog:Microsoft-Windows-Sysmon/Operational"
| stats count by sourcetype
```

The time range was set to **All time**, but the search returned **0 events**. Earlier troubleshooting also showed Windows Event Log subscription errors (`errorCode=5`, access denied). Therefore, the screenshots do not confirm successful collection of Sysmon events by Splunk.

### Screenshot 2 — Splunk search result

![Splunk Enterprise showing zero results for the Sysmon event search](screenshots/splunk_search.png)

## 3. Results

| Check | Observed result |
|---|---|
| Splunkd service | Running |
| Sysmon64 service | Running |
| Sysmon Operational log | Enabled |
| Sysmon local event records | 3,919 |
| Sysmon events returned by Splunk search | 0 |
| End-to-end Sysmon collection in Splunk | Not verified |

## 4. Issue and Limitation

Sysmon recorded Windows events, but Splunk did not return the expected events. During troubleshooting, Splunk logs showed that it could not subscribe to the Sysmon Operational channel and reported `errorCode=5`. The exact remaining cause was not confirmed, and the issue was not fully resolved during this lab.

## 5. Conclusion

I checked the installation and operation of Sysmon and Splunk Enterprise. Both services were running, and Sysmon was recording local events. I also tested a Splunk search for Sysmon events, but it returned no results. The practical work was therefore **partially completed**.

## 6. AI Usage Disclosure

I used an AI assistant to understand theoretical concepts related to Sysmon, Splunk, Windows Event Logs, and possible causes of the errors. AI also helped me organize and write the report in English. I performed the practical checks myself and used my own screenshots as evidence. The unsuccessful Splunk search is reported as it happened.
