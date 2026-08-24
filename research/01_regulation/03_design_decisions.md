# Registration Ontology — Design Decisions

## 1. Purpose

This document records the ontology design decisions for the Registration domain after source research, cross-jurisdiction comparison, and concept extraction. It explains what the ontology is modeling, how that modeling is being framed, and why the chosen boundaries are semantically preferable to alternatives.

The purpose is not to restate the regulation. It is to make explicit the domain semantics that are stable enough to become ontology classes, properties, and lifecycle patterns without collapsing jurisdictional differences.

The primary evidence base is:

- `README.md`
- `01_comparison.md`
- `02_concepts.md`
- `sources/01_FDA.md`
- `sources/02_MDR_IVDR.md`

The design decisions below are therefore traceable to research and comparison rather than derived from convenience or implementation preference.

These decisions should be read as working assumptions for ontology construction, not as final legal assertions. Where the evidence does not yet support a stable equivalence or a clean semantic boundary, the issue is intentionally left in the open-question set rather than forced into a premature mapping.

## 2. Design Principles

This design work follows the following principles:

- Research first, compare second, model third.
- Model the domain, not a specific company workflow.
- Prefer stable semantic meaning over software convenience.
- Preserve jurisdictional difference rather than forcing superficial equivalence.
- Avoid premature generalization; only introduce a superclass when a meaningful semantic distinction warrants it.
- Keep decisions minimal and evidence-based; unresolved questions remain explicit rather than silently resolved.

## 3. Design Decisions

### DD-001 — Model registration records and registration events as distinct but related concepts

**Status:** Accepted

**Decision**

Model registration-related objects as a persistent record entity and model the actions that create or modify that record as events, rather than treating `Registration` as a single undifferentiated class with a status property.

**Context**

The source research repeatedly distinguishes registry records from lifecycle events. FDA distinguishes establishment registration, device listing, and listing lifecycle changes. EU distinguishes actor registration, device registration, SRN issuance, and Basic UDI-DI assignment. The comparison explicitly warns that these are not all the same kind of object or event.

**Evidence**

- `02_concepts.md`: Concept 10 (RegistrationRecord), Concept 18 (DeviceListing vs DeviceRegistrationRecord), Concept 19 (Reified lifecycle events)
- `01_comparison.md`: sections on Establishment vs Economic Operator, Registration vs Listing, and structural differences in lifecycle handling
- `sources/01_FDA.md`: Part 807 establishment registration, device listing, lifecycle updates; 21 CFR Part 830 UDI system and GUDID
- `sources/02_MDR_IVDR.md`: Device registration, SRN issuance, Basic UDI-DI assignment, EUDAMED, Events E01–E13

**Alternatives considered**

- Alternative A — One class named `Registration` encompassing both record and event semantics
- Alternative B — Flatten all registration details into device or organization properties
- Alternative C — Model only event instances and omit persistent records

**Rationale**

A single `Registration` class would collapse distinct semantics: an actor registration record has different legal and provenance meaning from a submission or verification event, and a device listing record is not the same thing as the event that created it. The ontology requires both the persistent entity and the temporal act that produced it. This distinction is important for provenance, lifecycle traceability, and SHACL or graph queries that need to answer “what was entered,” “when,” and “by whom,” without conflating the record with the act of creation.

**Ontology impact**

- Introduce persistent record classes such as `EstablishmentRegistrationRecord`, `DeviceRegistrationRecord`, and `DeviceListingRecord` as separate from event classes such as `EstablishmentRegistration`, `BasicUDIDIAssignment`, and `SRNIssuance`
- Represent lifecycle transitions with event classes connected to a target record via object properties such as `createdRecord`, `updatedRecord`, `verifiedBy`, and `referencesRecord`
- Use temporal properties on events rather than compressing dates into a single record object

**Jurisdictional consideration**

FDA and EU both have registry-like objects, but the object and event boundaries differ: FDA keeps registration and listing separate, while EU separates actor registration (SRN) from device registration and Basic UDI-DI assignment. The ontology should retain these jurisdiction-specific patterns rather than forcing a single universal registration model.

**Open issue**

