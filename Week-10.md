# Week 10: APT29 Analysis

## Objective
I need to analyze the TTPs (Tactics, Techniques, and Procedures) of APT29. Then, I need to map these techniques to the MITRE ATT&CK framework.

## What is APT29?
APT29 is a hacker group. People also call them Cozy Bear or Midnight Blizzard. 
They are from Russia. They work for the Russian government (SVR). 
They hack governments and companies to steal secrets. 
They are very quiet and they stay in the network for a long time.

## MITRE ATT&CK Mapping

Here is a table of what APT29 does and how it connects to MITRE ATT&CK:

| Tactic | Technique ID | Technique Name | What APT29 does |
| :--- | :--- | :--- | :--- |
| **Initial Access** | T1566.001 | Spearphishing Attachment | They send bad files in emails to start hacking. |
| **Execution** | T1059.001 | PowerShell | They use PowerShell to run bad commands. |
| **Persistence** | T1547.001 | Registry Run Keys | They change the registry so their virus starts when the PC turns on. |
| **Defense Evasion** | T1027 | Obfuscated Files | They hide their bad code so antivirus cannot see it. |
| **Credential Access** | T1555.003 | Credentials from Web Browsers | They steal saved passwords from Google Chrome. |
| **Command and Control** | T1102 | Web Service | They use normal websites (like Dropbox or Twitter) to talk to the virus. |

**Screenshot of MITRE ATT&CK:**
![APT29 MITRE Techniques](screenshots/APT29_mitre.png)

## Important Techniques
1. **Supply Chain Attack:** In 2020, they hacked a company called SolarWinds. They put a virus inside a normal software update. Many big companies downloaded it and got hacked.
2. **Living off the Land:** They use normal Windows tools (like `cmd.exe` or `rundll32.exe`). This is hard to catch because these tools are not viruses.

## Summary
APT29 is very dangerous because they are very slow and smart. They do not break things. They just steal information. 
To stop them, companies must check their emails carefully and watch for strange PowerShell commands.

## References
- MITRE ATT&CK APT29: https://attack.mitre.org/groups/G0016/
- Mandiant APT1 Report
- CrowdStrike Global Threat Report

---
## AI Usage Disclosure

I used an AI (ChatGPT) to help me with this task. 
The AI helped me read about APT29. The AI gave me the table with the MITRE ATT&CK numbers. The AI also helped me write this text in simple English. 
I did the research myself. I read the MITRE website. I checked the information.
