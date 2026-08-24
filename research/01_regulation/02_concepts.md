# 02_concepts.md — Candidate concepts (source-grounded)

This document translates the cross-jurisdiction comparison into a prioritized, source-traceable list of candidate ontology concepts for the Registration domain. Each entry includes:
- short definition
- evidence (trace to the source research artifacts)
- primary relationships, events, and identifiers referenced in the sources
- modeling status: REQUIRED, OPTIONAL, or NEEDS_MORE_EVIDENCE
    REQUIRED: Concept is necessary for the Registration domain ontology.
    JURISDICTION-SPECIFIC: Concept is required/relevant within a specific jurisdiction but is not established as a cross-jurisdiction concept.
    OPTIONAL: Potentially useful but not necessary for the initial scope.
    NEEDS_MORE_EVIDENCE: Concept is plausible/relevant, but current evidence is insufficient to determine its precise ontology semantics.
- unresolved questions to track for the next stage

Primary evidence artifacts (source research files):
- FDA research: [research/01_registration/sources/01_FDA.md](D:/00_Coding/medtech-regulatory-ontology.worktrees/researchregistrationcross-jurisdiction-compariso/research/01_registration/sources/01_FDA.md)
- MDR / IVDR research: [research/01_registration/sources/02_MDR_IVDR.md](D:/00_Coding/medtech-regulatory-ontology.worktrees/researchregistrationcross-jurisdiction-compariso/research/01_registration/sources/02_MDR_IVDR.md)

Guidance: These are concepts extracted directly from the two source research files. Do not treat these as final ontology classes/properties — they are candidate concepts to be refined in 03_design_decisions.md and 05_ontology_draft.md.

---

## Concept entries

### 1) Device / MedicalDevice
- Definition: Regulatory object defined by intended purpose declared by the manufacturer (manufacturer-intent-dependent device concept).  
- Evidence: FDA: device/device classification sections ([01_FDA.md — 2.10 Device Classification, 2.14 510(k)]); EU: MDR Art.2 definitions (see [02_MDR_IVDR.md — Concept: Medical Device]).
- Primary relationships/events: manufacturedBy → Manufacturer; hasClassification → Class (FDA) / EMDN (EU); may undergo → ConformityAssessment (EU) or PremarketSubmission (FDA).  
- Identifiers: DI / UDI-DI (device-model identity), ProductCode (FDA), Basic UDI-DI (EU).  
- Modeling status: REQUIRED
- Unresolved questions: mapping of FDA ProductCode ↔ EU EMDN (Insufficient evidence in current research).

---

### 2) Manufacturer (role)
- Definition: A role-bearing legal actor that manufactures, refurbishes, or places devices on the market; defines intended purpose and assumes key regulatory obligations.  
- Evidence: FDA: manufacturer activity and role (see [01_FDA.md — 2.2 Manufacture / processing, 6 Actors]); EU: explicit role and obligations (see [02_MDR_IVDR.md — Concept: Manufacturer]).
- Primary relationships/events: manufactures → Device; assignsUDIs / submitsDeviceRegistration (EU); registers establishments (FDA contexts) or economic operator (EU).  
- Identifiers: may be associated with SRN (EU) or establishment registration number (FDA).  
- Modeling status: REQUIRED
- Unresolved questions: representation as OrganizationRole vs Organization subclass; handling of role transfers when intended purpose changes (EU Rule R09).

---

### 3) Establishment (place-of-business) [FDA-specific semantic]
- Definition: A place of business under one management at one general physical location (FDA Part 807 definition).  
- Evidence: [01_FDA.md — 2.1 Concept: Establishment; 2.6 Establishment Registration].
- Primary relationships/events: owner/operator registers establishment (EstablishmentRegistration event), establishment performs DeviceActivity (manufacturing, repackaging, relabeling).  
- Identifiers: Establishment Registration Number (FDA).  
- Modeling status: REQUIRED (FDA-layer)
- Modeling note: FDA treats Establishment as a regulatory object distinct from Manufacturer; do NOT equate with Manufacturer.  
- Relevance: Important for FDA-layer modeling; EU performs actor registration (SRN) rather than establishment registration as a central object.

---

### 4) EconomicOperator / SRN (EU actor & actor-registration)
- Definition: EU legal construct grouping manufacturer, authorised representative, importer, distributor and others; competent authority issues an SRN after verification.  
- Evidence: [02_MDR_IVDR.md — Concept: Economic Operator; Concept: SRN; Event E01–E03].
- Primary relationships/events: EconomicOperatorRegistrationSubmission → CompetentAuthorityVerification → SRNIssuance.  
- Identifiers: SRN (Single Registration Number) — EU-wide economic-operator identifier.  
- Modeling status: REQUIRED (EU-layer)
- Unresolved questions: MDR vs IVDR differences in the EconomicOperator definition and whether a common cross-jurisdiction abstraction is appropriate (source notes differences).