Whether a future higher-level class such as `RegulatoryRecord` or `MarketRegistrationRecord` is worth introducing remains a design choice, but it should be added only if it adds semantic clarity without obscuring the jurisdiction-specific distinctions already present in the evidence.

---

### DD-002 — Treat manufacturer, importer, distributor, and similar regulatory actors as role-bearing concepts associated with organizations rather than as organization subclasses

**Status:** Accepted

**Decision**

Model regulatory actors as role-bearing concepts, with `Organization` and `Person` as the primary legal entities, and role classes such as `Manufacturer`, `Importer`, and `Distributor` as roles or relationship types rather than as direct subclasses of the organization itself.

**Context**

The concept inventory explicitly raises the question whether a concept should be modeled as `OrganizationRole` vs `Organization` subclass. The research shows the same organization can play different regulatory roles depending on context and legal obligations. This is especially visible in the FDA distinction between establishment and manufacturer, and in the EU explicit role semantics for manufacturer, importer, distributor, and authorised representative.

**Evidence**

- `02_concepts.md`: Concept 2 (Manufacturer), Concept 5 (Importer and InitialImporter), Concept 6 (Distributor), Concept 7 (Authorised Representative), unresolved question on `OrganizationRole` vs `Organization` subclass
- `01_comparison.md`: Manufacturer and Establishment are compared as related but not equivalent; Importer is category 1 common concept, but the FDA-specific `InitialImporter` is noted as a sub-role
- `sources/01_FDA.md`: actor model and establishment/owner/operator responsibilities; Part 807 registration and listing distinctions
- `sources/02_MDR_IVDR.md`: manufacturing, economic operator, distributor, and authorised representative roles under MDR/IVDR

**Alternatives considered**

- Alternative A — Create a subclass hierarchy where each actor is a type of `Organization`
- Alternative B — Model actors only as literal role strings on an organization
- Alternative C — Use organization + role as a reified relationship class

**Rationale**

The legal evidence supports a distinction between the organizational entity and the regulatory role it bears. The same organization can be a manufacturer in one context, an importer in another, or an authorised representative in a third. Representing role as a first-class concept supports provenance, multiple-role assignment, and jurisdictional variation without misclassifying the organization itself.

**Ontology impact**

- Maintain `Organization` and `Person` as core legal entities
- Model roles such as `ManufacturerRole`, `ImporterRole`, `DistributorRole`, and `AuthorisedRepresentativeRole` as role classes or restricted relationship classes
- Define properties such as `hasRole` or `playsRoleIn` with domain `Organization` and range `RegulatoryRole`
- Preserve role-specific obligations and provenance where needed

**Jurisdictional consideration**

The FDA framework emphasizes establishment ownership and device activity while the EU framework strongly names legal actors and economic operator roles. A role-based model accommodates both: the organization remains the legal actor, while the meaning of the role is jurisdiction-specific and attached to the legal and regulatory context.

**Open issue**

The ontology should not prematurely create a universal super-role such as `EconomicOperator` across all jurisdictions unless evidence later supports a sufficiently stable shared meaning. For now, role modeling should remain explicit and jurisdiction-aware.

---

### DD-003 — Keep `Establishment`, `EconomicOperator`, and `SRN` as distinct concepts rather than collapsing FDA and EU registrants into one class

**Status:** Accepted

**Decision**

Do not merge FDA `Establishment` with EU `EconomicOperator` or EU `SRN` into a single class. Model them as separate but related concepts, with a common higher-level abstraction only if justified by future evidence.

**Context**

The comparison is explicit: the FDA establishment concept is a place-of-business registration object and the EU economic operator concept is a role-based actor construct tied to SRN issuance. The two are not semantically equivalent, even though both are regulatory registration objects.

**Evidence**

- `01_comparison.md`: Category 2 result for Establishment vs Economic Operator / SRN
- `02_concepts.md`: Concept 3 (Establishment), Concept 4 (EconomicOperator / SRN)
- `sources/01_FDA.md`: establishment definition, registration, device listing, ownership/operations
- `sources/02_MDR_IVDR.md`: economic operator, actor registration, SRN issuance, competent-authority verification

**Alternatives considered**

