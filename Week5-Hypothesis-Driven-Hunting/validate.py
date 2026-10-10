import csv
from pathlib import Path
rows=list(csv.DictReader((Path(__file__).resolve().parents[1]/'data/synthetic_phishing_logs.csv').open()))
dns=[r for r in rows if r['event_type']=='dns' and r['domain']=='login-outlook365.yzz.me']
url=[r for r in rows if r['event_type']=='proxy' and r['url']=='http://login-outlook365.yzz.me/']
ip=[r for r in rows if r['event_type']=='firewall' and r['dest_ip']=='77.72.1.44']
from collections import defaultdict
matches=defaultdict(set)
for r in dns: matches[r['host']].add('domain')
for r in url: matches[r['host']].add('url')
for r in ip: matches[r['host']].add('context_ip')
correlated={h:sorted(s) for h,s in matches.items() if len(s)>=2}
result={'total_events':len(rows),'dns_matches':len(dns),'url_matches':len(url),'context_ip_matches':len(ip),'correlated_hosts':correlated,'note':'Offline Python validation of synthetic data; not a Splunk execution.'}
print(result)
assert (len(rows),len(dns),len(url),len(ip),len(correlated))==(8,2,1,2,1)
