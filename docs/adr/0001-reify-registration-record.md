# ADR 0001 — Reify registration record vs event

Status: accepted

Context
- Research showed that registry records and lifecycle events have different legal and provenance semantics.

Decision
- Model `RegistrationRecord` as a persistent entity and `RegistrationEvent` as the temporal action that created/modified the record. Use properties `createdRecord` / `updatedRecord` to link events to records.

Consequences
- Pros: better provenance, clearer lifetime semantics, easier to represent jurisdictional differences.
- Cons: more classes and complexity in data and queries; requires example data and tests to prevent confusion.
