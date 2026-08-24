# Registration Ontology Draft

## Overview

This document is a draft ontology structure for the Registration domain. It is intended as a bridge between the comparative research and later OWL/SHACL implementation. The goal is not to finalize a legal or jurisdictional interpretation, but to define a workable conceptual backbone that can support future implementation.

The draft is grounded in the findings from the comparison of FDA and EU MDR/IVDR registration concepts. It explicitly distinguishes between:

- regulatory records
- lifecycle events
- legal or operational actors
- role-bearing relationships
- identifiers
- documents and evidence artifacts
- decision outcomes

This distinction is essential because the source research shows that the same regulatory problem may be represented differently across jurisdictions. In particular, the ontology should preserve differences between:

- an actor registration and a device registration
- a physical establishment and a legal actor role
- a registry record and an authorization decision
- an identifier assignment and the entity it identifies

The document therefore emphasizes candidate classes and properties rather than asserting final equivalence. Where the evidence is strong, a shared abstraction is proposed. Where the evidence remains incomplete or legally distinct, the concept is retained as jurisdiction-specific.

---

## Core modeling principles

1. Preserve the distinction between record and event.
   - A registration record is a persistent object.
   - A registration event is a temporal act that creates, updates, verifies, or revokes the record.

2. Separate actor from role.
   - An organization may act as manufacturer, importer, distributor, or authorised representative in different contexts.
   - Roles should not collapse the legal entity into a single universal type without preserving jurisdictional nuance.

3. Separate identifier from the entity it identifies.
   - A UDI, Basic UDI-DI, SRN, listing number, or product code is not merely a literal string; it is a typed identifier with owner, issuer, scope, and lifecycle.

4. Keep jurisdictional semantics explicit.
   - Shared abstractions are allowed only where the evidence supports a stable semantic boundary.
   - If a concept is structurally different across jurisdictions, retain the distinction.

5. Differentiate process from outcome.
   - A submission, a certification step, a verification event, and a final approval or CE-marking decision are not the same kind of object.

6. Treat uncertain equivalence as unresolved.
   - Where a mapping is plausible but not sufficiently evidenced, the ontology should keep the concepts separate and flag the mapping as needing evidence.

---

## Candidate classes

### Class: RegulatoryEntity
- Definition: A generic top-level entity for a regulated subject or actor relevant to registration and market access.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This class should remain abstract or high-level. It may serve as a parent for Device, Organization, Person, Establishment, EconomicOperator, and related entities. It should not be used to collapse incompatible legal objects.

### Class: Device
- Definition: A medical device or device-like regulated product subject to registration, listing, classification, or market-access activity.
- Typical jurisdictional representation: Shared abstraction, with jurisdiction-specific subclasses when needed.
- Notes: Device is the core regulated object. It should be linked to identifiers, classifications, registrations, declarations, and lifecycle events, without assuming one universal market-access model.

### Class: RegistrationRecord
- Definition: A persistent record describing the regulatory presence or status of a device, actor, or site in a jurisdictional system.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This is a foundational class for distinguishing a registry record from the event that created it. Examples include establishment registration records, device listing records, and device registration records.

### Class: RegistrationEvent
- Definition: An event that creates, updates, verifies, or removes a registration record.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This class should represent lifecycle activity rather than static data. It may be specialized into FDA-specific or EU-specific event classes.

### Class: Establishment
- Definition: A place of business or operational site associated with device manufacturing, distribution, or import-related obligations.
- Typical jurisdictional representation: FDA-specific concept.
- Notes: This should not be treated as equivalent to an EU economic operator. It is a site or operations concept, not necessarily a legal actor class.

### Class: Organization
- Definition: A legal or business organization that may hold regulatory roles.
- Typical jurisdictional representation: Shared abstraction.
- Notes: Organization is the legal entity; manufacturer, importer, distributor, and authorised representative are role-bearing relationships attached to it rather than necessarily subclasses.

### Class: Person
- Definition: An individual who plays a regulatory role or acts on behalf of an organization.
- Typical jurisdictional representation: Shared abstraction.
- Notes: Useful for persons such as designated official correspondents, responsible persons, or authorized agents where the jurisdiction supplies such roles.

### Class: RegulatoryRole
- Definition: A role an entity plays in the regulatory lifecycle.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This is a key class for modeling manufacturer, importer, distributor, authorised representative, owner, operator, and similar roles without hard-coding them as organization subclasses.

