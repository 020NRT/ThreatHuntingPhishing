# Simulated Hunting Results (Offline Validation)

**Data source:** `data/synthetic_phishing_logs.csv` (8 fictional events).
**Method:** Python CSV analysis via `scripts/validate.py`.
**Splunk execution:** Not performed. These are expected SPL outcomes, not Splunk screenshots.

| Hunt | Count | Hosts | Meaning |
|---|---:|---|---|
| DNS domain IOC | 2 | PC-01, PC-04 | Domain query in test logs |
| Proxy URL IOC | 1 | PC-01 | URL access in test logs |
| Related IP context | 2 | PC-01, PC-03 | Network events; IP alone is not proof |
| Multi-indicator correlation | 1 host | PC-01 | DNS + proxy + firewall test events |

## Analyst assessment
- **PC-01:** highest-priority test host because three indicators co-occur.
- **PC-04:** domain-only match; investigate DNS context.
- **PC-03:** IP-only match; low confidence without more evidence.
- **PC-02 and PC-05:** no IOC matches.

## Reproduce
Run `python scripts/validate.py` from the project root. For actual Splunk evidence, import the CSV and execute the searches in `queries/hunt.spl`.