- Alternative A — Treat `Establishment` and `EconomicOperator` as equivalent objects
- Alternative B — Reduce both to a generic `RegulatoryEntity`
- Alternative C — Represent only the shared registration number without a concept-level distinction

**Rationale**

The research shows the same underlying domain problem is represented differently in the two jurisdictions. FDA treats an establishment as a physical/business location tied to a registration number and device listing. EU treats an economic operator as a legal actor under a registration flow that includes verification and SRN issuance. These are related regulatory objects but not equivalent in scope, lifecycle, or actor semantics.

**Ontology impact**

- Keep FDA-specific `Establishment` and EU-specific `EconomicOperator` classes separate
- Model `SRN` as an identifier entity associated with the EU actor-registration process rather than as a literal-only string on an organization
- Keep object properties such as `hasEstablishmentRegistration`, `hasSRN`, and `hasEconomicOperatorRegistration` jurisdiction-specific unless a cross-jurisdiction abstraction is later justified

**Jurisdictional consideration**

This is a direct example of the cross-jurisdiction generalization rule: the concepts are related, but not equivalent. The ontology should capture both and the relationship between them, while preserving their respective legal and operational roles.

**Open issue**

The eventual need for a common abstraction, such as a generic `RegisteredActor` or `RegulatoryRegistrant`, should be revisited only after more evidence confirms a stable semantic boundary. At the current stage, separate concepts are preferable.

---

### DD-004 — Model identifier concepts as first-class entities with issuer, scope, and target semantics, not as bare strings on a device or organization

**Status:** Accepted

**Decision**

Represent regulatory identifiers such as UDI, Device Identifier, Basic UDI-DI, SRN, listing number, and submission identifier as first-class identifier entities or at minimum as semantically typed identifier properties, rather than as unstructured literal attributes.

**Context**

The research repeatedly distinguishes identifier systems with different scopes, issuers, and regulatory meaning. The source files and comparison stress that a device identifier is not merely a database field, but a regulatory object with assignment rules, lifecycle, and provenance.

**Evidence**

- `02_concepts.md`: Concept 14 (Device Identification), Concept 15 (Basic UDI-DI), Concept 16 (Classification systems), Concept 18 (DeviceListing vs DeviceRegistrationRecord)
- `01_comparison.md`: identifier comparison categories and unresolved products such as Product Code vs EMDN and listing number vs EU registration ID
- `sources/01_FDA.md`: UDI, DI, PI, device listing numbers, product codes, GUDID, premarket submission numbers
- `sources/02_MDR_IVDR.md`: UDI, Basic UDI-DI, SRN, EUDAMED, device and actor registration identifiers

**Alternatives considered**

- Alternative A — Store identifiers as datatype properties on `Device` or `Organization`
- Alternative B — Represent only the literal value and omit semantic type or issuer
- Alternative C — Create a generic `Identifier` class without differentiating identifier semantics

**Rationale**

Different identifiers carry different regulatory meaning, assignment authorities, and lifecycle obligations. A device’s UDI is not the same as a product code, which is not the same as a listing number or SRN. A first-class representation supports reasoning, provenance, validation, and future SHACL constraints without collapsing legal semantics into a flat string field.

**Ontology impact**

- Introduce identifier classes such as `DeviceIdentifier`, `ProductionIdentifier`, `BasicUDIDI`, `SRN`, `ListingNumber`, `SubmissionIdentifier`, and `RegulatoryAuthorityAssignedIdentifier`
- Add generic properties such as `hasIdentifier`, `issuedBy`, `identifiesEntity`, `hasIdentifierType`, `hasIdentifierScope`, and `hasIssueDate`
- Use identifier entities to preserve provenance and lifecycle changes rather than overwriting the original value

**Jurisdictional consideration**

The FDA and EU have closely related identifier systems, but they are not equivalent: Basic UDI-DI is an EU-specific grouping identifier, while Product Code is FDA-specific classification/reference data. The ontology should preserve these as separate identifier families and record relationships only where the evidence supports them.

**Open issue**

The mapping between FDA Product Code and EU EMDN or between FDA listing numbers and EU device registration identifiers remains unresolved; explicit evidence is insufficient for direct equivalence.

