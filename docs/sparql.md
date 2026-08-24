# SPARQL: writing and running queries

This file explains common SPARQL patterns used in the project and how to run queries locally.

Common patterns
- Listing triples: SELECT ?s ?p ?o WHERE { ?s ?p ?o }
- Devices with properties: use PREFIX reg: <...> and query by rdf:type reg:Device
- OPTIONAL for non-mandatory properties
- Use FILTER and BIND for simple transformations (dates, local-name extraction)

Running queries
- Python + rdflib: scripts/run_all_cqs.py demonstrates running multiple queries against TTL files.
- Apache Jena ARQ: `arq --data example_registration.ttl --query myquery.rq`
- RDF4J Workbench or Fuseki as a SPARQL endpoint for interactive querying

Tips
- Keep queries small and name them (comment header like # CQ1) for automated runners.
- When expecting human-readable labels, query for rdfs:label as a fallback.
- Test queries against minimal example data first, then the full dataset.
