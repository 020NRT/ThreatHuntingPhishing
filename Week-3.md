# MISP Deployment and IOC Preparation

## Objective

The objective of this task was to deploy MISP and prepare collected Indicators of Compromise (IOCs) for threat intelligence analysis.

## 1. MISP Deployment

MISP was deployed on Windows using Docker Desktop.

The official MISP Docker project was downloaded and configured. The project directory contained the Docker Compose configuration, environment file, MISP core, modules, Nginx, database, and other required components.

The following command was used to start the environment:

docker compose up -d

Docker created the required containers, including:

- MISP Core
- MISP Modules
- MariaDB
- Redis
- Nginx
- Mail service

During deployment, MariaDB, Redis, and MISP Modules successfully reached a healthy state. MISP Core had a health-check issue, so the complete web interface deployment was not finished.

## 2. IOC Collection

The IOCs were collected during the previous phishing OSINT investigation using VirusTotal, Shodan, and Maltego.

Collected indicators:

| IOC Type | Value |
|---|---|
| URL | http://login-outlook365.yzz.me/ |
| Domain | login-outlook365.yzz.me |
| IP Address | 77.72.1.44 |

The URL and domain were related to the investigated phishing activity.

The IP address was identified as related infrastructure. It was not automatically classified as malicious because the server appeared to host multiple domains.

## 3. IOC Preparation for MISP

The collected indicators were prepared using standard MISP attribute types.

| Raw Data | MISP Attribute Type |
|---|---|
| http://login-outlook365.yzz.me/ | url |
| login-outlook365.yzz.me | domain |
| 77.72.1.44 | ip-dst |

This structure makes the indicators easier to search, filter, and analyze in MISP.

## 4. Filtering

The prepared IOC data can be filtered by indicator type.

For example:

- Type = `url` → shows the phishing URL
- Type = `domain` → shows the phishing domain
- Type = `ip-dst` → shows the related IP address

Filtering helps analysts quickly find specific indicators in a larger threat intelligence dataset.

## 5. Data Normalization

The collected OSINT data was normalized before analysis.

The following normalization techniques were applied:

- The domain was stored in lowercase.
- The URL was stored using a consistent URL format.
- The IP address was stored in standard IPv4 format.
- Different indicators were separated into URL, domain, and IP types.
- Duplicate indicators were removed.
- The source and context of each indicator were preserved.

Normalization makes threat intelligence data more consistent and easier to analyze.

## 6. Investigation Workflow

The complete workflow of the project was:

PhishTank
↓
VirusTotal
↓
Shodan
↓
Maltego
↓
IOC Collection
↓
MISP-compatible IOC Preparation
↓
Filtering
↓
Normalization

## Conclusion

In this task, a local MISP environment was prepared using Docker Desktop. Several MISP services were successfully deployed, although the MISP Core container required additional troubleshooting.

The phishing indicators collected during the OSINT investigation were organized into MISP-compatible attribute types. Filtering and normalization techniques were also applied to prepare the data for threat intelligence analysis.
