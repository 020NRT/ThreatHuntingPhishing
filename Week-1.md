# Phishing Threat Intelligence Analysis

## Task: Create a Glossary of Key CTI Terms and Classify Threats

### 1. Glossary of Key CTI Terms

| Term                                          | Definition                                                                                           |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **CTI (Cyber Threat Intelligence)**           | Information about cyber threats that helps organizations understand, detect, and prevent attacks.    |
| **Phishing**                                  | An attack where criminals pretend to be a trusted person or company to steal sensitive information.  |
| **IOC (Indicator of Compromise)**             | Evidence of possible malicious activity, such as an IP address, domain, URL, or file hash.           |
| **TTP (Tactics, Techniques, and Procedures)** | Methods and techniques used by attackers during cyberattacks.                                        |
| **Threat Actor**                              | A person or group responsible for a cyberattack.                                                     |
| **Malicious URL**                             | A harmful link used for phishing, malware delivery, or credential theft.                             |
| **Malicious Domain**                          | A domain used to host phishing pages, malware, or other malicious content.                           |
| **Spoofing**                                  | Pretending to be a trusted sender, website, or organization.                                         |
| **Social Engineering**                        | Manipulating people into giving sensitive information or performing unsafe actions.                  |
| **Spear Phishing**                            | A targeted phishing attack against a specific person or organization.                                |
| **Smishing**                                  | Phishing attacks performed through SMS messages.                                                     |
| **Vishing**                                   | Phishing attacks performed through phone or voice calls.                                             |
| **Credential Theft**                          | Stealing usernames, passwords, or other login information.                                           |
| **OSINT**                                     | Collecting intelligence from publicly available sources.                                             |
| **Threat Feed**                               | A source that provides information about known malicious IPs, domains, URLs, hashes, and other IOCs. |

---

## 2. Classification of Phishing Threats

| Threat Type                         | Description                                                                     | Example                               |
| ----------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------- |
| **Email Phishing**                  | Fake emails are sent to users to steal information.                             | Fake password reset email             |
| **Spear Phishing**                  | A phishing attack targets a specific person or company.                         | Fake email sent to a company employee |
| **Smishing**                        | Phishing is performed through SMS messages.                                     | Fake bank SMS with a malicious link   |
| **Vishing**                         | Attackers use phone calls to manipulate victims.                                | Fake bank support call                |
| **Clone Phishing**                  | A legitimate message is copied and modified with malicious content.             | Fake delivery notification            |
| **Credential Phishing**             | Fake login pages are used to steal usernames and passwords.                     | Fake Microsoft 365 login page         |
| **Malware Phishing**                | Emails or messages contain malicious files or links.                            | Email with a malicious attachment     |
| **Business Email Compromise (BEC)** | Attackers impersonate employees or managers to request money or sensitive data. | Fake CEO requesting a payment         |

---

## 3. Sources of Phishing Threats

Phishing attacks can come from different sources:

* **Cybercriminals** – use phishing to steal money, passwords, and personal information.
* **Organized threat groups** – may use targeted phishing to gain access to organizations.
* **Insider threats** – employees or contractors may misuse their access or company information.
* **Automated phishing campaigns** – attackers use automated tools to send phishing messages to many users.

### CTI and OSINT Data Sources

Information about phishing threats can be collected from:

* **VirusTotal** – analysis of suspicious URLs, domains, IP addresses, and files.
* **Shodan** – information about Internet-connected systems and infrastructure.
* **MISP** – collection, analysis, and sharing of threat intelligence and IOCs.
* **Public threat feeds** – lists of known malicious domains, IP addresses, URLs, and hashes.
* **Security reports** – reports published by cybersecurity companies and organizations.

---

## Conclusion

Phishing includes different types of attacks such as email phishing, spear phishing, smishing, vishing, credential phishing, and malware phishing.

Cyber Threat Intelligence helps analysts understand **who may be behind an attack, how the attack works, and what indicators can be used to detect it**. This information can help organizations detect and prevent future phishing attacks.