### Class: ManufacturerRole
- Definition: The role of a party that manufactures or has responsibility for manufacturing a device.
- Typical jurisdictional representation: Shared abstraction; jurisdiction-specific constraints may apply.
- Notes: This should be represented as a specialization of RegulatoryRole, not as a direct subclass of Organization.

### Class: ImporterRole
- Definition: The role of a party bringing a device into a jurisdictional market or handling import-related obligations.
- Typical jurisdictional representation: Shared abstraction with FDA-specific InitialImporter variant.
- Notes: The FDA may distinguish an initial importer role; the EU imports through a more explicit importer concept. The role can be refined by jurisdiction.

### Class: DistributorRole
- Definition: The role of a party distributing a device in a regulated market.
- Typical jurisdictional representation: Shared abstraction.
- Notes: Similar semantics across jurisdictions but different legal obligations and verification steps.

### Class: AuthorisedRepresentativeRole
- Definition: A role representing a party formally designated to act on behalf of a manufacturer in a jurisdiction.
- Typical jurisdictional representation: EU-specific concept with possible functional analogue in FDA.
- Notes: Do not equate directly with a generic official correspondent unless the evidence clearly supports such a mapping.

### Class: EconomicOperator
- Definition: A regulated actor concept explicitly represented in the EU framework.
- Typical jurisdictional representation: EU-specific concept.
- Notes: This class should remain distinct from Establishment unless further evidence supports a shared abstraction. It is legally actor-focused, whereas Establishment is operational/site-focused.

### Class: SRN
- Definition: A single registration number issued to a regulated actor in the EU context.
- Typical jurisdictional representation: EU-specific identifier/record concept.
- Notes: This should be modeled as a typed identifier or credentials artifact, not merely as a string attribute on Organization.

### Class: DeviceListingRecord
- Definition: A registry record that corresponds to a device listed in a jurisdictional database.
- Typical jurisdictional representation: FDA-specific record concept with analogous EU device registration record.
- Notes: This should not be collapsed into a generic device registration record without preserving lifecycle and authority semantics.

### Class: DeviceRegistrationRecord
- Definition: A registry record linked to the EU or other jurisdictional device registration system.
- Typical jurisdictional representation: EU-specific concept with analogous FDA listing record.
- Notes: This is likely a sibling concept to DeviceListingRecord rather than a strict synonym.

### Class: Identifier
- Definition: A typed identifier assigned by a regulatory authority or system.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This should be the superclass for UDI, BasicUDIDI, SRN, ProductCode, listing number, and submission identifiers.

### Class: DeviceIdentifier
- Definition: An identifier assigned to a device or device model.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This may include UDI-DI and related device-level IDs.

### Class: ProductionIdentifier
- Definition: A production-level identifier associated with a specific device unit or production instance.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This is relevant for UDI-PI semantics.

### Class: BasicUDIDI
- Definition: A grouping identifier used in the EU framework to group device variants under a common registration identity.
- Typical jurisdictional representation: EU-specific concept.
- Notes: This should not be directly equated with FDA listing number or product code without explicit evidence.

### Class: ProductCode
- Definition: A device classification or reference code used in the FDA framework.
- Typical jurisdictional representation: FDA-specific concept.
- Notes: Similar to classifications in other systems, but likely not equivalent to EU EMDN or Basic UDI-DI.

### Class: Submission
- Definition: A submission, application, or dossier presented to a regulator or other authority.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This is a process/exchange object and should not be conflated with the outcome or final decision.

### Class: RegulatoryDecision
- Definition: An authoritative or formally recorded outcome of a review, evaluation, or conformity process.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This may include FDA clearance, approval, Denovo decision, and EU certificate/CE-marking-related outcome. It should not be treated as identical to a submission or a registration record.

### Class: ApprovalDecision
- Definition: A positive regulatory determination issued by a competent authority or agency.
- Typical jurisdictional representation: Shared abstraction with jurisdiction-specific subclasses.
- Notes: Candidate specializations include FDA clearance/approval decision and EU conformity assessment outcome.

### Class: CMDecision or CEMarkingDecision
- Definition: A decision or artifact indicating conformance with a regulatory framework and suitability for placement on the market.
- Typical jurisdictional representation: EU-specific concept.
- Notes: This concept should remain distinct from a generic approval unless the evidence supports a higher-level abstraction.

### Class: Certificate
- Definition: An issued conformity or approval certificate by an authorized body.
- Typical jurisdictional representation: EU-specific concept, with possible analogues in FDA decisions.
- Notes: A certificate is not the same as a submission or a legal actor registration record.

