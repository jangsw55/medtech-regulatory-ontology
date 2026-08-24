# Open Questions

## Overview

This document records the open questions that remain after the comparative analysis of regulatory registration concepts across the FDA and MDR/IVDR frameworks. It is not intended to assert a single universal answer; rather, it highlights where the evidence base is still incomplete, where concepts overlap but are not equivalent, and where additional research or source validation is needed before a final ontology or mapping can be stabilized.

The comparison shows that several concepts are sufficiently clear to support cross-jurisdiction modeling, but other areas remain ambiguous because the legal, operational, and administrative meanings differ across jurisdictions. In particular, the source research suggests that there is a difference between a regulatory record, a legal actor, a lifecycle event, and a market-access decision. These layers are not always distinguished consistently in the source materials, which means some questions remain open even when the general patterns are visible.

The sections below identify the main unresolved issues in a structured manner. Each item follows a research-oriented pattern: the question is stated, the importance is explained, the evidence gap is described, and a follow-up route is suggested.

---

## Cross-jurisdiction regulatory gaps

### 1. Are FDA “registration” and EU “device registration” semantically equivalent functions?

- Question: Are the FDA establishment-registration and device-listing processes equivalent to the EU device-registration and actor-registration flows?
- Why it matters: This is a central modeling issue. If the underlying legal objects differ, then a cross-jurisdiction ontology should not collapse them into one class without losing essential meaning.
- Current uncertainty: The FDA system is organized around establishment registration, device listing, and market-access pathways such as 510(k), PMA, and De Novo. The EU system separates economic-operator registration, SRN issuance, device registration, and Basic UDI-DI assignment. These are related but not obviously identical in legal function.
- Evidence or data needed: A side-by-side mapping of the object being registered, the authority issuing the record, the lifecycle events, the required evidence, and the legal effect of each record. This should distinguish record, actor, assignment, and decision.
- Suggested follow-up: Build a comparative matrix that separates (a) actor registration, (b) device registry record, (c) identifier assignment, and (d) authorization decision. This would clarify whether the common abstraction is a regulatory record or a broader market-access event.

### 2. Is there a stable shared concept for “regulatory actor” across FDA and EU?

- Question: Can a single concept such as “RegulatoryActor” reliably cover manufacturer, importer, distributor, authorised representative, and establishment owner across both frameworks?
- Why it matters: A cross-jurisdiction ontology needs a stable way to represent who is legally responsible for a device without flattening distinct legal roles into a single category.
- Current uncertainty: FDA uses establishment, owner/operator, and manufacturer-related responsibilities, while the EU explicitly distinguishes manufacturer, authorised representative, importer, distributor, and economic operator. The same organization may hold multiple roles, but the role structure differs between jurisdictions.
- Evidence or data needed: Jurisdiction-specific role tables showing legal obligations, who can act on behalf of a manufacturer, which actors must be registered, and which actors are tied to a physical site versus a legal entity.
- Suggested follow-up: Model actor, role, and site as separate but linked concepts before defining any higher-level abstraction. This prevents premature generalization.

### 3. Is a single “market authorization” concept feasible across the FDA and EU models?

- Question: Can FDA clearance/approval and EU CE marking/conformity assessment be represented under one common concept without distortions?
- Why it matters: These are often treated as analogous outcomes in practical discussions, but their legal form and procedural origin differ.
- Current uncertainty: FDA decisions are submission-based and authority-issued. EU processes are structured around conformity assessment, notified-body certificates, declaration of conformity, and CE marking. The legal artifact used to demonstrate compliance is not identical.
- Evidence or data needed: Comparative process maps showing the sequence of submissions, evaluations, certificates, declarations, and placement-on-market events for representative device classes in each jurisdiction.
- Suggested follow-up: Keep “authorization” as a higher-level concept only if it is clearly abstracted from the underlying process; otherwise maintain separate jurisdiction-specific decision classes.

---

## Classification and scope ambiguities

### 4. How should classification and scope distinctions be handled across jurisdictions?

- Question: When is a product considered a device, accessory, combination product, or regulated product under each regime, and how should those distinctions be represented in a shared ontology?
- Why it matters: Classification affects registration, evidence requirements, labeling obligations, and lifecycle obligations. A product that is a device in one jurisdiction may fall under a different regulatory category in another.
- Current uncertainty: The source research identifies differences in the way regulatory objects are assigned and how classification criteria are applied. The boundaries between core device, accessories, and combination products remain difficult to generalize without additional evidence.
- Evidence or data needed: Device-classification rules, triggers for classification review, rules for combination products, and the crosswalk between device category and registration obligations.
- Suggested follow-up: Add a classification layer that separates product-type classification from the registration record itself, so that jurisdictional differences are preserved without confusing them with the actual device identity.

### 5. Are FDA Product Code and EU EMDN or equivalent classification codes directly comparable?

