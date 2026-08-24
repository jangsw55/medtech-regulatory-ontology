import sys
import subprocess

try:
    from rdflib import Graph, Namespace
except Exception:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "rdflib"]) 
    from rdflib import Graph, Namespace

from rdflib.namespace import RDFS

if len(sys.argv) < 2:
    print("Usage: python run_devices_query.py <path-to-ttl>")
    sys.exit(1)

ttl_path = sys.argv[1]

reg = Namespace('https://example.org/medtech-regulatory-ontology/registration#')

g = Graph()
try:
    g.parse(ttl_path, format='turtle')
except Exception as e:
    print(f"Error parsing TTL: {e}")
    sys.exit(2)

q = '''PREFIX reg: <https://example.org/medtech-regulatory-ontology/registration#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?device ?deviceName ?jurLabel ?status WHERE {
  ?device a reg:Device .
  OPTIONAL { ?device reg:deviceName ?deviceName }
  OPTIONAL { ?device reg:hasJurisdiction ?jur . ?jur rdfs:label ?jurLabel }
  OPTIONAL { ?device reg:hasRegistrationRecord ?reg . ?reg reg:hasStatus ?status }
}
'''

res = g.query(q)

print('device\tdeviceName\tjurisdiction\tstatus')
for row in res:
    device = row[0] or ''
    name = row[1] or ''
    jur = row[2] or ''
    status = row[3] or ''
    # simplify status to local name if it's a URI
    s = str(status)
    if '#' in s:
        s = s.split('#')[-1]
    print(f"{device}\t{name}\t{jur}\t{s}")