### Class: EvidenceArtifact
- Definition: A document or dataset used to support a registration, evaluation, or conformity claim.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This class supports differentiation between declarations, test summaries, clinical evidence, quality-system documents, and other supporting material.

### Class: PostMarketObligation
- Definition: An obligation or duty that continues after a device has entered the market.
- Typical jurisdictional representation: Shared abstraction.
- Notes: These obligations are distinct from the initial registration record and should be linked to device, actor, and jurisdictional context.

### Class: Jurisdiction
- Definition: A regulatory environment or market area considered in the ontology.
- Typical jurisdictional representation: Shared abstraction.
- Notes: This class supports mapping between FDA, EU, and other jurisdictional boundaries without forcing a single global representation.

---

## Candidate object properties

### Property: hasRegistrationRecord
- Domain: Device, Organization, Establishment, EconomicOperator
- Range: RegistrationRecord
- Intended meaning: Connects a regulated entity to a persistent record of regulatory presence.
- Notes: This property should be used carefully because a device and an actor may each have different kinds of registration records.

### Property: createdByEvent
- Domain: RegistrationRecord
- Range: RegistrationEvent
- Intended meaning: Indicates the lifecycle event that created or changed the record.
- Notes: Useful for provenance and temporal traceability.

### Property: hasActorRole
- Domain: Organization, Person
- Range: RegulatoryRole
- Intended meaning: Connects an entity to a role it plays in a regulatory context.
- Notes: This is a preferred property over direct subclassing for organizational roles.

### Property: playsRoleIn
- Domain: Organization, Person
- Range: Device, RegistrationRecord, Submission, RegulatoryDecision
- Intended meaning: Indicates the role played by an actor in relation to a specific regulated object or process.
- Notes: This helps capture “manufacturer of device X,” “importer for market Y,” or “authorised representative for manufacturer Z.”

### Property: hasEstablishment
- Domain: Organization
- Range: Establishment
- Intended meaning: Connects a legal organization to a place of business or operational site.
- Notes: This is a candidate FDA-facing relation that should not be blindly generalized to the EU model.

### Property: hasEconomicOperatorRole
- Domain: Organization, Person
- Range: EconomicOperator
- Intended meaning: Links an actor to an EU-specific economic operator concept.
- Notes: Retain as jurisdiction-specific unless evidence supports broader abstraction.

### Property: hasIdentifier
- Domain: Device, Organization, Establishment, EconomicOperator, Submission, RegistrationRecord
- Range: Identifier
- Intended meaning: Connects a regulatory object to its assigned identifiers.
- Notes: This property should be generic enough to support multiple identifier families.

### Property: issuedByAuthority
- Domain: Identifier, Certificate, RegulatoryDecision, RegistrationRecord
- Range: RegulatoryAuthority, NotifiedBody, Jurisdiction
- Intended meaning: Captures the authority or body that assigned or issued the artifact.
- Notes: Important for provenance and for distinguishing authority-issued from manufacturer-issued artifacts.

### Property: identifies
- Domain: Identifier
- Range: Device, Organization, Establishment, EconomicOperator, RegistrationRecord
- Intended meaning: Declares what the identifier refers to.
- Notes: This property is necessary because identifiers are semantically meaningful beyond simple strings.

### Property: hasSubmission
- Domain: Device, Organization, RegulatoryDecision, Jurisdiction
- Range: Submission
- Intended meaning: Connects a regulated subject or process to a submission or dossier.
- Notes: A submission is not the same as the final decision; this distinction should be kept explicit.

### Property: hasDecision
- Domain: Submission, Device, Organization
- Range: RegulatoryDecision
- Intended meaning: Connects a submission or regulatory process to a final decision outcome.
- Notes: This property supports process-to-outcome reasoning without collapsing the decision into the original submission.

### Property: supportsEvidence
- Domain: Submission, RegulatoryDecision, RegistrationRecord
- Range: EvidenceArtifact
- Intended meaning: Connects a regulatory object to the evidence that underpins or substantiates it.
- Notes: This is essential for distinguishing proof artifacts from decision artifacts.

### Property: subjectOfObligation
- Domain: Device, Organization
- Range: PostMarketObligation
- Intended meaning: Connects a regulated object or actor to ongoing post-market obligations.
- Notes: This property should be separate from registration and approval properties.

