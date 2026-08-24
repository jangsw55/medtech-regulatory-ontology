# Architecture overview

Purpose: give a high-level picture of the repository components and how they interact.

Components
- research/: domain research, comparison, and design decisions
- ontology/: TTL/OWL source files (core, shapes, examples)
- examples/: sample RDF instances used for CQ testing and demos
- scripts/: helper scripts to run SPARQL queries and validations
- docs/: this folder — guidance, modeling rules, SPARQL examples, validation guide

Deployment / usage
- The ontology and examples are stored in the repo; consumers can load TTL files into an RDF graph (rdflib, Jena, RDF4J) for querying and validation.
- Use scripts/run_all_cqs.py to run competency-question checks against example data.

Notes
- Keep core ontology files small and modular (core, shapes, mapping) to ease reuse
- Prefer Turtle for source files; generate other serializations from source if needed
