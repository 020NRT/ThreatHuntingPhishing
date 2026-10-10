# Week 5 — Hypothesis-Driven Hunting: Phishing Threat Intelligence

## Objective
Build and test a threat hunting hypothesis using phishing indicators collected in earlier weeks. The hunt uses Splunk Search Processing Language (SPL).

## Previous research
This project extends [ThreatHuntingPhishing](https://github.com/020NRT/ThreatHuntingPhishing), especially Week 3 IOC preparation and Week 4 ATT&CK analysis. Its layout is inspired by [simulated-infostealer-threat-hunting](https://github.com/User-ease/simulated-infostealer-threat-hunting), but the data and queries are independently prepared.

## Hypothesis
If an endpoint interacts with a known phishing domain, the domain or URL may appear in DNS and proxy logs. Network traffic to a related IP can provide additional context, but an IP match alone does not prove phishing.

## Threat intelligence indicators
| Type | Value | Interpretation |
|---|---|---|
| Domain | `login-outlook365.yzz.me` | Phishing indicator from earlier OSINT research |
| URL | `http://login-outlook365.yzz.me/` | Investigated phishing URL; **do not visit** |
| IP | `77.72.1.44` | Related infrastructure only; shared hosting may cause false positives |

These are historical research indicators, not verified live threats as of this report. The synthetic log file uses them as inert strings; it never connects to them.

## Dataset
`data/synthetic_phishing_logs.csv` contains 8 fictional events from 5 fictional hosts: DNS, proxy and firewall telemetry. It is **synthetic**, not collected from real systems. Timestamps are invented test timestamps. Do not describe these as real incidents.

## Hunt procedure in Splunk
1. Open Splunk Web → Settings → Add Data → Upload.
2. Select `data/synthetic_phishing_logs.csv`; set sourcetype to `phishing:csv` (CSV with header); select/create index `phishing_lab`.
3. Configure `_time` as event time using the ISO 8601 timestamp column; if necessary set `TIME_FORMAT=%Y-%m-%dT%H:%M:%SZ` and `TIMESTAMP_FIELDS=_time` in a custom sourcetype.
4. Open Search & Reporting. Choose **All time** and run each query from `queries/hunt.spl` separately (not all at once).
5. Record actual counts and capture screenshots of each search, including search bar, selected time range and results. Put them in `evidence/`.
6. If CSV field names or index differ, update the queries to match the actual imported events.

## Simulated results (offline validation, not observed Splunk results)
| Query | Expected matches |
|---|---|
| DNS phishing domain | 2 events (PC-01, PC-04) |
| Proxy phishing URL | 1 event (PC-01) |
| Related IP | 2 events (PC-01, PC-03); context only |
| Host correlation | 1 host (PC-01), three indicator types |

Run `python scripts/validate.py` to verify the dataset independently of Splunk. Detailed results and analyst assessment are in [`evidence/RESULTS.md`](evidence/RESULTS.md). This is **not** a substitute for executing SPL.

## Analysis
PC-01 has DNS, proxy, and network events matching the test indicators. PC-04 has a domain match only. PC-03 has an IP match only, which is insufficient to label it compromised. In this simulation, the hypothesis is supported by the planted telemetry, not confirmed against production activity.

## MITRE ATT&CK
- **T1566 — Phishing:** background delivery technique in the Week 4 case; the synthetic network logs alone do not prove delivery.
- **T1204 — User Execution:** possible follow-up if endpoint telemetry confirms user interaction; not observed in these logs.
- **T1071.001 — Web Protocols:** candidate network behavior to investigate; URL access alone does not prove C2.

## Limitations and next steps
The dataset is small, controlled, and intentionally seeded. No real mail, endpoint, proxy, DNS, or SIEM evidence has been collected. IOC age, DNS caching, redirects, and shared infrastructure affect accuracy. Validate the real SPL execution and investigate hits with email and endpoint logs before deciding whether an incident occurred.

## Conclusion (B1 English)
I created a phishing threat hunting hypothesis and prepared safe test logs. I wrote Splunk searches to find suspicious domains, URLs, and related IP addresses. The test data shows how threat intelligence can help find systems for further investigation. Real Splunk results and screenshots are still needed to finish the practical task.

## Project files
- `README.md` — project report and methodology.
- `data/synthetic_phishing_logs.csv` — safe fictional logs.
- `queries/hunt.spl` — four SPL searches to run in Splunk.
- `scripts/validate.py` — reproducible offline checks.
- `evidence/RESULTS.md` — simulated results and analyst assessment.
- `evidence/offline_validation.txt` — saved offline output.

## Work attribution
Earlier OSINT/IOC and Kill Chain research: original student repository. New report, synthetic dataset, SPL queries, and offline validation: AI-assisted preparation. Splunk execution and screenshots: **not yet performed**.

## AI Usage Disclosure

**Tools used:** ChatGPT (OpenAI).

**My work:** I selected the topic *Phishing Threat Intelligence* and provided my existing GitHub research about phishing indicators, OSINT tools, and the Cyber Kill Chain. I chose to build a hypothesis-driven hunting scenario around phishing-related domains, URLs, and IP addresses.

**How I used AI:** I used ChatGPT to help organize this report in B1 English, formulate the hunting hypothesis, create a small synthetic dataset, draft four Splunk SPL queries, prepare a Python validation script, and explain the simulated findings and possible MITRE ATT&CK connections.

**Verification and limitations:** The results in this repository are based on synthetic data and offline checks. I did **not** run the queries in Splunk or ELK, and I do not present simulated findings as real SIEM results. The generated queries should be tested in Splunk before they are used with real security logs.