### Property: hasJurisdiction
- Domain: Device, Organization, Submission, RegistrationRecord, RegulatoryDecision
- Range: Jurisdiction
- Intended meaning: Declares the regulatory environment in which the object exists or is active.
- Notes: This property helps avoid conflating EU and FDA semantics under one global entity.

### Property: hasStatus
- Domain: RegistrationRecord, Submission, RegulatoryDecision, PostMarketObligation
- Range: StatusValue
- Intended meaning: Captures lifecycle state or current state of the object.
- Notes: Status should be modeled as a property or controlled vocabulary, not as a surrogate for the object itself.

### Property: referencesRecord
- Domain: RegistrationEvent, RegulatoryDecision, Submission
- Range: RegistrationRecord
- Intended meaning: Indicates the targeted record affected by an event or decision.
- Notes: Useful when multiple actions may modify or validate the same registration record.

---

## Candidate data properties

### Data property: registrationNumber
- Domain: RegistrationRecord
- Range: xsd:string
- Intended meaning: A literal value assigned to a registration record.
- Notes: This should be used only when the specific number type is already represented elsewhere as a typed identifier or record property.

### Data property: issueDate
- Domain: Identifier, RegistrationRecord, Certificate, RegulatoryDecision
- Range: xsd:date or xsd:dateTime
- Intended meaning: The date on which the identifier, record, certificate, or decision was issued.
- Notes: Distinguish issue date from effective date when needed.

### Data property: effectiveDate
- Domain: RegistrationRecord, RegulatoryDecision, PostMarketObligation
- Range: xsd:date or xsd:dateTime
- Intended meaning: The date on which the record or obligation becomes effective.
- Notes: This may differ from issuance date.

### Data property: statusLabel
- Domain: RegistrationRecord, Submission, RegulatoryDecision, PostMarketObligation
- Range: xsd:string
- Intended meaning: A human-readable status value.
- Notes: Still useful for display-oriented systems, but should be backed by a controlled vocabulary or structured status class when possible.

### Data property: submissionIdentifier
- Domain: Submission
- Range: xsd:string
- Intended meaning: A unique identifier assigned to a submission artifact.
- Notes: Prefer representing this as a typed Identifier object in a more mature ontology.

### Data property: legalEntityName
- Domain: Organization, Person
- Range: xsd:string
- Intended meaning: Human-readable legal or business name.
- Notes: This is useful but should not replace the structured representation of legal relationships.

### Data property: deviceName
- Domain: Device
- Range: xsd:string
- Intended meaning: Human-readable name or model name.
- Notes: This is not a substitute for device identity or classification.

### Data property: documentReference
- Domain: EvidenceArtifact, Submission, Certificate
- Range: xsd:anyURI
- Intended meaning: Pointer to a stored file or external document.
- Notes: Useful for implementation but should not replace semantic linking to the evidence artifact itself.

---

## Relationship patterns

### Pattern 1: Device → hasIdentifier → Identifier
- Purpose: Capture the core identity of a device.
- Notes: This pattern supports UDI, DI, PI, Basic UDI-DI, and other typed identifier families without flattening them into a single string field.

### Pattern 2: Organization/Person → hasActorRole → RegulatoryRole
- Purpose: Represent legal responsibility and operational role.
- Notes: This pattern avoids a brittle model where each actor must be subclassed as a manufacturer or distributor.

### Pattern 3: Device → hasRegistrationRecord → RegistrationRecord
- Purpose: Link the regulated product to its registration records.
- Notes: A device may have multiple records across jurisdictions or lifecycle states.

### Pattern 4: RegistrationRecord → createdByEvent → RegistrationEvent
- Purpose: Preserve lifecycle provenance.
- Notes: This supports temporal tracking of creation, update, verification, suspension, reactivation, or deletion.

### Pattern 5: Submission → hasDecision → RegulatoryDecision
- Purpose: Separate the reviewing process from the final outcome.
- Notes: This pattern is important because approval/clearance and submission are conceptually distinct.

### Pattern 6: Device → subjectOfObligation → PostMarketObligation
- Purpose: Capture ongoing obligations after market entry.
- Notes: These obligations are distinct from the initial registration event and should not be absorbed into the device’s static metadata.

### Pattern 7: Identifier → identifies → Device/Organization/Record
- Purpose: Ensure the identifier is semantically grounded.
- Notes: This pattern helps distinguish product identifiers from actor identifiers and registration numbers.

### Pattern 8: RegistrationRecord → hasJurisdiction → Jurisdiction
- Purpose: Maintain jurisdictional boundaries.
- Notes: This pattern is critical for preventing false cross-jurisdiction equivalence.

