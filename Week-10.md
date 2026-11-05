<div align="center">Week 10 — Phishing Threat Intelligence Analysis
APT29 | MITRE ATT&CK | Indicators of Compromise | Detection



</div>Table of Contents
- 1. Objective
- 2. APT29 Overview
- 3. APT29 Phishing Campaign Analysis
  - 3.1 Social Engineering
  - 3.2 Spearphishing
  - 3.3 Malicious HTML and HTML Smuggling
  - 3.4 Analysis Points
- 4. MITRE ATT&CK Mapping
  - 4.1 Mapping Summary
- 5. Threat Intelligence Indicators (IOCs)
  - 5.1 IOC Investigation Steps
- 6. Detection Methods
  - 6.1 Email Detection
  - 6.2 Endpoint Detection
  - 6.3 Splunk and Threat Hunting
- 7. Prevention and Mitigation
- 8. Conclusion
- 9. References
1. Objective
The goal of this lab is to study phishing attacks and methods linked to APT29. I will review the group's methods, study its tactics, techniques, and procedures (TTPs), and map ten techniques to the MITRE ATT&CK framework.

This report is connected to my project topic: Phishing Threat Intelligence Analysis. It explains how attackers use phishing to gain access to systems and how security teams can detect and prevent these attacks.
2. APT29 Overview
APT29 is a cyber threat group. It is also known as Cozy Bear and Midnight Blizzard. Public reports link this group to Russia's Foreign Intelligence Service (SVR).

APT29 has targeted government and diplomatic organizations. The group tries to collect sensitive information and keep access to computer systems.

APT29 is important for phishing analysis because it has used targeted phishing messages. These messages can help attackers gain access to a victim's system.
3. APT29 Phishing Campaign Analysis
This section reviews phishing activity reported by security researchers, including activity targeting diplomatic organizations.
3.1 Social Engineering
Social engineering means tricking people. Attackers can send emails that look like real work messages or official notices. The goal is to make the user trust the message and take an action.
3.2 Spearphishing
Spearphishing is a phishing attack against a specific person or organization. Attackers may use information about the target's job or interests to make a message look real.

Common things to examine include:
- the sender's email address and domain;
- the message subject and wording;
- links included in the message;
- attached files and file types;
- the action requested from the recipient.
3.3 Malicious HTML and HTML Smuggling
Some reported attacks have used HTML files to deliver harmful content.

HTML smuggling is a technique that uses HTML and JavaScript in a browser to create or deliver a file on the victim's computer. Attackers may use it to make harmful files harder for some security tools to detect.
3.4 Analysis Points
When an analyst investigates a suspicious email, they should check:
1. The sender's email address.
2. The sender's domain and email headers.
3. Links and the domains they lead to.
4. Attached files, names, and file types.
5. File hashes, if a file is available.
6. Computer activity after the email is opened.
This information can help analysts understand the attack and search for related activity.
Important: The techniques in this report may come from different APT29 operations. This report does not claim that all ten techniques were used in one phishing campaign.

4. MITRE ATT&CK Mapping — 10 Techniques
The table connects ten techniques with phishing activity or other stages of an intrusion. The mapping is intended to show how phishing can fit into a wider attack lifecycle.
#	Technique ID	Technique	Tactic	Connection to the attack
1	T1586.002	Compromise Accounts: Email Accounts	Resource Development	Attackers may take control of email accounts to prepare an attack or send trusted-looking messages.
2	T1566.001	Spearphishing Attachment	Initial Access	Attackers send a targeted email with a harmful file.
3	T1566.002	Spearphishing Link	Initial Access	Attackers send a targeted email with a harmful link.
4	T1566.003	Spearphishing via Service	Initial Access	Attackers use an online service to send phishing messages.
5	T1204.001	User Execution: Malicious Link	Execution	The user clicks a harmful link.
6	T1204.002	User Execution: Malicious File	Execution	The user opens a harmful file received in a message.
7	T1027.006	HTML Smuggling	Defense Evasion	Attackers use HTML to create or deliver a harmful file on the victim's computer.
8	T1059.001	PowerShell	Execution	Attackers may use PowerShell to run commands or scripts after gaining access.
9	T1078	Valid Accounts	Defense Evasion, Persistence, Initial Access	Attackers use real accounts that they have stolen or taken control of.
10	T1102.002	Web Service: Bidirectional Communication	Command and Control	Attackers use a web service to send and receive information from a compromised computer.


