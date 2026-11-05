# Week 10: Phishing Threat Intelligence Analysis — APT29

## 1. Introduction

The goal of this task is to analyze the phishing techniques used by APT29 and map them to the MITRE ATT&CK framework.

APT29 is a cyber espionage group known for targeted phishing attacks. This report focuses on its phishing methods, threat indicators, and detection techniques.

## 2. APT29 Overview

APT29 is also known as Cozy Bear and Midnight Blizzard.

The group mainly targets:

- Government organizations.
- Diplomatic institutions.
- Research organizations.
- International organizations.

APT29 uses phishing emails to gain access to target systems and collect confidential information.

Source: [MITRE ATT&CK — APT29](https://attack.mitre.org/groups/G0118/)

## 3. Phishing Campaign Analysis

In 2022, Mandiant reported a phishing campaign by APT29 against diplomatic organizations.

The attackers sent emails that looked like official embassy notifications.

The attack process included:

1. Sending a targeted phishing email.
2. Attaching a malicious HTML file.
3. Using HTML Smuggling to create an ISO or IMG file.
4. Making the victim open the file.
5. Executing malicious content through a Windows shortcut.
6. Using web services for communication during the operation.

This campaign shows how APT29 used social engineering and malicious files to deliver malware.

Source: [Mandiant — Tracking APT29 Phishing Campaigns](https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns)

## 4. MITRE ATT&CK Mapping — 10 Techniques

MITRE ATT&CK helps security analysts identify and understand attacker techniques.

The following table contains 10 techniques associated with documented APT29 operations.

| No. | Technique ID | Technique | Tactic |
|---|---|---|---|
| 1 | T1586.002 | Compromise Accounts: Email Accounts | Resource Development |
| 2 | T1566.001 | Spearphishing Attachment | Initial Access |
| 3 | T1566.002 | Spearphishing Link | Initial Access |
| 4 | T1566.003 | Spearphishing via Service | Initial Access |
| 5 | T1204.002 | User Execution: Malicious File | Execution |
| 6 | T1027.006 | HTML Smuggling | Defense Evasion |
| 7 | T1059.001 | PowerShell | Execution |
| 8 | T1078.004 | Valid Accounts: Cloud Accounts | Initial Access, Persistence, Privilege Escalation, Defense Evasion |
| 9 | T1098.002 | Additional Email Delegate Permissions | Persistence, Privilege Escalation |
| 10 | T1102.002 | Web Service: Bidirectional Communication | Command and Control |

**Important:** These techniques are documented across different APT29 operations. They were not all used in the same 2022 phishing campaign.

### Main Technique Analysis

- **T1566.001:** APT29 sends phishing emails with malicious attachments.
- **T1566.002:** Attackers use malicious links in targeted emails.
- **T1566.003:** Attackers use online services to send phishing messages.
- **T1204.002:** Victims open malicious files.
- **T1027.006:** HTML Smuggling hides malicious content inside HTML files.
- **T1586.002:** Attackers compromise email accounts to support their operations.
- **T1059.001:** PowerShell can execute malicious commands.
- **T1078.004:** Attackers use compromised cloud accounts.
- **T1098.002:** Attackers abuse email permissions to access other mailboxes.
- **T1102.002:** Attackers use web services for communication.

## 5. Threat Intelligence and IOC Analysis

Threat Intelligence helps analysts identify suspicious activity.

Important Indicators of Compromise (IOCs) include:

| Indicator | Description |
|---|---|
| Sender Email | Suspicious email address |
| Email Domain | Suspicious sender domain |
| URL | Potentially malicious link |
| File Hash | Unique file identifier |
| File Type | Suspicious HTML or ISO attachment |

Useful investigation tools:

- **VirusTotal:** Checks suspicious files, URLs, and domains.
- **MITRE ATT&CK:** Helps identify attacker techniques.
- **Google Safe Browsing:** Checks dangerous websites.

No unverified IOC values are included in this report.

## 6. Detection and Prevention

Security analysts can detect phishing activity by:

- Checking suspicious email addresses and domains.
- Analyzing email attachments and URLs.
- Checking file hashes with VirusTotal.
- Monitoring suspicious file creation with Sysmon.
- Investigating unusual processes in Splunk.

Organizations can prevent phishing attacks by:

- Using email security filters.
- Blocking malicious links and attachments.
- Training employees to recognize phishing.
- Using antivirus and EDR solutions.
- Monitoring suspicious account activity.

## 7. Conclusion

In this task, I analyzed APT29 phishing activities and studied its TTPs.

The analysis showed how APT29 uses phishing emails, compromised accounts, malicious HTML files, and social engineering.

I mapped 10 techniques to the MITRE ATT&CK framework.

I also studied how Threat Intelligence tools, IOC analysis, Sysmon, and Splunk can help detect phishing activity.

**The main conclusion is that Threat Intelligence helps security analysts understand phishing attacks, identify suspicious indicators, and improve security.**

## 8. References

1. [Mandiant — Tracking APT29 Phishing Campaigns](https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns)
2. [MITRE ATT&CK — APT29](https://attack.mitre.org/groups/G0118/)
3. [MITRE ATT&CK — Techniques](https://attack.mitre.org/techniques/)
4. [VirusTotal](https://www.virustotal.com/)
5. [Microsoft Sysmon Documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon)
6. [Splunk Documentation](https://docs.splunk.com/)
