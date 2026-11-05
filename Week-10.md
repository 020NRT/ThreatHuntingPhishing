Week 10: Phishing Threat Intelligence Analysis — APT29
1. Objective
The goal of this lab is to study phishing attacks used by APT29. I will look at the group's methods, study its TTPs, and connect ten techniques to the MITRE ATT&CK framework.

This report is about Phishing Threat Intelligence Analysis. It explains how attackers use phishing to enter a system and how security teams can find and stop these attacks.
2. APT29 Overview
APT29 is a cyber threat group. It is also known as Cozy Bear and Midnight Blizzard. Public reports link this group to Russia's Foreign Intelligence Service (SVR).

APT29 has attacked government and diplomatic organizations. The group tries to get private information and keep access to computer systems.

APT29 is important for phishing analysis because it uses targeted phishing emails. These emails can help attackers enter a victim's system.
3. APT29 Phishing Campaign Analysis
This section looks at phishing activity reported by security researchers, including attacks against diplomatic organizations.
3.1 Social Engineering
Social engineering means tricking people. Attackers can send emails that look like real work messages or official notices. The goal is to make the user trust the email.
3.2 Spearphishing
Spearphishing is a phishing attack against a specific person or organization. Attackers may use the target's job or interests to make the email look real.
3.3 Malicious HTML and HTML Smuggling
Some reported attacks used HTML files to deliver harmful content.

HTML smuggling is a method that can create or download a file on the victim's computer through a web browser. Attackers may use this method to hide harmful files from some security tools.
3.4 Why This Is Important
When an analyst checks a phishing email, they should look at:
- the sender's email address;
- the sender's domain;
- links in the email;
- attached files;
- file names and file types;
- file hashes, if a file is available;
- activity on the computer after the email is opened.
This information can help analysts understand the attack and find similar threats.
4. MITRE ATT&CK Mapping — 10 Techniques
The table below shows ten techniques linked to APT29 reports or to different stages of its attacks. These techniques are from different operations. This does not mean that all ten techniques were used in one phishing campaign.
No.	Technique ID	Technique	Tactic	Connection to the attack
1	T1586.002	Compromise Accounts: Email Accounts	Resource Development	Attackers may take control of email accounts to prepare an attack or send trusted-looking messages.
2	T1566.001	Spearphishing Attachment	Initial Access	Attackers send a targeted email with a harmful file.
3	T1566.002	Spearphishing Link	Initial Access	Attackers send a targeted email with a harmful link.
4	T1566.003	Spearphishing via Service	Initial Access	Attackers use an online service to send phishing messages.
5	T1204.001	User Execution: Malicious Link	Execution	The user clicks a harmful link.
6	T1204.002	User Execution: Malicious File	Execution	The user opens a harmful file from an email.
7	T1027.006	HTML Smuggling	Defense Evasion	Attackers use HTML to create or deliver a harmful file on the victim's computer.
8	T1059.001	PowerShell	Execution	Attackers may use PowerShell to run commands or scripts.
9	T1078	Valid Accounts	Defense Evasion, Persistence, Initial Access	Attackers use real accounts that they have stolen or taken control of.
10	T1102.002	Web Service: Bidirectional Communication	Command and Control	Attackers use a web service to send and receive information from a compromised computer.


4.1 Mapping Summary
The first seven techniques show different parts of phishing and user activity. The last three show actions that may happen after attackers enter a system.

It is important to remember:
- A technique linked to APT29 was not used in every APT29 attack.
- Some techniques are not phishing techniques. They show what attackers may do after they get access.
- We need a report about a specific attack to confirm which techniques were used in that attack.
5. Threat Intelligence Indicators (IOCs)
IOC means Indicator of Compromise. It is a sign that may show that a system or account is under attack.
Indicator	Meaning	What an analyst checks
Sender email address	The email address of the sender	Is the sender real and trusted?
Sender domain	The domain in the email address	Does the domain look strange or fake?
URL	A link in the email	Does the link lead to a dangerous website?
IP address	An internet address linked to a website or server	Is the IP address known as dangerous?
Attachment	A file sent with the email	Is the file type or name unusual?
File hash	A unique value for a file	Is the file hash known as harmful?


5.1 IOC Investigation Steps
1. Save the suspicious email and its email headers.
2. Find the sender, domain, links, and attachments.
3. Check the links and file hashes with trusted tools, such as VirusTotal.
4. Write down the results and the source of the information.
5. Check computer and network logs for related activity.
6. Compare all results before deciding that the email is dangerous.
Note: This report explains how to check IOCs. It does not show real IOC values or VirusTotal results because these values must be collected and checked first.
6. Detection Methods
Companies can use email tools, computer logs, and network logs to find phishing attacks.
6.1 Email Detection
- Check the sender's email address and domain.
- Use SPF, DKIM, and DMARC to help stop fake emails.
- Check links and attachments.
- Look carefully at unexpected HTML files.
6.2 Computer Detection
- Check which programs start after a user opens an email attachment.
- Look for strange PowerShell activity.
- Use Sysmon to record process and network activity.
- Compare the time of the email with the time of computer activity.
6.3 Splunk and Threat Hunting
Splunk can collect and search security logs. An analyst can search for:
- suspicious domains and URLs;
- known harmful file hashes;
- strange processes started by a browser or email program;
- unusual PowerShell commands;
- unexpected network connections.
One event does not always mean that an attack happened. The analyst must check the user, time, process, command, and network address.
7. Prevention and Mitigation
Organizations can use these steps to reduce phishing risks:
1. Email security: block suspicious emails, links, and files.
2. Email authentication: use SPF, DKIM, and DMARC.
3. User training: teach employees how to find fake emails.
4. Least privilege: give users only the access they need.
5. Multi-factor authentication: add another step when users sign in.
6. Endpoint protection: check files, programs, and scripts.
7. Logging: collect email, computer, and network logs.
8. Incident response: block harmful links, protect accounts, and check infected computers.
8. Conclusion
In this lab, I studied phishing methods linked to APT29. I looked at social engineering, spearphishing, harmful HTML files, and HTML smuggling.

I also mapped ten techniques to MITRE ATT&CK. The table includes phishing techniques and other actions that may happen after attackers enter a system. These techniques are linked to different APT29 operations, not all to one campaign.

Threat intelligence helps security teams study suspicious emails, check IOCs, understand attacker methods, and improve detection. This work is connected to my project topic: Phishing Threat Intelligence Analysis.
9. References
1. Google Cloud / Mandiant — Tracking APT29 Phishing Campaigns
2. MITRE ATT&CK — APT29 (G0118)
3. MITRE ATT&CK — Phishing (T1566)
4. MITRE ATT&CK — User Execution (T1204)
5. MITRE ATT&CK — HTML Smuggling (T1027.006)
6. MITRE ATT&CK — PowerShell (T1059.001)
7. MITRE ATT&CK — Valid Accounts (T1078)
8. MITRE ATT&CK — Web Service: Bidirectional Communication (T1102.002)