- Question: Is there a reliable one-to-one or many-to-one mapping between FDA Product Code and EU classification identifiers?
- Why it matters: Classification codes often influence product categorization, premarket pathways, and registry logic. Direct equivalence would simplify cross-jurisdiction comparison, but the evidence base may not support this.
- Current uncertainty: The source comparison notes that these systems are similar in function but likely not equivalent in scope, issuer, and operational meaning. This remains unresolved.
- Evidence or data needed: Code definition documents, assignment logic, and examples of products mapped across both systems.
- Suggested follow-up: Treat these as related but not equivalent until a stronger evidence base is established; in the ontology they should remain separate identifier or classification concepts.

### 6. Are “listing number,” “registration number,” and “device identifier” distinct enough to justify separate ontology classes?

- Question: Do FDA listing numbers, EU registration identifiers, and device identifiers represent the same semantic type, or do they belong to distinct subclasses of regulatory identifier?
- Why it matters: These numbers often appear together in operational systems, but they are assigned for different purposes and can have different lifecycle rules.
- Current uncertainty: The research suggests that registration numbers, listing numbers, and device identifiers share a broad family resemblance but differ in issuer, target object, and legal effect.
- Evidence or data needed: Institutionally defined descriptions of each identifier’s purpose, source, lifecycle, and relationship to the device, actor, or record it identifies.
- Suggested follow-up: Maintain a general identifier hierarchy with subclasses rather than flattening all numbers into a single generic “ID” category.

---

## Evidence and documentation gaps

### 7. What evidence is required to assert equivalence or non-equivalence between regulatory records?

- Question: Which evidence points are sufficient to claim that two records across jurisdictions are equivalent, related, or different?
- Why it matters: Without clear evidence criteria, cross-jurisdiction mappings can be over-stated or under-specified.
- Current uncertainty: The source research is careful to distinguish category types, but it does not yet define a formal evidentiary threshold for when a semantic mapping becomes acceptable.
- Evidence or data needed: A template for each mapping that records object purpose, regulatory authority, legal effect, lifecycle, actor, and provenance; then any mapping claim should be evaluated against this template.
- Suggested follow-up: Define a mapping rubric for the ontology project: direct equivalence, related-but-not-equivalent, jurisdiction-specific, and unresolved.

### 8. Which documentation burdens are genuinely comparable across jurisdictions?

- Question: Do premarket, registration, and post-market documentation requirements create equivalent compliance burdens across FDA and EU pathways for the same device type?
- Why it matters: Documentation practices influence not only compliance cost but also the quality and form of the underlying data captured by a regulatory ontology.
- Current uncertainty: The source work clarifies the existence of multiple procedural artifacts and identifier systems, but it does not yet provide a sufficiently systematic comparison of submission package contents or required evidence.
- Evidence or data needed: Real-world device dossiers, required submission checklists, and evidence maps by device class and jurisdiction.
- Suggested follow-up: Create a documentation-structure comparison that separates device identity data, quality/system evidence, clinical evidence, labeling information, and post-market obligations.

### 9. How should “evidence quality” be represented when comparing jurisdictions?

- Question: Can the ontology capture differences in evidentiary strength, validation requirements, and status of proof in a way that is consistent across jurisdictions?
- Why it matters: Regulatory records may look similar on paper while implying very different standards of proof, verification, or auditability.
- Current uncertainty: The source research indicates that similar artifact types may not carry equal evidentiary weight. This matters particularly for submissions, declarations, and post-market reporting.
- Evidence or data needed: Evidence categories such as manufacturer declaration, notified-body assessment, authority review, and monitoring data, together with their legal significance.
- Suggested follow-up: Distinguish evidence type, evidence source, and evidence status from the regulated object itself, so that registries and approvals remain semantically precise.

---

## Clinical evaluation and post-market obligations

### 10. Are clinical evidence and post-market surveillance requirements functionally comparable across jurisdictions?

- Question: Does a jurisdictional difference in the clinical evidence framework necessarily imply a difference in substantive safety or performance standards?
- Why it matters: Clinical evaluation and post-market follow-up influence both regulatory burden and the long-term evidence base for a device.
- Current uncertainty: The research indicates that the FDA and EU differ in how evidence is framed and how market access is achieved, but a systematic comparison of clinical evaluation obligations remains incomplete.
- Evidence or data needed: Device-level comparison of clinical evaluation pathways, post-market surveillance requirements, adverse-event reporting obligations, and vigilance systems.
- Suggested follow-up: Add a dedicated clinical-evidence and vigilance layer to the ontology rather than treating those obligations as peripheral to registration.

### 11. How should post-market obligations be linked to initial registration records?

- Question: Should post-market obligations be modeled as separate obligations attached to a device, actor, or registration record, and how should those links vary by jurisdiction?
- Why it matters: The same product can have different ongoing obligations depending on how it was registered and what market it entered. Without clear modeling, the ontology may underrepresent the lifecycle relationship.
- Current uncertainty: The comparison shows that registration and post-market duties are conceptually separate but operationally connected. The exact semantic relationship remains insufficiently specified.
- Evidence or data needed: Lifecycle diagrams showing the connection between initial registration, device listing, market placement, monitoring, and reporting events.
- Suggested follow-up: Treat post-market obligations as associated obligations linked to a device and its confirmed regulatory context, rather than as direct properties of a static registration object.