---

### DD-005 — Model submission and decision artifacts as reified regulatory processes, not as direct attributes on a device or organization

**Status:** Accepted

**Decision**

Represent regulatory submissions and decisions as first-class process or event objects with provenance, target object, actor, and outcome, rather than encoding them as simple status attributes or labels on the regulated device.

**Context**

The concept analysis treats submission and decision as separate, reified objects. This is necessary because the same device may have multiple submissions, review outcomes, and different decision types over time. FDA and EU both differentiate the process of applying for a regulatory action from the decision or certificate that results from it.

**Evidence**

- `02_concepts.md`: Concept 11 (RegulatorySubmission), Concept 12 (RegulatoryDecision), Concept 13 (Certificate), Concept 19 (Reified lifecycle events)
- `01_comparison.md`: discussion of FDA submission-based pathways versus EU conformity-assessment and certificate model
- `sources/01_FDA.md`: 510(k), PMA, De Novo, HDE, IDE, approval, clearance, denial, withdrawal
- `sources/02_MDR_IVDR.md`: conformity assessment, notified-body certificate, CE marking, SRN issuance, device-registration prerequisites

**Alternatives considered**

- Alternative A — Model submission and decision as annotation properties on a device
- Alternative B — Collapse decision to a completed boolean or status enumeration
- Alternative C — Model only the final certificate or approval artifact and ignore the pathway that created it

**Rationale**

A regulatory decision is not just a label; it is a temporally anchored event with actor, evidence, target device or device family, and provenance. Without reification, the ontology loses the distinction between an application, a review, and an outcome; it also loses the ability to query how a device reached a given status, who issued the decision, and what evidence accompanied it.

**Ontology impact**

- Introduce classes such as `RegulatorySubmission`, `RegulatoryDecision`, `ConformityAssessment`, and `Certificate`
- Require properties such as `submittedBy`, `issuedBy`, `referencesDevice`, `hasOutcome`, `hasDecisionDate`, and `hasStatus`
- Maintain a temporal event chain rather than flattening everything into a single current state

**Jurisdictional consideration**

FDA emphasizes submission-driven agency decisions (510(k), PMA, De Novo), whereas EU emphasizes conformity assessment, notified-body certificates, and CE marking. This strengthens the case for reified decision objects while preserving both legal forms.

**Open issue**

Whether a future shared super-class such as `RegulatoryAuthorizationArtifact` is useful depends on whether the decision semantics remain sufficiently aligned across jurisdictions. Until then, jurisdiction-specific decision families should remain explicit.

---

### DD-006 — Preserve jurisdiction-specific legal concepts where the evidence shows different semantics, even when the vocabulary appears functionally similar

**Status:** Accepted

**Decision**

Retain jurisdiction-specific concepts such as `Establishment`, `EconomicOperator`, `SRN`, `NotifiedBody`, `BasicUDIDI`, and `ProductCode` as distinct ontology concepts, even when they serve overlapping regulatory purposes.

**Context**

The main cross-jurisdiction modeling risk is over-generalizing similar concepts across FDA and EU law. The comparison clearly distinguishes direct common concepts from related-but-non-equivalent concepts and from jurisdiction-specific concepts.

**Evidence**

- `01_comparison.md`: categories 2, 3, and 4; explicit identification of jurisdiction-specific concepts and unresolved mappings
- `02_concepts.md`: Concept 3 (Establishment), Concept 4 (EconomicOperator / SRN), Concept 8 (Notified Body), Concept 15 (Basic UDI-DI), Concept 16 (Product Code / EMDN), Concept 17 (GUDID / EUDAMED)
- `sources/01_FDA.md`: establishment registration, product code, GUDID, classification, user-facing FDA-specific systems
- `sources/02_MDR_IVDR.md`: Economic Operator, SRN, Authorised Representative, Notified Body, EUDAMED, Basic UDI-DI

**Alternatives considered**

- Alternative A — Collapse all similar registration concepts into one generic `Registration` or `RegistryEntry`
- Alternative B — Use a single `Authority` class regardless of source and legal role
- Alternative C — Reduce each jurisdiction-specific concept to mere terminology differences rather than distinct semantics

