# Cyber Kill Chain and MITRE ATT&CK Analysis

## Objective

The objective of this task is to analyze a real-world cyberattack using the Cyber Kill Chain and connect each attack stage with MITRE ATT&CK techniques.

For this analysis, the **TA459 phishing campaign** was selected. TA459 is a threat group that has used phishing emails with malicious Microsoft Word files.

---

## 1. Attack Overview

TA459 used phishing emails to attack victims.

The attackers sent emails with malicious Word documents. The goal was to make the victim open the attached file. After the victim opened the file, malicious code could run on the computer.

This attack shows how phishing and social engineering can be used to get access to a victim's system.

---

## 2. Cyber Kill Chain Analysis

The Cyber Kill Chain has seven main stages.

| Kill Chain Stage | Activity | MITRE ATT&CK |
|---|---|---|
| Reconnaissance | Collect information about the target | Reconnaissance |
| Weaponization | Prepare a malicious document | T1059.005 – Visual Basic |
| Delivery | Send the document by phishing email | T1566.001 – Spearphishing Attachment |
| Exploitation | Victim opens the malicious file | T1204.002 – Malicious File |
| Installation | Malicious code runs on the system | T1059 – Command and Scripting Interpreter |
| Command and Control | Malware communicates with the attacker | Command and Control |
| Actions on Objectives | Attacker collects or steals information | Collection / Exfiltration |

---

## 3. Reconnaissance

First, the attacker collects information about the target.

This information can include:

- Employee names
- Email addresses
- Job positions
- Company information
- Public social media information

The attacker can use this information to create a more realistic phishing email.

**MITRE ATT&CK tactic:** Reconnaissance

---

## 4. Weaponization

In this stage, the attacker prepares the malicious file.

For example, the attacker can create a Microsoft Word document with malicious VBA code or another payload.

**MITRE ATT&CK: T1059.005 – Visual Basic**

Attackers can use Visual Basic or VBA code inside Microsoft Office documents to run malicious commands.

---

## 5. Delivery

The attacker sends the malicious document to the victim by email.

TA459 has used spearphishing emails with malicious Microsoft Word attachments.

**MITRE ATT&CK: T1566.001 – Spearphishing Attachment**

This technique is used when an attacker sends a malicious file as an email attachment.

**Attack flow:**

Attacker → Phishing Email → Malicious Attachment → Victim

---

## 6. Exploitation

The victim opens the malicious Word document.

The attacker needs the victim to interact with the file so that the malicious code can run.

**MITRE ATT&CK: T1204.002 – User Execution: Malicious File**

This technique means that the attack depends on the user opening a malicious file.

**Attack flow:**

Phishing Email → Victim Opens File → Malicious Code Runs

---

## 7. Installation

After the victim opens the file, malicious code can run on the computer.

The malware may download other files, run commands, or make changes to the system.

**MITRE ATT&CK: T1059 – Command and Scripting Interpreter**

This technique allows attackers to use commands or scripts on the victim's system.

---

## 8. Command and Control

After the malware starts, it may connect to a server controlled by the attacker.

This connection allows the attacker to send commands and receive information from the infected computer.

Common communication methods include:

- HTTP
- HTTPS
- DNS

**MITRE ATT&CK tactic:** Command and Control

---

## 9. Actions on Objectives

In the final stage, the attacker tries to complete the main goal of the attack.

Possible actions include:

- Collecting system information
- Stealing usernames and passwords
- Collecting sensitive files
- Taking screenshots
- Monitoring user activity
- Sending stolen information to an external server

**MITRE ATT&CK tactics:** Collection, Credential Access, and Exfiltration.

---

## 10. Full Attack Flow

Reconnaissance  
↓  
Collect Target Information  
↓  
Weaponization  
↓  
Create Malicious Word Document  
↓  
Delivery  
↓  
Send Phishing Email  
↓  
Exploitation  
↓  
Victim Opens File  
↓  
Installation  
↓  
Malicious Code Runs  
↓  
Command and Control  
↓  
Connect to Attacker Server  
↓  
Actions on Objectives  
↓  
Collect or Steal Information

---

## 11. Main MITRE ATT&CK Techniques

| ATT&CK ID | Technique | Purpose |
|---|---|---|
| T1566.001 | Spearphishing Attachment | Send a malicious file by email |
| T1204.002 | User Execution: Malicious File | Make the victim open the file |
| T1059.005 | Visual Basic | Run malicious VBA or Visual Basic code |
| T1059 | Command and Scripting Interpreter | Run commands or scripts |

---

## Conclusion

The Cyber Kill Chain helps us understand the main stages of a cyberattack. MITRE ATT&CK gives more detailed information about the techniques used by attackers.

In the TA459 phishing campaign, attackers used phishing emails with malicious Word documents. The victim had to open the file to start the malicious code. After that, the attacker could run commands, communicate with the infected system, and collect information.

Using the Cyber Kill Chain together with MITRE ATT&CK helps security teams understand attacks and find ways to detect or stop them.
