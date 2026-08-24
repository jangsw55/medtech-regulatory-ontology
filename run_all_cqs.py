import sys
import subprocess

try:
    from rdflib import Graph
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdflib"]) 
    from rdflib import Graph

import re

if len(sys.argv) < 2:
    print("Usage: python run_all_cqs.py <path-to-ttl> [path-to-sparql-file]")
    sys.exit(1)

ttl_path = sys.argv[1]
sparql_path = sys.argv[2] if len(sys.argv) > 2 else 'ontology/registration/registration_competency_questions.sparql'

# load graph
g = Graph()
try:
    g.parse(ttl_path, format='turtle')
except Exception as e:
    print(f"Error parsing TTL: {e}")
    sys.exit(2)

with open(sparql_path, 'r', encoding='utf-8') as f:
    content = f.read()

# split queries on lines that start with # CQ
parts = re.split(r"(?m)^#\s*CQ", content)
# first part is prefix area possibly
prefix = parts[0]
queries = []
for p in parts[1:]:
    # restore the CQ header number if present
    header_and_query = p.strip()
    # find the first newline, header is up to that
    m = re.match(r"(.*?)(\n+)([\s\S]*)", header_and_query)
    if m:
        # header like '1: devices and jurisdictions\nSELECT ...'
        header = m.group(1).strip()
        query = prefix + "\n# CQ" + header + "\n" + m.group(3)
        queries.append((header, query))

report = []
for header, q in queries:
    print(f"--- Running CQ{header.strip()} ---")
    try:
        res = g.query(q)
    except Exception as e:
        print(f"Query error for CQ{header}: {e}")
        report.append((header, 'error', str(e)))
        continue
    rows = list(res)
    varnames = [str(v) for v in res.vars]
    print(f"Variables: {varnames}")
    print(f"Rows: {len(rows)}")
    # print up to 10 rows
    for r in rows[:10]:
        vals = [str(x) if x is not None else '' for x in r]
        print('\t'.join(vals))
    if len(rows) == 0:
        report.append((header, 'empty', varnames))
    else:
        # check for requested label vars such as statusLabel or decisionStatus
        missing_label_vars = []
        for label_var in ['statusLabel','decisionStatus','jurLabel']:
            if label_var in varnames:
                # check if any row has a bound value for that var
                idx = varnames.index(label_var)
                if all((r[idx] is None) for r in rows):
                    missing_label_vars.append(label_var)
        if missing_label_vars:
            report.append((header, 'partial_labels_missing', missing_label_vars))
        else:
            report.append((header, 'ok', None))

print('\n=== SUMMARY REPORT ===')
for item in report:
    print(item)

# write a report file
with open('cq_run_report.txt','w',encoding='utf-8') as out:
    out.write('CQ run report\n\n')
    for item in report:
        out.write(str(item) + '\n')

print('\nReport written to cq_run_report.txt')
