# From ontology to knowledge graph

This note explains how the repository can evolve from a set of ontology files and examples into a running knowledge graph.

Stages
1. Authoritative ontology and shapes in repo (this project)
2. Ingest example and production data into a triplestore (Fuseki, Blazegraph, Virtuoso)
3. Run SPARQL CQ tests and SHACL validation on ingestion
4. Expose a SPARQL endpoint and build simple APIs/queries for consumers
5. Add provenance, versioning, and ETL to keep KG synchronized with sources

Operational tips
- Keep example data small and representative for CI tests.
- Log provenance (who/when/which source) for imported records.
- Consider a lightweight ETL that transforms CSV/JSON inputs into TTL using templates.