**Rationale**

The evidence shows that similar-looking concepts have different legal meaning, issuer, lifecycle, and purpose. For example, FDA `ProductCode` and EU `EMDN` are both classification systems but are not semantically interchangeable; the EU `SRN` is not just a renamed FDA establishment number. Preserving these distinctions avoids false equivalence and supports robust cross-jurisdiction querying.

**Ontology impact**

- Keep separate classes for jurisdiction-specific legal constructs
- Use cross-jurisdiction link properties only when evidence supports a relationship; do not force symmetry
- Allow the ontology to represent common concepts and divergence simultaneously, rather than one flattened legal model

**Jurisdictional consideration**

This is a direct application of the project’s explicit cross-jurisdiction generalization rule: commonality is allowed where semantics are equivalent, but related or jurisdiction-specific concepts must remain separate.

**Open issue**

The exact mapping between FDA classification codes and EU nomenclature codes remains under-specified, and should remain an unresolved question unless external evidence is added.

---

### DD-007 — Distinguish `Market`, `Country`, and `Jurisdiction` as separate semantic contexts when the evidence supports it

**Status:** Proposed

**Decision**

Model market and country as distinct semantic contexts unless evidence demonstrates that they are coextensive in a specific regulatory relationship. The ontology should not assume a geographic country is equivalent to a regulatory market or a jurisdictional authority context.

**Context**

The research repeatedly handles registration, device listing, approval pathways, and actor roles in a way that is jurisdiction-bound but not identical to geography. An FDA or EU market context is different from a physical location or a country boundary, even when both are associated with the same device or actor.

**Evidence**

- `README.md`: project roadmap and cross-jurisdiction design objectives; explicit differentiation of market and country is a design concern for the domain
- `01_comparison.md`: discussion of authority context, registration, and lifecycle semantics across jurisdictions
- `02_concepts.md`: actor and registration concepts are tied to jurisdictional authority and market access pathways
- `sources/01_FDA.md` and `sources/02_MDR_IVDR.md`: jurisdictional authorities, locations, and regulator-specific requirements

**Alternatives considered**

- Alternative A — Treat `Country` and `Market` as the same class
- Alternative B — Use only a country value without an explicit regulatory jurisdiction entity
- Alternative C — Model market access as a property on a device without a distinct jurisdiction concept

**Rationale**

A device may be subject to market access rules in one jurisdiction and distribution or presence in another. A country is a geographic or legal administrative unit; a market is a regulatory and commercial context. Reusing a single concept would blur semantics and reduce the ontology’s utility for jurisdiction-aware and provenance-aware reasoning.

**Ontology impact**

- Introduce `Jurisdiction` or `RegulatoryJurisdiction` as a distinct concept when needed
- Keep `Country` as a geographic or geopolitical entity
- Use `Market` or `MarketContext` only where the evidence indicates a distinct regulatory commerce context

**Jurisdictional consideration**

The FDA and EU frameworks have different regulatory authority structures and legal obligations. A jurisdictional model that separates geography from market context allows both to be represented without forcing one into the other.

**Open issue**

The current research does not yet provide a final, exhaustive rule for which concepts should be modeled as Country, Market, or Jurisdiction. This should remain a minimal but explicit design decision rather than a fully resolved ontology model.

---

## 4. Cross-Jurisdiction Modeling Principles

The following principles are required for future implementation work in the Registration domain:

- Shared concepts must be supported only where the evidence supports actual semantic equivalence.
- Related concepts remain separate and linked rather than flattened into the same class.
- Jurisdiction-specific concepts should remain explicit and not be silently removed to improve symmetry.
- Event semantics and record semantics should stay distinct.
- Identifier semantics should remain typed and provenance-aware.
- Common legal patterns, such as `submit → review → decision`, are not automatically equivalent across jurisdictions without checking the regulatory structure.

## 5. Modeling Conventions

The following conventions are adopted for the first iteration of the Registration ontology:

