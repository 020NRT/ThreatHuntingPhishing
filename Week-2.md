# OSINT Data Collection for Phishing Threat Intelligence

## Objective

The objective of this task is to perform OSINT data collection using
VirusTotal, Shodan, and Maltego.

The investigation focuses on one phishing URL. The purpose is to collect
Indicators of Compromise (IOCs), investigate related infrastructure,
and create a data source mapping for phishing threat analysis.

---

# 1. Phishing Indicator

The following URL was selected for investigation:

**URL:** `http://login-outlook365.yzz.me/`

**Domain:** `login-outlook365.yzz.me`

The URL was identified as a phishing indicator and was investigated
using different OSINT tools.

---

# 2. VirusTotal Analysis

The first step was to analyze the suspicious URL using VirusTotal.

VirusTotal was used to check:

- Security vendor detections
- URL reputation
- Domain information
- Related IP addresses
- URL categories
- Redirect information

## Results

| Indicator | Information |
|---|---|
| URL | http://login-outlook365.yzz.me/ |
| Domain | login-outlook365.yzz.me |
| Related IP | 77.72.1.44 |
| Security Detections | 21 / 92 |
| HTTP Status | 200 |
| Content Type | text/html |
| Redirect | https://suspended-domain.net/ |
| Threat Type | Phishing / Fraud |

Several security vendors categorized the URL as phishing or fraud.

The analysis also showed that the domain was associated with the
IP address:

`77.72.1.44`

This IP address was used for the next stage of the OSINT investigation.

### VirusTotal Analysis

VirusTotal provided useful information about the suspicious URL and
helped identify an associated IP address.

The fact that 21 security engines detected the URL as malicious or
suspicious provides additional evidence that the URL was associated
with malicious activity.

The URL currently redirects to `suspended-domain.net`, which suggests
that the original domain may no longer be serving its previous content.

---

# 3. Shodan Analysis

After obtaining the IP address from VirusTotal, I investigated it using
Shodan.

**Investigated IP:**

`77.72.1.44`

Shodan was used to collect information about the network infrastructure
associated with this IP address.

## Results

| Indicator | Information |
|---|---|
| IP Address | 77.72.1.44 |
| Open Ports | 80, 110, 143, 443, 2082, 2083, 2095, 2096 |
| Web Service | HTTP |
| Web Server | OpenResty 1.31.1.1 |
| Last Seen | September 24, 2026 |

Shodan also displayed several domains and hostnames associated with the
same IP infrastructure.

Examples included:

- `gavshop.com`
- `gregoryav.co.uk`
- `k-hosting.co.uk`
- `krystal.uk`

## Infrastructure Analysis

The Shodan results showed several open ports on the server.

Examples include:

- Port 80 – HTTP
- Port 110 – POP3
- Port 143 – IMAP
- Port 443 – HTTPS
- Ports 2082/2083 – commonly associated with hosting control services
- Ports 2095/2096 – commonly associated with webmail services

Port 80 was running an HTTP service using OpenResty.

The presence of several domains and hostnames on the same IP suggests
that the server may be part of shared hosting infrastructure.

Therefore, the IP address itself should not automatically be classified
as malicious only because a phishing domain was associated with it.

Shodan helped expand the investigation from a phishing URL to the
network infrastructure associated with the indicator.

---

# 4. Maltego Analysis

The next step was to investigate the phishing domain using Maltego.

The following domain was added as an entity:

`login-outlook365.yzz.me`

Maltego was used to investigate possible relationships between the
domain and other infrastructure.

## Transform

I performed an:

**MX Lookup**

The purpose of this transform was to identify possible mail
infrastructure associated with the domain.

## Results

| Indicator | Information |
|---|---|
| Domain | login-outlook365.yzz.me |
| Tool | Maltego |
| Transform | MX Lookup |
| Additional Entities | None |
| Links | 0 |
| Transform Result | Completed with issues |

The transform completed with issues and did not discover additional
entities or relationships.

The available transforms were limited in the current Maltego
configuration, so additional domain-to-IP relationships could not be
retrieved directly through Maltego.

This is still useful information because OSINT investigations do not
always return additional relationships for every indicator.

---

# 5. Data Source Mapping

The collected information can be mapped between the different OSINT
sources.

| Data Source | Input | Data Collected | Purpose |
|---|---|---|---|
| VirusTotal | Phishing URL | Detections, domain, IP, categories, redirect | Identify and analyze malicious IOC |
| Shodan | 77.72.1.44 | Open ports, services, hostnames and server information | Investigate network infrastructure |
| Maltego | login-outlook365.yzz.me | Domain entity and MX lookup | Investigate and visualize relationships |

---

# 6. OSINT Investigation Workflow

The investigation followed this process:

Phishing URL  
↓  
**VirusTotal**  
↓  
Domain: `login-outlook365.yzz.me`  
↓  
IP Address: `77.72.1.44`  
↓  
**Shodan**  
↓  
Open Ports + Services + Related Infrastructure  
↓  
**Maltego**  
↓  
Domain Relationship Investigation

---

# 7. Indicators of Compromise

The main indicators collected during the investigation were:

| IOC Type | Indicator | Source |
|---|---|---|
| URL | http://login-outlook365.yzz.me/ | VirusTotal |
| Domain | login-outlook365.yzz.me | VirusTotal / Maltego |
| IP Address | 77.72.1.44 | VirusTotal / Shodan |
| Threat Category | Phishing / Fraud | VirusTotal |
| Web Server | OpenResty 1.31.1.1 | Shodan |

The domain and URL are the main phishing indicators investigated in
this report.

The IP address should be treated as related infrastructure rather than
automatically classified as malicious because Shodan indicates that
multiple domains and services may share the same infrastructure.

---

# Conclusion

This investigation demonstrated how multiple OSINT tools can be combined
for phishing threat intelligence analysis.

VirusTotal was used to analyze the phishing URL and identify the related
IP address `77.72.1.44`.

Shodan was then used to investigate this IP address. It revealed several
open ports, services, hostnames, and related domains, providing more
information about the infrastructure.

Finally, Maltego was used to investigate the domain and search for
additional relationships. The MX Lookup did not return additional
entities, but it demonstrated how graph-based OSINT tools can be used
to search for relationships between threat indicators.

By combining information from VirusTotal, Shodan, and Maltego, CTI
analysts can move from a single suspicious URL to a broader
understanding of its associated infrastructure and indicators.
