# Modeling guidelines

Purpose: concise rules and trade-offs for building the ontology.

Principles (short):
- Model legal entities (Organization/Person) separately from roles (ManufacturerRole, ImporterRole).
- Prefer explicit reified records for registry objects (RegistrationRecord) and separate events for lifecycle actions.
- Keep jurisdiction-specific classes when legal semantics differ; introduce superclasses only when evidence supports them.

Trade-offs (for learners):
- Simplicity vs fidelity: Flattening (fewer classes/properties) is easier to implement but loses legal detail. Reification and more classes increase fidelity but raise implementation/testing costs.
- Labels vs IRIs: Relying on rdfs:label makes human-readable queries easier; relying only on URIs keeps canonical identifiers but needs client mapping.
- Strict validation vs flexibility: SHACL shapes enforce consistent data but can block legitimate jurisdictional variants; lighter validation accepts more data but may hide errors.

Practical tips
- Use clear namespaces and a small set of well-documented properties.
- Provide example instances that exercise features (status labels, role labels, evidence references).
- Keep CQ tests (SPARQL) alongside examples to guard against regressions.