---

### 5) Importer and InitialImporter
- Definition: Importer (actor placing devices from third countries on market); FDA additionally defines Initial Importer as the US importer that furthers marketing of a device from a foreign manufacturer.  
- Evidence: FDA: [01_FDA.md — 2.3 Initial Importer; 2.4 Importer]; EU: [02_MDR_IVDR.md — Concept: Importer].
- Primary relationships/events: placesOnMarket (EU) / importsDevice (FDA); FDA InitialImporter has specific registration/listing obligations.  
- Identifiers: may be linked to SRN (EU) or establishment/registration numbers (FDA).  
- Modeling status: REQUIRED
- Modeling note: Represent Importer as common concept with FDA-specific InitialImporter role/subtype.

---

### 6) Distributor
- Definition: Supply-chain actor that makes devices available before putting into service; has verification obligations (e.g., CE marking, DoC checks in EU).  
- Evidence: FDA: referenced distributor/wholesale distributor (01_FDA.md — Actors); EU: Concept: Distributor (02_MDR_IVDR.md).  
- Primary relationships/events: makesAvailable → Device; verification events triggered at placing/making available.  
- Modeling status: REQUIRED

---

### 7) Authorised Representative (EU)
- Definition: EU-established natural or legal person representing a manufacturer outside the Union under a written mandate; supports registration and competent-authority interactions.  
- Evidence: [02_MDR_IVDR.md — Concept: Authorised Representative].
- Primary relationships/events: hasMandate → Manufacturer; may act in EUDAMED registration and interact with Competent Authority.  
- Modeling status: REQUIRED (EU-layer)
- Modeling note: No direct FDA statutory equivalent in the current FDA source research — treat as EU-specific.

---

### 8) Notified Body (EU) and Assessor / Review Body (general)
- Definition: Notified Body — EU-designated conformity assessment body performing conformity assessment and issuing certificates; FDA uses internal review panels and agency reviewers rather than notified-body model.  
- Evidence: [02_MDR_IVDR.md — Concept: Notified Body; Event E06–E07].  
- Primary relationships/events: performsConformityAssessment → Device; issues → Certificate; uploads relevant EUDAMED information.  
- Modeling status: REQUIRED (EU-layer); consider optional high-level AssessorBody abstraction if needed across jurisdictions (confidence: LOW–MEDIUM).  
- Risk: do not conflate Notified Body semantics with FDA reviewers — different designation and legal effects.

---

### 9) RegulatoryAuthority (FDA: FDA; EU: Competent Authority)
- Definition: The governmental authority charged with verification, oversight, issuance of authoritative regulatory decisions or designation (FDA vs national competent authority in EU).  
- Evidence: [01_FDA.md — Actors / PMA / 510(k) review], [02_MDR_IVDR.md — Competent Authority responsibilities, SRN issuance].  
- Primary relationships/events: verifiesRegistrationData (EU), issues/records decisions (FDA PMA Approval), oversees Notified Bodies (EU).  
- Modeling status: REQUIRED

---

### 10) RegistrationRecord (Registry) — DeviceRegistration / EstablishmentRegistration / EconomicOperatorRegistration
- Definition: Persistent regulatory record created by a registration event and stored in a regulatory information system (GUDID, EUDAMED, FDA listing/registration systems).  
- Evidence: FDA: EstablishmentRegistration, DeviceListing, GUDID (01_FDA.md — 2.6, 2.7, 2.28); EU: DeviceRegistration, EconomicOperatorRegistration, EUDAMED (02_MDR_IVDR.md — Device Registration, SRN, EUDAMED).  
- Primary relationships/events: createdBy → registration submission; verifiedBy → competent authority (EU); lifecycle events: create, update, verification, reactivation, discontinuation.  
- Modeling status: REQUIRED
- Modeling note: Keep device registration records separate from certificates/market-access artifacts.

---

### 11) RegulatorySubmission (FDA-specific submission types and EU conformity applications)
- Definition: A submission or application to a regulatory process (examples: 510(k), PMA, De Novo, HDE, IDE in FDA; applications/requests to Notified Body or EUDAMED entries in EU).  
- Evidence: [01_FDA.md — PremarketSubmission types 2.14–2.22]; [02_MDR_IVDR.md — Conformity Assessment, Notified Body interactions].  
- Primary relationships/events: submittedBy → Applicant/Manufacturer; resultsIn → RegulatoryDecision / Certificate / SEDetermination / Approval.  
- Identifiers: PremarketSubmissionIdentifier (FDA submission number); Notified Body application references (EU).  
- Modeling status: REQUIRED
- Modeling note: Represent submission and decision as separate, reified objects (submissionEvent → reviewEvent → decisionEvent).