---

## Lifecycle patterns

### Lifecycle A: Registration record creation
- Proposed flow: Device or Organization → hasRegistrationRecord → RegistrationRecord → createdByEvent → RegistrationEvent
- Notes: The lifecycle begins with an event that introduces a registration record into a jurisdictional system.

### Lifecycle B: Identifier assignment
- Proposed flow: Device or Actor → hasIdentifier → Identifier → issuedByAuthority → Authority
- Notes: This may precede or follow the creation of a registration record. The order differs by jurisdiction.

### Lifecycle C: Submission to decision
- Proposed flow: Submission → hasDecision → RegulatoryDecision
- Notes: This separates the action of submitting from the legally effective outcome.

### Lifecycle D: Post-market obligation tracking
- Proposed flow: Device or Organization → subjectOfObligation → PostMarketObligation → hasStatus → StatusValue
- Notes: Obligations can remain active long after the initial registration event.

### Lifecycle E: Update and verification events
- Proposed flow: RegistrationRecord → createdByEvent → RegistrationEvent → referencesRecord → RegistrationRecord
- Notes: Update or verification events should not overwrite the original record without retaining provenance.

This pattern reflects the design decision to preserve both persistent records and the temporal acts that produce those records.

---

## Jurisdiction-specific modeling notes

### FDA-specific modeling candidates

- Establishment as a site/operations concept
- Device listing as a device registry record distinct from establishment registration
- Product Code as a classification or identifier family distinct from Basic UDI-DI
- Submission to clearance/approval as a review-driven process
- Official correspondent or owner/operator concepts as role-bearing constructs

### EU-specific modeling candidates

- EconomicOperator as a legal actor concept
- SRN as a typed registration identifier or actor credential
- Basic UDI-DI as a device grouping identifier distinct from product code or listing number
- Notified Body and certificate concepts as separate from the device registration record
- CE marking / conformity assessment as a decision pattern that should not be forced into an FDA-style approval model

### Shared abstraction candidates

- Device
- Organization
- Person
- RegulatoryRole
- Identifier
- Submission
- RegistrationRecord
- RegulatoryDecision
- Jurisdiction
- PostMarketObligation

These shared abstractions should be introduced only when they add semantic clarity. They are useful as common anchors, but they should not erase the jurisdiction-specific legal meaning carried by many domain concepts.

### Need-evidence mappings

The following mappings should remain explicit as unresolved unless stronger evidence is added:

- FDA Device Listing vs EU Device Registration Record
- FDA Product Code vs EU classification or assignment code
- FDA Establishment vs EU EconomicOperator
- FDA approval/clearance outcome vs EU CE-marking/conformity decision
- FDA registration number vs EU SRN as a strict semantic equivalence

These should be marked in implementation notes as “needs evidence” or “retain as jurisdiction-specific” rather than forced into a shared class definition.

---

## Open modeling risks

### 1. Over-generalization of legal actor concepts
- Risk: Collapsing Organization, EconomicOperator, Manufacturer, and Establishment into one hierarchy may hide important legal differences.
- Mitigation: Keep Organization and RegulatoryRole separated; represent role as a relationship or role class.

### 2. Equating any database record with a legal decision
- Risk: Treating a listing record, registration record, or certificate as if it were the same as a market authorization decision.
- Mitigation: Maintain clear class separation between record, event, and decision.

### 3. Flattening identifiers into strings
- Risk: A string-only representation loses issuer, target object, lifecycle, and regulatory semantics.
- Mitigation: Represent identifiers as typed classes with issuer, target, and date metadata.

### 4. Assuming a universal lifecycle model
- Risk: A single lifecycle state model may not fit both regulatory review processes and registry updates.
- Mitigation: Keep universal lifecycle relationships abstract and allow jurisdiction-specific event subclasses.

### 5. Forcing equivalence across jurisdictions too early
- Risk: Cross-jurisdiction mapping can overfit to terminology and underrepresent legal distinctions.
- Mitigation: Use a careful mapping rubric: direct equivalence, related but not equivalent, jurisdiction-specific, and unresolved.

---

This draft aims to provide a stable ontology backbone for the Registration domain without prematurely committing to a single legal interpretation. It is specifically designed to support the next implementation stage: translating candidate classes and properties into OWL classes, object properties, and SHACL constraints while preserving uncertainty where the evidence base is still incomplete.
