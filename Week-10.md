# Week 10: Phishing Threat Intelligence Analysis — APT29

## 1. Introduction

The goal of this week is to study phishing attacks used by APT29, understand its Tactics, Techniques, and Procedures (TTPs), and map them to the MITRE ATT&CK framework.

APT29 is an advanced cyber espionage group. It uses phishing, compromised accounts, malware, and legitimate web services to gain access to target organizations.

This report focuses on APT29's diplomatic phishing campaigns and explains how Threat Intelligence can help security analysts detect and prevent similar attacks.

## 2. APT29 Overview

APT29 is also known by the following names:

- Cozy Bear
- Midnight Blizzard
- The Dukes
- NOBELIUM (in some vendor reporting)

APT29 is associated with Russian state-sponsored cyber espionage.

**Main targets:**
- Government organizations
- Diplomatic institutions
- Foreign ministries
- International organizations
- Research and technology organizations

**Main objectives:**
- Gain unauthorized access to systems.
- Steal confidential information.
- Access email accounts.
- Collect intelligence.
- Maintain long-term access to target networks.

APT29 is known for using social engineering and carefully prepared phishing emails.

Source: [MITRE ATT&CK — APT29 (G0118)](https://attack.mitre.org/groups/G0118/)

## 3. APT29 Phishing Campaign Analysis

### 3.1 The 2022 Diplomatic Phishing Campaign

In April 2022, Mandiant published research about APT29 phishing campaigns targeting diplomatic organizations.

The campaign started in January 2022 and targeted government and diplomatic organizations in different regions.

Attackers sent emails that looked like official administrative notifications from embassies.

They used legitimate but compromised email accounts to make their messages look more trustworthy.

### 3.2 Attack Process

The campaign included several important stages:

**Step 1 — Phishing Email**

APT29 sent emails that looked like official embassy notifications.

**Step 2 — Malicious HTML Attachment**

The emails included malicious HTML files. One example was a file named `Covid.html`.

**Step 3 — HTML Smuggling**

When the victim opened the HTML file, it created an IMG or ISO file on the computer.

**Step 4 — User Execution**

The victim opened the mounted image and clicked a Windows shortcut (LNK) file.

**Step 5 — Malware Execution**

The shortcut executed a malicious DLL. This helped attackers install additional malware.

**Step 6 — Command and Control**

APT29 used legitimate web services, including Atlassian Trello, for command and control communication.

### 3.3 Why Was This Attack Effective?

The attack was effective for several reasons:

- Emails looked like real administrative messages.
- Attackers used compromised email accounts.
- HTML files helped hide the malicious delivery process.
- Legitimate services made network activity harder to identify.
- Users were encouraged to open files themselves.

**Main lesson:** Phishing is not only about sending suspicious emails. It can be the first stage of a larger cyberattack.

Source: [Mandiant — Tracking APT29 Phishing Campaigns (2022)](https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns)

## 4. Analysis of APT29 TTPs

TTP means Tactics, Techniques, and Procedures.

- **Tactics:** What the attacker wants to achieve.
- **Techniques:** How the attacker achieves the goal.
- **Procedures:** The specific actions and tools used.

The following TTPs are important for understanding APT29:

| TTP | Description |
|---|---|
| Spearphishing | Sending targeted phishing emails |
| Social Engineering | Making messages look trustworthy |
| HTML Smuggling | Hiding malicious content inside HTML |
| User Execution | Making victims open malicious files |
| PowerShell | Using scripts to execute commands |
| Valid Accounts | Using compromised accounts |
| Command and Control | Communicating with attacker infrastructure |
| Credential Access | Stealing or accessing credentials |

These techniques help security analysts understand how the attack works and what they should monitor.

## 5. MITRE ATT&CK Mapping — 10 Techniques

MITRE ATT&CK is a knowledge base of real-world attacker tactics and techniques.

The following table contains 10 techniques documented in APT29 operations.

**Important:** Not all 10 techniques were used in the same 2022 phishing campaign. The first four are directly related to the described phishing and delivery activity. The remaining techniques represent other documented APT29 operations and show possible activity during later stages of intrusions.

| No. | Technique ID | Technique Name | Tactic |
|---|---|---|---|
| 1 | T1566.001 | Spearphishing Attachment | Initial Access |
| 2 | T1204.002 | User Execution: Malicious File | Execution |
| 3 | T1027.006 | HTML Smuggling | Defense Evasion |
| 4 | T1102.002 | Web Service: Bidirectional Communication | Command and Control |
| 5 | T1059.001 | PowerShell | Execution |
| 6 | T1078 | Valid Accounts | Initial Access, Persistence, Privilege Escalation, Defense Evasion |
| 7 | T1003.006 | OS Credential Dumping: DCSync | Credential Access |
| 8 | T1053.005 | Scheduled Task | Execution, Persistence, Privilege Escalation |
| 9 | T1098.002 | Additional Email Delegate Permissions | Persistence, Privilege Escalation |
| 10 | T1087.002 | Domain Account | Discovery |

### 5.1 Technique Analysis

**1. T1566.001 — Spearphishing Attachment**

APT29 sent targeted emails with malicious attachments.

The messages looked like official administrative notifications. The malicious HTML file was used to deliver the next stage of the attack.

**2. T1204.002 — User Execution: Malicious File**

The attack required user interaction.

The victim opened the malicious HTML attachment and later interacted with files inside the mounted image.

**3. T1027.006 — HTML Smuggling**

APT29 used HTML Smuggling to deliver malicious content.

The HTML file generated an IMG or ISO file on the victim's computer. This method made the delivery process more difficult to detect.

**4. T1102.002 — Web Service: Bidirectional Communication**

APT29 used legitimate web services such as Trello for command and control communication.

This technique can help attackers hide malicious traffic among normal web activity.

**5. T1059.001 — PowerShell**

APT29 has used PowerShell in other documented operations.

PowerShell can execute commands and scripts on Windows systems. Security analysts should monitor unusual PowerShell activity.

**6. T1078 — Valid Accounts**

APT29 has used compromised accounts to access victim systems and cloud environments.

Using real accounts can help attackers avoid some security controls.

**7. T1003.006 — OS Credential Dumping: DCSync**

APT29 used DCSync during the SolarWinds compromise.

This technique allows attackers with the required Active Directory permissions to request credential data through domain replication.

**8. T1053.005 — Scheduled Task**

APT29 has used scheduled tasks to maintain access to compromised systems.

A malicious scheduled task can execute programs automatically at a specific time or event.

**9. T1098.002 — Additional Email Delegate Permissions**

APT29 has abused email delegation permissions in compromised environments.

This can allow attackers to access or collect information from other users' mailboxes.

**10. T1087.002 — Domain Account**

APT29 has used account discovery techniques in Windows domains.

Attackers can search for domain accounts to understand the organization's structure and identify valuable targets.

### 5.2 MITRE ATT&CK Analysis

The 10 techniques show different stages of a cyberattack.

| Attack Stage | Relevant Techniques |
|---|---|
| Initial Access | T1566.001, T1078 |
| Execution | T1204.002, T1059.001, T1053.005 |
| Defense Evasion | T1027.006, T1078 |
| Credential Access | T1003.006 |
| Discovery | T1087.002 |
| Persistence | T1078, T1053.005, T1098.002 |
| Command and Control | T1102.002 |

This mapping helps analysts understand the attack lifecycle and create better detection rules.

Sources:
- [MITRE ATT&CK — APT29](https://attack.mitre.org/groups/G0118/)
- [MITRE ATT&CK — Techniques](https://attack.mitre.org/techniques/)
- [Mandiant — Tracking APT29 Phishing Campaigns](https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns)

## 6. Threat Intelligence Indicators (IOC)

Indicators of Compromise (IOCs) are technical signs that may indicate malicious activity.

Security analysts can investigate different indicators during phishing analysis.

| Indicator | Description | Investigation Method |
|---|---|---|
| Sender Email | Suspicious sender address | Email header analysis |
| Email Domain | Suspicious sender domain | Domain reputation check |
| URL | Suspicious website link | URL analysis |
| File Hash | Unique file identifier | VirusTotal |
| File Type | HTML, ISO, ZIP or other file | File analysis |
| IP Address | Suspicious network address | Threat Intelligence databases |

### 6.1 IOC Investigation

Analysts can use several tools:

**VirusTotal**

Used to check file hashes, URLs, domains, and IP addresses.

Website: https://www.virustotal.com/

**MITRE ATT&CK**

Used to identify attacker techniques and understand their behavior.

Website: https://attack.mitre.org/

**Google Safe Browsing**

Used to check potentially dangerous websites and URLs.

Website: https://safebrowsing.google.com/

**Important:** This report does not claim that new IOC values were collected or tested. Analysts should use verified indicators from reliable reports and security sources.

## 7. Detection Methods

Detecting phishing attacks requires monitoring both email activity and endpoint behavior.

### 7.1 Email Detection

Security analysts should:

- Check the sender's email address.
- Review email headers.
- Identify suspicious attachments.
- Check links before opening them.
- Look for unusual administrative messages.
- Compare sender domains with official organization domains.

### 7.2 Endpoint Detection with Sysmon

Sysmon can help analysts investigate suspicious activity on Windows systems.

Important Event IDs:

| Event ID | Description | Investigation Purpose |
|---|---|---|
| 1 | Process Creation | Detect suspicious processes |
| 3 | Network Connection | Monitor network connections |
| 7 | Image Loaded | Investigate DLL loading |
| 11 | File Create | Detect suspicious file creation |
| 22 | DNS Query | Investigate suspicious domain requests |

For example, analysts can investigate:

- HTML files creating unexpected ISO or IMG files.
- Unusual processes launched by Windows Explorer.
- Suspicious DLL loading.
- Unexpected network connections.
- Unusual PowerShell execution.

### 7.3 Splunk Monitoring

Splunk can collect and analyze Sysmon events.

Security analysts can use Splunk to:

- Search for suspicious process creation.
- Investigate unusual file creation.
- Monitor network connections.
- Identify suspicious PowerShell commands.
- Correlate multiple events to understand attack activity.

A combination of Sysmon and Splunk can help detect suspicious behavior after a phishing email is opened.

## 8. Prevention and Mitigation

Organizations can reduce phishing risks by using several security measures.

**Email Security**
- Use email security gateways.
- Filter suspicious attachments.
- Block known malicious domains.
- Use SPF, DKIM, and DMARC.

**Endpoint Security**
- Use antivirus and EDR solutions.
- Monitor suspicious processes.
- Restrict unnecessary script execution.
- Keep operating systems updated.

**User Awareness**
- Train employees to recognize phishing emails.
- Check unexpected attachments.
- Avoid suspicious links.
- Report unusual messages to the security team.

**Threat Intelligence**
- Monitor new APT29 reports.
- Check suspicious URLs and file hashes.
- Use MITRE ATT&CK for threat mapping.
- Share verified indicators with security teams.

## 9. Conclusion

During Week 10, I studied APT29 and its phishing operations against diplomatic organizations.

The analysis showed that phishing can be the first stage of a complex cyberattack.

APT29 used social engineering, malicious HTML files, HTML Smuggling, and legitimate web services to deliver malware and communicate with compromised systems.

The MITRE ATT&CK mapping included 10 techniques from different APT29 operations. These techniques helped explain the different stages of an attack, including Initial Access, Execution, Defense Evasion, Credential Access, Persistence, Discovery, and Command and Control.

I also studied how Threat Intelligence indicators can help identify suspicious emails, domains, URLs, and files.

Finally, I learned how Sysmon and Splunk can support security monitoring and help analysts investigate suspicious activity.

**Main conclusion:** Threat Intelligence is important because it helps security analysts understand attacker behavior, identify possible threats, and improve organizational security.

## 10. References

1. Mandiant. (2022). [Tracking APT29 Phishing Campaigns](https://cloud.google.com/blog/topics/threat-intelligence/tracking-apt29-phishing-campaigns).

2. Mandiant. (2023). [Backchannel Diplomacy: APT29's Rapidly Evolving Diplomatic Phishing Operations](https://cloud.google.com/blog/topics/threat-intelligence/apt29-evolving-diplomatic-phishing).

3. MITRE ATT&CK. [APT29 — Group G0118](https://attack.mitre.org/groups/G0118/).

4. MITRE ATT&CK. [Phishing — T1566](https://attack.mitre.org/techniques/T1566/).

5. MITRE ATT&CK. [User Execution — T1204](https://attack.mitre.org/techniques/T1204/).

6. MITRE ATT&CK. [Obfuscated Files or Information — T1027](https://attack.mitre.org/techniques/T1027/).

7. MITRE ATT&CK. [Web Service — T1102](https://attack.mitre.org/techniques/T1102/).

8. VirusTotal. [Official Website](https://www.virustotal.com/).

9. Microsoft. [Sysmon Documentation](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

10. Splunk. [Official Documentation](https://docs.splunk.com/).