---

### 12) RegulatoryDecision / Determination (reified)
- Definition: A reified regulatory determination/event that records who decided, on what submission, when, and with what outcome (e.g., SEDetermination, PMAApproval, DeNovoDecision, ConformityAssessmentOutcome).  
- Evidence: FDA: SEDetermination and Clearance (01_FDA.md — 2.15–2.17); EU: ConformityAssessment outcomes, Certificate issuance (02_MDR_IVDR.md — Event E06–E07).  
- Primary relationships/events: resultsIn → regulatory state change (Cleared, Approved, Classified, Certified); provenance: issuedBy → RegulatoryAuthority or NotifiedBody; references → submission / conformity-assessment record.  
- Modeling status: REQUIRED
- Modeling note: Reification is essential to preserve the context of predicate-device comparisons (FDA) and certificate provenance (EU).

---

### 13) Certificate (EU) and Approval/Clearance (FDA)
- Definition: Regulatory artifacts evidencing conformity or authorization: EU: Notified-Body-issued certificate, manufacturer-issued EU Declaration of Conformity and CE marking; FDA: PMA Approval, 510(k) Clearance.  
- Evidence: [01_FDA.md — PMA Approval, 510(k) Clearance]; [02_MDR_IVDR.md — Concept: Certificate, EU Declaration of Conformity, CE Marking].  
- Primary relationships/events: issuedBy → NotifiedBody (EU) or FDA (PMA); affixedBy → Manufacturer (CE Mark).  
- Modeling status: REQUIRED
- Modeling note: Keep EU certificates and FDA approvals/clearances as distinct concept artifacts; only later consider a higher-level Authorization artifact if semantics can be preserved.

---

### 14) Device Identification — DI / UDI-DI / PI / UDI-PI
- Definition:Regulatory identification mechanisms used to identify a medical device and, where applicable, production-related information.

Jurisdiction: FDA / EU

FDA terminology:
- Device Identifier (DI)
- Production Identifier (PI)
- UDI
- GUDID

EU terminology:
- UDI
- UDI-DI
- UDI-PI
- Basic UDI-DI
- EUDAMED UDI/Devices module

Modeling status:
REQUIRED

Important modeling note:
The existence of device-identification concepts is supported in both
jurisdictions. Exact semantic equivalence between FDA DI/PI and EU
UDI-DI/UDI-PI must not be assumed at the concept-analysis stage.

- Evidence: FDA: UDI, DI, PI, GUDID (01_FDA.md — 2.25–2.28); EU: UDI, Basic UDI‑DI, UDI‑DI, UDI‑PI and EUDAMED UDI/DEV module (02_MDR_IVDR.md — UDI sections). MDCG guidance (MDCG 2018‑1 Rev.4; MDCG 2022‑7) clarifies Basic UDI‑DI semantics and assignment/change expectations for MDR and IVDR. (See [02_MDR_IVDR.md — 1.3 MDCG sources] for trace to MDCG docs.)  

---

### 15) Basic UDI-DI (EU-specific semantics)
- Definition: EU-required Basic UDI‑DI assigned prior to placing the relevant device on the market and submitted to EUDAMED; serves as a regulatory grouping/reference identifier that links to the core device dataset.  
- Evidence: [02_MDR_IVDR.md — Concept: Basic UDI‑DI; Event E04; Rule R02]; MDCG guidance (MDCG 2018‑1 Rev.4; MDCG 2022‑7) clarifies role and assignment/change expectations for Basic UDI‑DI under MDR and IVDR.  
- Primary relationships/events: BasicUDIDIAssignment precedes PlacingOnMarket; for specified conformity-assessment routes BasicUDIDIAssignment precedes NotifiedBodyApplication; Basic UDI‑DI is included in EUDAMED UDI/DEV module and links to DeviceRegistrationRecords.  
- Modeling status: REQUIRED (EU-layer)
- Ontology observations:  
  - Basic UDI‑DI behaves as a registry/grouping identifier rather than a per-production-instance identifier; model separately from UDI‑DI (model-level DeviceIdentifier) and UDI‑PI (production-level identifiers).  
  - Capture BasicUDIDIAssignment and BasicUDIDIChange as reified events with provenance (actor, date, source) to preserve the regulatory context of assignment and any permitted changes.  
