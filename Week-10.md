# Week 10: APT29 (Cozy Bear) TTP Analysis & MITRE ATT&CK Mapping

## Objective
Analyze the Tactics, Techniques, and Procedures (TTPs) of the threat actor APT29 (also known as Cozy Bear, Midnight Blizzard, or UNC2452) and map their observed behaviors to the MITRE ATT&CK framework.

## Threat Actor Overview: APT29
- **Attribution:** Widely assessed to be associated with Russia's Foreign Intelligence Service (SVR) [citation:1].
- **Motivation:** Cyber espionage, intelligence gathering, and long-term persistence in high-value targets (government, diplomatic, and technology sectors).
- **Notable Campaigns:** SolarWinds supply chain compromise (2020), Operation Ghost, and targeted phishing campaigns against diplomatic entities [citation:7].
- **Key Characteristics:** APT29 is known for being stealthy, patient, and using legitimate tools (Living off the Land) and compromised credentials to avoid detection.

## MITRE ATT&CK Mapping (Key TTPs)

The following table maps the observed behaviors of APT29 to specific MITRE ATT&CK techniques:

| Tactic | Technique ID | Technique Name | How APT29 Uses It |
| :--- | :--- | :--- | :--- |
| **Initial Access** | T1566.001 | Spearphishing Attachment | Used to deliver exploits or malicious files to initial victims via email . |
| **Initial Access** | T1078 | Valid Accounts | Used stolen or compromised credentials to access victim environments (e.g., via OAuth phishing or password spraying) [citation:1]. |
| **Execution** | T1059.001 | PowerShell | Uses encoded PowerShell scripts to download payloads, execute commands, and move laterally . |
| **Persistence** | T1547.001 | Registry Run Keys | Modifies registry keys to ensure malware (like the Dukes family) runs on startup . |
| **Persistence** | T1136.003 | Create Cloud Account | Creates new users in Azure AD to maintain access to cloud environments . |
| **Defense Evasion** | T1027 | Obfuscated Files/Information | Uses custom encryption and steganography (hiding data in images) to hide C2 traffic and payloads [citation:7]. |
| **Defense Evasion** | T1218.011 | Rundll32 | Uses `rundll32.exe` to execute malicious payloads, a common LOLBin technique . |
| **Credential Access** | T1110.003 | Password Spraying | Conducts brute-force password spray attacks against mailboxes and services . |
| **Credential Access** | T1555.003 | Credentials from Web Browsers | Stole saved passwords from Chrome during the SolarWinds campaign . |
| **Command and Control** | T1102 | Web Service | Uses legitimate services like Dropbox, Twitter, and Reddit as dead drops for C2 addresses [citation:7]. |
| **Command and Control** | T1090.003 | Multi-hop Proxy | Uses Tor and residential proxies to obfuscate their location and access [citation:1]. |

## Deep Dive into Key Techniques

### 1. Supply Chain Compromise (T1195)
While not always their primary entry point, APT29 is famous for the SolarWinds Orion supply chain attack. They injected malicious code (SUNBURST) into legitimate software updates. This allowed them to gain access to thousands of organizations without direct exploitation, showcasing a highly sophisticated level of **Resource Development (TA0042)**.

### 2. Living off the Land (LotL)
APT29 heavily relies on tools already present in the victim's environment (like PowerShell, `cmd.exe`, and `rundll32.exe`) . This makes detection difficult because these tools are normally used by administrators. For example, using `Get-ManagementRoleAssignment` via PowerShell to enumerate Exchange roles .

### 3. Cloud and Identity Focus
Recent analysis indicates a shift towards cloud environments. They abuse OAuth and device-code phishing to bypass Multi-Factor Authentication (MFA) [citation:1]. They also use Azure Run Command to execute code on virtual machines and create new cloud accounts for persistence .

## Summary & Key Takeaways
- **Stealth over Speed:** APT29 prioritizes staying hidden for long periods rather than quick financial gain.
- **Detection Difficulty:** Because they use legitimate tools and compromised accounts, signature-based detection (like antivirus) is often ineffective.
- **Defense Recommendations:**
  1.  Monitor for suspicious PowerShell and `rundll32` arguments (e.g., encoded commands).
  2.  Implement strict MFA and conditional access policies to prevent OAuth phishing.
  3.  Monitor for anomalous registry modifications and new account creations in cloud environments.

## Recommended Reading & References
- **Mandiant APT1 Report:** (Historical context on APT tracking) [citation:3]
- **CrowdStrike Global Threat Report 2026:** (Context on modern adversary speed and AI) [citation:4][citation:9]
- **MITRE ATT&CK - APT29 (G0016):** https://attack.mitre.org/groups/G0016/
- **Operation Ghost Analysis:** (Specific APT29 campaign) [citation:7]

---
## AI Usage Disclosure

I used an AI assistant (ChatGPT) to help me structure this week's report and map the TTPs of APT29 to the MITRE ATT&CK framework. The AI provided the table format and summarized the key techniques based on publicly available threat intelligence reports. I verified the information against the MITRE ATT&CK website and the recommended reading materials to ensure accuracy.
