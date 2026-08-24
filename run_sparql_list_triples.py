import sys
import subprocess

try:
    from rdflib import Graph
except Exception:
    # Install rdflib if missing
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdflib"]) 
    from rdflib import Graph

if len(sys.argv) < 2:
    print("Usage: python run_sparql_list_triples.py <path-to-ttl>")
    sys.exit(1)

ttl_path = sys.argv[1]

g = Graph()
try:
    g.parse(ttl_path, format='turtle')
except Exception as e:
    print(f"Error parsing TTL: {e}")
    sys.exit(2)

q = "SELECT ?s ?p ?o WHERE { ?s ?p ?o }"
res = g.query(q)

# Print headers
print("subject\tpredicate\tobject")
for row in res:
    s, p, o = row
    print(f"{s}\t{p}\t{o}")