4.1 Mapping Summary
- Techniques T1566.001, T1566.002, and T1566.003 describe phishing delivery methods.
- Techniques T1204.001 and T1204.002 describe actions taken by the user.
- T1027.006 describes an evasion method that may be used to deliver a file.
- T1059.001, T1078, and T1102.002 describe activity that may happen during later stages of an intrusion.
Note: A technique associated with a threat group is not necessarily used in every operation. A specific incident report is needed to confirm which techniques were used in a particular campaign.

5. Threat Intelligence Indicators (IOCs)
IOC means Indicator of Compromise. It is a sign that may show that a system or account is involved in suspicious activity.
Indicator	Meaning	What an analyst checks
Sender email address	The address of the message sender	Is the sender real and trusted?
Sender domain	The domain used in the sender's address	Does the domain look unusual or imitate a real organization?
URL	A link included in the email	Does it lead to a suspicious or harmful website?
IP address	An internet address linked to a website or server	Is the address connected to known malicious activity?
Attachment	A file sent with the email	Is the file name or type unusual?
File hash	A value that identifies a file	Is the hash known to be malicious?


5.1 IOC Investigation Steps
1. Save the suspicious email and its headers.
2. Identify the sender, domain, links, and attachments.
3. Check links and file hashes with trusted security services, such as VirusTotal.
4. Record the results and the source of each indicator.
5. Check computer and network logs for related activity.
6. Compare the evidence before deciding whether the email is malicious.
Data note: This report describes an IOC investigation process. It does not provide real IOC values or claim VirusTotal results. Those values must be collected and verified during an actual investigation.

6. Detection Methods
Organizations can use email security tools, endpoint logs, and network logs to detect phishing activity.
6.1 Email Detection
- Check the sender's email address and domain.
- Use SPF, DKIM, and DMARC to help detect or prevent spoofed emails.
- Scan links and attachments.
- Review unexpected HTML files carefully.
6.2 Endpoint Detection
- Check which programs start after a user opens an attachment.
- Look for unusual PowerShell activity.
- Use Sysmon to record process and network activity.
- Compare the time of the email with the time of endpoint activity.
6.3 Splunk and Threat Hunting
Splunk can collect and search security logs. An analyst can search for:
- suspicious domains and URLs;
- known malicious file hashes;
- unusual processes started by a browser or email program;
- unexpected PowerShell commands;
- unusual network connections.
One event does not always mean that an attack happened. The analyst should check the user, time, process, command, and network address before making a conclusion.
7. Prevention and Mitigation
Organizations can use the following steps to reduce phishing risks:
1. Email security: block suspicious emails, links, and files.
2. Email authentication: configure SPF, DKIM, and DMARC.
3. User training: teach employees how to recognize suspicious messages.
4. Least privilege: give users only the access they need.
5. Multi-factor authentication (MFA): add another verification step during sign-in.
6. Endpoint protection: monitor files, programs, and scripts.
7. Logging: collect email, endpoint, and network logs.
8. Incident response: block harmful links, secure affected accounts, and investigate infected computers.
8. Conclusion
In this lab, I studied phishing methods and techniques connected to APT29. I reviewed social engineering, spearphishing, malicious HTML files, and HTML smuggling.

I also mapped ten techniques to MITRE ATT&CK. The mapping includes phishing techniques and other actions that may happen after attackers gain access. The techniques can relate to different operations and should not be treated as one confirmed campaign.

Threat intelligence helps security teams investigate suspicious emails, verify IOCs, understand attacker methods, and improve detection. This work supports my project topic: Phishing Threat Intelligence Analysis.
9. References
1. Google Cloud / Mandiant — Tracking APT29 Phishing Campaigns
2. MITRE ATT&CK — APT29 (G0118)
3. MITRE ATT&CK — Phishing (T1566)
4. MITRE ATT&CK — User Execution (T1204)
5. MITRE ATT&CK — HTML Smuggling (T1027.006)
6. MITRE ATT&CK — PowerShell (T1059.001)
7. MITRE ATT&CK — Valid Accounts (T1078)
8. MITRE ATT&CK — Web Service: Bidirectional Communication (T1102.002)
<div align="center">Week 10 — Phishing Threat Intelligence Analysis
</div>