---

## Operational / implementation questions

### 12. Which abstraction should be primary in the ontology: record, process, actor, or role?

- Question: What is the correct semantic anchor for registration-related modeling when a single real-world action can involve a business site, a legal actor, an identifier, and a registry record?
- Why it matters: This choice affects every downstream class and relationship in the ontology. A wrong anchor can blur jurisdictional differences and prevent accurate queries.
- Current uncertainty: The research repeatedly distinguishes object types, but the exact hierarchy of object, role, event, and record is still a modeling decision that needs stronger grounding.
- Evidence or data needed: A set of canonical examples from both jurisdictions showing what counts as the object of regulation, what counts as an event, and what counts as an actor or role.
- Suggested follow-up: Use the design-decision process to fix a minimal ontology backbone before expanding into more detailed subclasses.

### 13. How should lifecycle transitions be represented without forcing a single universal timeline?

- Question: Can one common lifecycle model cover registration creation, update, discontinuation, reactivation, verification, and issuance across FDA and EU without losing jurisdictional nuance?
- Why it matters: Regulatory records are not static. They are created, updated, suspended, verified, and sometimes retired. Lifecycle semantics are essential for traceability.
- Current uncertainty: FDA and EU processes differ in the status transitions and the legal events that trigger them. A universal state model may be too coarse to capture these differences.
- Evidence or data needed: Lifecycle event dictionaries for each jurisdiction, including triggers, actors involved, and status transitions.
- Suggested follow-up: Keep jurisdiction-specific event classes and represent generalized lifecycle relations only at the highest abstract layer, if at all.

### 14. How should data provenance be captured when the same regulatory concept has multiple issuers or review bodies?

- Question: If a device has an identifier assigned by one authority, a registration record by another, and a certificate or declaration issued by a third party, how should provenance be modeled?
- Why it matters: Legal provenance is essential for understanding responsibility, auditability, and record validity. A flat data model may obscure who assigned what and under which authority.
- Current uncertainty: The comparison identifies multiple actors and authorities, but it does not yet settle how provenance should be linked across registry records, identifier assignments, and decision documents.
- Evidence or data needed: A provenance model that distinguishes issuer, subject, time, legal basis, and resulting artifact for each record type.
- Suggested follow-up: Introduce provenance relationships at the record and identifier level rather than assuming all metadata belongs on the primary device object.

---

## Priority questions for future research

### 15. Which unresolved mappings should receive priority in the next research phase?

- Question: Which open questions are most important for ontology construction and which can be deferred until later?
- Why it matters: Not all unresolved issues carry equal weight. Some affect the core structure of the model, while others matter mainly for detailed subclassing or implementation.
- Current uncertainty: The current evidence base is strong enough to distinguish many domain concepts, but it is not yet complete enough to decide which abstractions are stable across all jurisdictions.
- Evidence or data needed: A prioritization matrix based on impact on ontology structure, legal significance, and data availability.
- Suggested follow-up: Rank unresolved questions into (a) blocking for ontology design, (b) important for detailed comparison, and (c) suitable for future jurisdictional extension.

### 16. Which concepts are safe to unify, and which must remain jurisdiction-specific?

- Question: What is the appropriate boundary between shared abstraction and jurisdiction-specific representation in the ontology?
- Why it matters: This is the central design question. Over-generalization may erase legal meaning; under-generalization may make cross-jurisdiction comparison unnecessarily cumbersome.
- Current uncertainty: The current evidence suggests that some concept families (actor, identifier, registry record) may be shared, while others (SRN, notified body, Product Code, establishment) should remain explicit and distinct.
- Evidence or data needed: A concept mapping matrix graded by semantic similarity, legal equivalence, and implementation feasibility.
- Suggested follow-up: Use this matrix to decide where a common superclass is justified and where separate classes should be maintained.

---

In summary, the current evidence suggests that the core unresolved questions concern whether the jurisdictions share the same legal object, lifecycle, or evidentiary structure, rather than whether they share a common vocabulary alone. At this stage, the most defensible approach is to preserve shared concepts where they are stable, maintain jurisdiction-specific distinctions where the legal semantics diverge, and treat uncertain mappings as open questions pending further evidence. This keeps the ontology faithful to the source material while leaving space for later refinement as the knowledge graph matures.

## CQ validation note (2026-08-24)

- Action: Ran the registration CQ suite (ontology/registration/registration_competency_questions.sparql) against example data (ontology/registration/example_registration.ttl).
- Outcome: Two CQ items required small example-data fixes to return human-readable labels:
  - CQ3 expected status labels (statusLabel) but example status resources lacked rdfs:label values.
  - CQ5 returned decisions but decisionStatus labels were missing for the same reason.
- Fix applied: example_registration.ttl updated to add rdfs:label for reg:Approved and reg:Pending, and example role resources were given rdfs:label values to improve readability in CQ outputs.
- Follow-up: Re-run CQ suite and consider adding tests/SHACL shapes to ensure example/production data expose expected label properties where queries rely on them.