- Class names use singular, domain-meaningful nouns.
- Event classes follow an action or lifecycle pattern where the action creates or changes a regulatory object.
- Identifier classes are modeled as entities when their legal meaning is functionally independent of the object they identify.
- Role concepts stay distinct from the legal organization or person acting in that role.
- Jurisdiction-specific families of concepts are retained as explicit modules rather than merged into a single generic layer prematurely.
- Provenance is captured at the event and identifier level, not only on the resulting record.

## 6. Deferred Decisions / Open Modeling Questions

The following issues remain intentionally unresolved because the current evidence base is insufficient or because they require a future modeling tradeoff:

1. Product Code ↔ EMDN mapping
   - Evidence status: insufficient
   - The research indicates both are classification systems but does not establish a direct semantic mapping or equivalence rule.

2. FDA listing number ↔ EU device registration identifier mapping
   - Evidence status: insufficient
   - The source files show similar device-record functions but not the same legal scope or lifecycle.

3. Universal `RegulatoryRecord` or `RegulatoryAuthorization` abstraction
   - Evidence status: partial
   - The evidence supports jurisdiction-specific structures; a unified abstraction is possible but not yet required.

4. Exact object-property and cardinality constraints for relationship reification
   - Evidence status: partial
   - The concept analysis supports reification, but cardinality rules require implementation-level validation work.

5. Country vs market vs regulatory jurisdiction semantics
   - Evidence status: partial
   - The current evidence supports separation at a conceptual level but not full normative specification.

## Final Design Decision Summary

| ID | Decision | Status | Main Concepts Affected | Evidence Status |
| --- | --- | --- | --- | --- |
| DD-001 | Distinguish registration records from registration events | Accepted | RegistrationRecord, RegistrationEvent, DeviceListing, SRN issuance | Strong |
| DD-002 | Model manufacturer/importer/distributor as role-bearing concepts | Accepted | Manufacturer, Importer, Distributor, OrganizationRole | Strong |
| DD-003 | Keep Establishment and EconomicOperator/SRN separate | Accepted | Establishment, EconomicOperator, SRN | Strong |
| DD-004 | Model identifiers as first-class regulatory entities | Accepted | UDI, DI, PI, Basic UDI-DI, SRN, ListingNumber | Strong |
| DD-005 | Reify submission and decision objects | Accepted | RegulatorySubmission, RegulatoryDecision, Certificate | Strong |
| DD-006 | Preserve jurisdiction-specific legal concepts | Accepted | ProductCode, EMDN, NotifiedBody, Basic UDI-DI, SRN | Strong |
| DD-007 | Distinguish Country, Market, and Jurisdiction contexts | Proposed | Country, Market, Jurisdiction | Moderate |

This record intentionally remains at the ontology-design layer, not the OWL implementation layer. It is meant to explain the semantic structure of the Registration domain and the reasons those choices were made before implementation begins.

## CQ run findings (2026-08-24)

- Action: Executed registration_competency_questions.sparql against ontology/registration/example_registration.ttl to validate competency-question coverage.
- Findings:
  - CQ1 (devices and jurisdictions): OK — devices with jurisdictions returned.
  - CQ2 (device registration numbers): OK — registrationNumber values present.
  - CQ3 (current registration status): EMPTY — queries expected a status rdfs:label (statusLabel) but status resources in the example data had no rdfs:label values.
  - CQ4 (organizations and roles): OK — organizations and role URIs returned.
  - CQ5 (submissions and decisions): PARTIAL — decisions returned but decisionStatus label was missing (no rdfs:label on the status resources).
  - CQ6 (evidence supporting submissions): OK — evidence documentReference values present.
- Decision / Fix applied: Added rdfs:label annotations to example data for status resources and role examples to make CQ3 and CQ5 return human-readable labels. See ontology/registration/example_registration.ttl (added reg:Approved and reg:Pending labels; added rdfs:label for ManufacturerRole1 and ImporterRole1).
- Ontology impact: Example data now includes labels for status and role resources. Consider whether the ontology should require rdfs:label on status classes or whether queries should dereference status URIs to a standardized label property. Also consider adding SHACL/tests to ensure example data exposes expected label properties.
- Next steps: Re-run the CQ suite after changes, add unit/test harness for CQ checks, and propagate any necessary schema-level documentation so implementers know which label properties are expected in example data.