- Unresolved questions: normative Annex VI details and edge-case change rules (e.g., software‑based device families, significant intended‑purpose change) require review of Annex VI and MDCG examples for authoritative modeling rules — [EXTERNAL SOURCE REQUIRED].

---

### 16) Jurisdiction-Specific Device Classification / Nomenclature Systems
- FDA:Product Code
- EU: EMDN
- Definition: Jurisdiction-specific coding or nomenclature mechanisms used to categorize or identify regulated devices for regulatory purposes.
- Evidence: FDA: Product Code (01_FDA.md — 2.8); EU: EMDN mention (02_MDR_IVDR.md — Identifiers table).  
- Modeling status: REQUIRED as jurisdiction-specific concepts
- Cross-jurisdiction equivalence: UNRESOLVED
- Important modeling note: Product Code and EMDN must not be modeled as equivalent identifiers without additional evidence establishing their semantic relationship.Unresolved questions: mapping rules for ProductCode ↔ EMDN (Insufficient evidence in current research).

---

### 17) GUDID / EUDAMED (Regulatory Information Systems)
- Definition: Regulatory information systems: FDA GUDID stores DI records and other FDA databases; EUDAMED is a modular EU system (actor, UDI/device, notified bodies & certificates, market surveillance, other modules).  
- Evidence: [01_FDA.md — 2.28 GUDID]; [02_MDR_IVDR.md — Concept: EUDAMED, EUDAMED modules].  
- Modeling status: REQUIRED (model as registry/system concept)
- Modeling note: Represent the system itself (Registry) and the record objects it contains separately.

---

### 18) DeviceListing (FDA) vs DeviceRegistrationRecord (EU)
- Definition: FDA DeviceListing is the Part 807 listing record with listing number and lifecycle events (create/update/discontinue/reactivate). EU DeviceRegistrationRecord refers to device records in EUDAMED associated with Basic UDI-DI and related core data elements.  
- Evidence: [01_FDA.md — 2.7 Device Listing; 5.2 Device listing lifecycle]; [02_MDR_IVDR.md — Device Registration, Event E05].  
- Modeling status: REQUIRED
- Unresolved questions: Are listing-number ↔ EUDAMED device-record mappings feasible? Insufficient evidence to assert equivalence.

---

### 19) Reified lifecycle events (examples to model as first-class objects)
- Examples: EstablishmentRegistration, DeviceListingCreation, DeviceListingDiscontinuation, 510kSubmission, 510kSEDetermination, PMASubmission, PMAApproval, DeNovoRequestSubmission, DeNovoDecision, IDEApproval, BasicUDIDIAssignment, DeviceRegistrationSubmission, ConformityAssessmentPerformed, CertificateIssuance, SRNIssuance, PlacingOnMarket, MakingAvailable, PuttingIntoService.  
- Evidence: Both source files enumerate lifecycle events (see [01_FDA.md — Sections 5.x] and [02_MDR_IVDR.md — Events E01–E13]).  
- Modeling status: REQUIRED
- Modeling note: Reifying events preserves provenance (actor, date, source) and avoids conflating a persistent record with the event that created it.

---

### 20) CertificateOfFreeSale (EU) and related export artifacts
- Definition: EU-specific certificate evidencing ability to market or export (MDR Article 60).  
- Evidence: [02_MDR_IVDR.md — Concept: Certificate of Free Sale].  
- Modeling status: OPTIONAL (EU-layer) — include if export-use cases are in scope.

---

## Prioritization guidance
- REQUIRED: Device, ManufacturerRole, RegulatoryActor, Importer/InitialImporter, Distributor, Establishment (FDA), EconomicOperator & SRN (EU), UDI/DI/PI, DeviceRegistration/DeviceListing, RegulatorySubmission and RegulatoryDecision (reified), GUDID/EUDAMED, Certificate(ies), NotifiedBody (EU).  
- OPTIONAL: CertificateOfFreeSale, certain historical HDE threshold tracking artifacts (unless historical auditability is required).  
- NEEDS_MORE_EVIDENCE: ProductCode↔EMDN mapping rules, mapping of listing number ↔ EUDAMED device ID.

## Next actions recommended for 03_design_decisions.md
1. Decide representation patterns: role vs organization; reified event model template (required properties: actor, date, source, references to affected objects).  
2. Define identifier classes and minimal required properties (issuer, target class, scope, persistence).  
3. For NEEDS_MORE_EVIDENCE items, collect specific regulatory text (Annex VI, MDCG UDI guidance, EMDN documentation) as inputs.  

---

## Traceability note
All concept entries above cite the two source research files. Where additional legal detail is required the concept entry marks that as NEEDS_MORE_EVIDENCE and lists the specific research to fetch.



*End of 02_concepts.md draft.*