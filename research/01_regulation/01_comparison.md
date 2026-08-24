# Registration Comparison

Note: This comparison is based only on the two jurisdiction research artifacts listed below. All claims are traceable to those files and to the section headings they contain. No external regulatory sources were introduced or used to resolve semantic questions. Links point to the source research files in this workspace:

FDA research: research/01_registration/sources/01_FDA.md — see the sections referenced below (e.g., "2.6 Registration", "2.7 Device Listing", "2.25 UDI", "7. IDENTIFIERS").
MDR / IVDR research: research/01_registration/sources/02_MDR_IVDR.md — see the sections referenced below (e.g., "Concept: Device Registration", "Concept: SRN", "Concept: Basic UDI-DI", "3. Relationships").
Purpose

Provide a rigorous, evidence-driven, semantically-focused cross-jurisdiction comparison (FDA vs MDR/IVDR) to support subsequent ontology stages.
Identify shared concepts, related-but-different concepts, jurisdiction-specific concepts, lifecycle & relationship differences, identifier semantics, candidate abstractions, concepts that must remain jurisdiction-specific, unresolved questions, and modeling risks.
This document avoids any ontology design choices (OWL/ShACL) beyond high-level hypotheses.
Executive summary (brief)

Strong common ground: both jurisdictions distinguish (a) actor/role concepts (manufacturer, importer, distributor), (b) device/product definitions grounded in manufacturer-intended purpose, (c) device-identifiers/UDI constructs that separate device-level DI from production-level PI, and (d) regulatory information systems/registries (FDA: GUDID + listing/registration databases; EU: EUDAMED modules + SRN).
Critical semantic mismatches: FDA's "registration" (establishment registration) and "device listing" are operationally distinct and are NOT market authorizations; EU's registration mechanisms (device registration, economic operator registration, Basic UDI-DI, SRN) are also not equivalent to conformity assessment or CE marking. However, the EU also ties conformity assessment, notified-body certificates and CE marking into the market-access chain in a way that is structurally different from FDA (which uses 510(k)/PMA/De Novo/HDE/IDE pathways).
Modeling implication: several higher-level abstractions are plausible (RegulatoryActor, RegulatorySubmission, RegulatoryIdentifier), but many legal semantics are jurisdiction-specific and must remain separate slices in the ontology design layer.
Comparison approach and evidence discipline
The comparison below compares SEMANTIC MEANING, not mere terminology. For each candidate mapping the analysis explicitly answers: entity represented, regulatory role, creator/owner, interacting actors, creation/change/termination events, identifier semantics, authority, legal effect, object of regulation, and relationships.
Only evidence from the two source files above is used. Where the source files do not provide conclusive evidence, the comparison records "Insufficient evidence in the current source research." and marks the item UNRESOLVED or as requiring [EXTERNAL SOURCE REQUIRED] when further external legal interpretation would be needed.
Core concept-by-concept comparison (CATEGORY classification)
For each item in the A. Core Regulatory Concepts list from the brief, the table below classifies the relationship per the specified CATEGORY definitions (1–6) and provides evidence pointers.
Note: "FDA: <section>" and "EU: <section>" refer to the heading names in the source research files.

A. Core Regulatory Concepts

Candidate domain concept	FDA representation (evidence)	MDR/IVDR representation (evidence)	Classification (Category)	Rationale / Semantic assessment (traceable)
Establishment / Place of business	Concept: Establishment — defined as "place of business under one management" (FDA 2.1 Establishment; Registration section) ([FDA: 2.1 Establishment])	EU does not use the same "establishment" concept as the central registration construct; EU uses Economic Operator / Manufacturer / Actor Registration / SRN (see EU Actor / Economic Operator sections) ([EU: Concept: Economic Operator], [EU: Concept: SRN])	Category 2 — Related but not equivalent	FDA treats Establishment as a regulatory object to be registered (establishment registration, registration number). EU focuses on Economic Operator registration (SRN) rather than the "establishment" spatial/operational concept. Semantic difference: FDA's Establishment is a locational/operational object that is separately registered; EU emphasizes actor identity and SRN issuance by competent authority. (FDA: 2.6; EU: 2.3, 7)
Manufacturer	FDA: manufacturer appears as an activity/role within establishment framework, but source cautions Manufacturer ≠ Establishment (FDA 2.2, 6, 9)	EU: explicit "manufacturer" legal role (EU Concept: Manufacturer (MDR Art 2(30) etc.)) ([EU: Concept: Manufacturer])	Category 2 — Related but not equivalent	FDA's materials emphasize activities and owner/operator relationships (organization may have role ManufacturerRole and separately own Establishment). EU explicitly defines Manufacturer as role-bearing actor with statutory obligations (assign UDI, draw up DoC, place on market). The legal contours differ enough to prevent direct equivalence; potential shared abstraction (Organization + hasRole Manufacturer) but role semantics differ. (FDA: sections 2.1–2.6, 6; EU: Concept: Manufacturer)
Economic Operator	FDA: no explicit "economic operator" construct in source research; FDA uses Owner/Operator, Establishment, Labeler, Applicant (see FDA Actors 6)	EU: Economic Operator is explicit and enumerated (manufacturer, authorised representative, importer, distributor; MDR/IVDR differences noted) ([EU: Concept: Economic Operator])	Category 3 — Jurisdiction-specific concept (EU)	EU-specific legal construct; FDA research contains no direct mapping to an EU-style EconomicOperator concept. Therefore treat as jurisdiction-specific unless later abstraction is justified. (EU: Concept: Economic Operator; FDA: no direct counterpart — see "Insufficient evidence" below)
Registration (establishment)	Establishment Registration (FDA 2.6; registration lifecycle 5.1). Registration number, annual registration, update, 30-day rules.	EU: Economic Operator Registration / Device Registration (EUDAMED); separate SRN for economic operators; Basic UDI-DI/device registration (EU 2.3, 2.5)	Category 2 — Related but not equivalent	Both systems maintain registration records, but semantic scope differs: FDA registration is establishment-centric and operational (register an establishment and list devices). EU registration splits actor (SRN) and device (Basic UDI-DI/UDI/DeviceRegistration) and couples verification by competent authority before SRN issuance. Not equivalent. (FDA: 2.6, 5.1, 7; EU: Concept: SRN, Device Registration, Economic Operator Registration).
Listing (device listing)	Device Listing (FDA 2.7): device listing associated with establishments, listing number, listing lifecycle (create/update/discontinue/reactivate).	EU: Device registration in EUDAMED (Concept: Device Registration / Basic UDI-DI / UDI/DEV module).	Category 2 — Related but not equivalent	Both capture device-level registration records. Key differences: FDA device listing is a device listing tied to establishment and is operational under Part 807 with listing-number semantics; EU device registration is part of EUDAMED with Basic UDI-DI semantics and regulatory prerequisites for placing on market. They are similar objects (device-level registry) but differ in lifecycle and governance (e.g., EU Basic UDI-DI must be assigned before placing on market — EU Rule R02). (FDA: 2.7; EU: Concept: Device Registration, Basic UDI-DI, Rule R02).
Market Authorization / Approval / Clearance	FDA: multiple market-access pathways — 510(k) (SE→Clearance), PMA (Approval), De Novo (classification enabling marketing), HDE (humanitarian approval), IDE (investigational exemption) (see FDA sections 2.14–2.22, 8)	EU: MDR/IVDR do not prescribe a single "MarketAuthorization" object; market access results from conformity assessment, certificate, EU Declaration of Conformity, CE marking, and meeting MDR/IVDR requirements. (EU: Concept: Conformity Assessment; EU: Concept: CE Marking; EU: MQ01 / 9.1)	Category 2 — Related but not equivalent (STRUCTURAL DIFFERENCE)	FDA legal semantics center on submission-based regulatory decisions (SE/Clearance, PMA Approval). EU semantics center on conformity assessment + CE marking as manufacturer-based conformity claim, with notified-body certificates where applicable and EUDAMED records. Structurally different: FDA uses authority-issued decision tokens; EU relies more on manufacturer declarations supported by certificates/from notified bodies and competent-authority verification. (FDA: 2.17–2.19; EU: 2.3, 2.5, 2.9)
Submission / Application / Premarket Submission	FDA: clearly defined submission types with identifiers (510(k), PMA, De Novo, HDE, IDE; see FDA 2.14–2.23; FDA Premarket Submission Number 2.9)	EU: submissions occur (e.g., notified-body applications, certificates, device registration), but the role and objects differ (e.g., manufacturers apply to notified body; Basic UDI-DI assignment and EUDAMED registration before certain steps). The EU has certificates and conformity-assessment applications.	Category 2 — Related but not equivalent	Both have submission/application concepts, but FDA submits to FDA as a central authority leading to explicit agency decisions; EU submissions are often actions taken toward notified bodies / EUDAMED / competent authority verification, and many market-access effects are manufacturer-attested. (FDA: 2.14–2.20, 2.9; EU: Conformity Assessment, Notified Body, EUDAMED, Rule R03).
Certificate (regulatory certificate)	FDA: PMA approval exists; FDA issues approvals/clearances — but FDA does not use "Notified Body certificate" concept (FDA: PMA Approval 2.19, Clearance 2.17).	EU: Notified Body certificates are explicit (MDR Articles 56–57; IVDR Articles 51–52). Certificates have lifecycle (issue/amend/suspend/withdraw). (EU: Concept: Certificate).	Category 3 (jurisdiction-specific) / Category 2 (related concept)	Certificates as issued by notified bodies are EU-specific in the precise legal form and lifecycle. The concept of a regulatory decision or 'approval' exists in both, but the EU "certificate" structure (issued by notified body) is a distinct legal artifact without a direct FDA equivalent; treat as jurisdiction-specific artifact. (EU: Concept: Certificate; FDA: PMA approval/clearance are agency decisions, not the same artifact.)
Conformity Assessment / Notified Body / Competent Authority	FDA: FDA performs scientific/regulatory review for PMA/510(k); no concept of "Notified Body" (FDA uses review panels, FDA staff) (FDA: 2.18–2.20, 6).	EU: Conformity assessment is central; Notified Bodies are designated conformity assessment bodies with issuance of certificates; Competent Authorities verify registrations and issue SRNs. (EU: Concept: Conformity Assessment; Notified Body; SRN; Competent Authority)	Category 3 (notified body) and Category 2 for the higher-level notion of "assessor"	The concept of third-party designated conformity assessors (Notified Bodies) is EU-specific and has different semantics than FDA internal review processes. Higher-level mapping (assessment body / regulatory reviewer) may be possible, but semantics, designation authority, and roles differ. (EU: Concept: Notified Body; FDA: review processes described in PMA/510(k) sections)
Authorized Representative / Official Correspondent	FDA: concept of "Official Correspondent" appears (FDA Actors 6) and Owner/Operator; no statutory EU-style Authorized Representative concept in FDA.	EU: Authorised Representative is explicit; required for non-EU manufacturers with a written mandate. (EU: Concept: Authorised Representative)	Category 3 — Jurisdiction-specific (EU AR) and Category 2 (rough analogue)	EU AR is a formal EU-specific role with a written mandate; FDA has contacts/official correspondents but not the same statutory role. (EU: Concept: Authorised Representative; FDA: Actors 6, Official Correspondent)
Importer / Initial Importer	FDA: Importer and Initial Importer are distinct — "Initial Importer" defined specially (FDA 2.3, 2.4).	EU: Importer is defined as Union-established person placing device from third country on the market (EU Concept: Importer).	Category 1 — Direct common concept (Importer) with FDA-specific subrole (Initial Importer)	Both have Importer concepts with broadly overlapping semantic roles (placing imported devices on the market / handling import procedures). FDA additionally distinguishes "Initial Importer" (specific Part 807 definition). Ontology implication: model Importer as common concept with FDA-specific InitialImporter subtype/role. (FDA: 2.3–2.4; EU: Concept: Importer)
Distributor	FDA: Wholesale Distributor is referenced (Actors 6).	EU: Distributor is explicit (EU Concept: Distributor)	Category 1 — Direct common concept	Both jurisdictions define distributor roles with supply-chain responsibilities; semantics align sufficiently for a common concept, but regulatory obligations (CE checks, verifications) differ in specifics. (FDA: Actors 6; EU: Concept: Distributor)
Identifier (UDI, DI, PI, Product Code, SRN, Listing Number, Submission Numbers)	FDA: UDI (DI, PI) and GUDID; Product Code; listing numbers; establishment registration numbers; submission numbers (510(k), PMA, HDE) (FDA 2.25–2.28, 7)	EU: UDI (Basic UDI-DI, UDI-DI, UDI-PI), SRN for economic operators, EUDAMED registration records, EMDN codes (EU 2.5–2.8, 7)	Category 2 — Related but not equivalent (identifiers often have similar roles but different scopes/issuers)	Both systems have layered identifier systems (device-level DI / UDI, production PI, registry identifiers). Critical semantic differences: issuer and scope (e.g., SRN identifies economic operator and is issued by competent authority via EUDAMED in EU; FDA registration/listing numbers and GUDID are FDA-managed). Product Code (FDA) identifies a generic regulatory category and is distinct from DI. EU Basic UDI-DI semantics are not identical to FDA's ProductCode or listing numbers. (FDA: 2.25–2.28, 7; EU: Basic UDI-DI, SRN, 7)
Classification details (CATEGORY examples and reasoning)
CATEGORY 1 — DIRECT COMMON CONCEPT

Importer (both): FDA defines Importer & Initial Importer (distinct), EU defines Importer. Semantics: actor who places imported device on national/Union market. (FDA: 2.3–2.4; EU: Concept: Importer)
Distributor (both): defined as supply-chain actor; both specify verifications/obligations. (FDA: Actors; EU: Concept: Distributor)
CATEGORY 2 — RELATED BUT NOT EQUIVALENT

Establishment (FDA) vs Economic Operator / Economic Operator Registration (EU)

Similarity: both link actors to operational or identity records.
Critical difference: FDA Establishment is a place-of-business registration object with owner/operator responsibilities and listing ties; EU EconomicOperator is a role/actor identity (SRN) issued after competent-authority verification and EUDAMED registration. Ontology implication: do not conflate; consider common higher-level abstraction (RegulatoryActor or OrganizationRole) but maintain jurisdiction-specific substructures.
Evidence: [FDA: 2.1 Establishment], [EU: Concept: Economic Operator], [EU: Concept: SRN].
Device Listing (FDA) vs Device Registration (EU)

Similarity: registry entry describing devices in public/regulatory systems.
Critical difference: FDA device listing is associated with establishment(s) and listing numbers and lifecycle events like discontinuation/reactivation (FDA 2.7 and lifecycle); EU device registration uses Basic UDI-DI and EUDAMED device modules with assignment prerequisites and links to conformity assessment before placing on market. Ontology implication: model both as registry-record concepts with separate properties and lifecycle semantics. (FDA: 2.7; EU: Concept: Device Registration, Rule R02)
FDA Product Code vs EU EMDN / Device classification codes

Similarity: both serve to classify device categories.
Critical difference: ProductCode in FDA is an FDA-specific code identifying generic category (FDA: 2.8); EU EMDN is EU nomenclature used in EUDAMED (EU: 7 Identifiers). Do not equate without mapping rules.
FDA submission numbers (510(k) No., PMA No.) vs EU certificate identifiers / SRN

Similarity: identifiers for regulatory records.
Critical difference: assignment authority and the object identified differ (submission identifier vs certificate vs SRN). (FDA: 2.9, 7; EU: 7 Identifiers)
CATEGORY 3 — JURISDICTION-SPECIFIC

Notified Body (EU) — no direct FDA equivalent. (EU: Concept: Notified Body)
SRN (EU Single Registration Number for economic operators) — EU-specific; FDA has establishment registration numbers and listing numbers but no SRN concept or equivalent issuance procedure. (EU: Concept: SRN; FDA: 7 Identifiers)
EUDAMED — EU-specific modular regulatory information system; FDA analogs exist (GUDID, FDA databases) but EUDAMED's module structure and SRN issuance process are EU-specific. (EU: Concept: EUDAMED; FDA: 2.28 GUDID)
Authorised Representative (EU) — formal EU role (EU: Concept: Authorised Representative); no direct FDA-equivalent statutory role.
CATEGORY 4 — TERMINOLOGY DIFFERENCE

FDA "clearance" (SE determination → cleared) vs EU "CE marking"/"EU Declaration of Conformity"
FDA uses "cleared"/"approved"; EU uses "CE marking" / manufacturer declaration supported by certificates.
Semantic evidence: FDA 2.17 (Clearance), FDA explicitly distinguishes clearance vs approval; EU: CE Marking and EU Declaration of Conformity (EU: Concept: CE Marking, EU Declaration of Conformity).
Ontology implication: these terms must remain distinct at the jurisdiction layer; later consider a higher-level abstraction (RegulatoryAuthorizationArtifact) only if semantics align.
CATEGORY 5 — STRUCTURAL DIFFERENCE

FDA submission-oriented market access vs EU conformity-assessment + manufacturer-declaration model
Structural difference: FDA market access is often an agency-decision process (submission → review → agency decision), while EU market access is commonly: manufacturer assigns Basic UDI-DI → performs conformity assessment (possibly with Notified Body) → obtains certificate (if applicable) → issues EU Declaration of Conformity → affixes CE mark → places device on market; competent authorities verify actor registrations (SRN). (FDA: 5.2–5.6; EU: Event E04–E09; EU: Rule R02, R03, R04)
Modeling implication: lifecycle models must remain jurisdiction-specific; do not force one universal "submission→approval" model.
CATEGORY 6 — UNRESOLVED

Is "Device Listing Number" (FDA) semantically mappable to "EUDAMED Device Registration ID" or Basic UDI-DI? Evidence suggests device listing (FDA) and EUDAMED device registration are analogous in being device registry records, but semantics, issuance, prerequisites, and lifecycle behaviors differ. The source research does not provide sufficient evidence to assert equivalence. => UNRESOLVED: "Insufficient evidence in the current source research."
Is "Product Code" (FDA) equivalent to EU "EMDN code"? Insufficient evidence in the current source research to assert direct equivalence mapping rules. Mark as UNRESOLVED.
Cross-jurisdiction concept matrix (candidate domain concepts)
The matrix below summarizes candidate domain concepts, how they are represented in each source, relationship type (Category), semantic assessment and ontology implication (hypothesis-level).
Candidate Domain Concept	FDA representation	MDR/IVDR representation	Relationship Type (Category)	Semantic Assessment	Ontology Implication
Establishment / Place of Business	Establishment (place of business) — registration, establishment registration number (FDA 2.1, 2.6)	EU: actor-centric SRN / economic operator registration (EU: SRN, EconomicOperator)	2	Related: Both associate identity & registration info with actors/locations but EPA semantics differ (establishment vs economic operator).	likely common abstraction: OrganizationRole / OperationalSite, but keep jurisdiction-specific subclasses (fda:Establishment, eu:EconomicOperatorRegistrationSite)
Manufacturer (role)	Role/activity; separate from Establishment; performs manufacturing activities (FDA 2.2, 6)	Explicit legal role with duties (assign UDI, place on market, DoC) (EU: Concept: Manufacturer)	2	Similar purpose (responsible for device) but regulatory obligations differ (e.g., assignment of Basic UDI-DI and DoC in EU).	likely common abstraction: ManufacturerRole; model jurisdiction-specific obligations as properties/events
Device / Medical Device	Device concept used by FDA; classification into Classes (FDA 2.10)	Medical Device (MDR Article 2) and IVD (IVDR) with intended purpose definitions (EU: Concept: Medical Device, InVitroDiagnosticDevice)	1	Direct common concept: both define device based on intended purpose.	likely common concept: RegulatedDevice / Device, with jurisdiction-specific classification properties
Device listing / Device registration	Device Listing (FDA listing number, lifecycle) (FDA 2.7)	Device Registration / Basic UDI-DI / EUDAMED device module (EU Device Registration)	2	Related: registry records for devices, but different data, prerequisites, and governance.	requires separate concepts (fda:DeviceListing, eu:DeviceRegistration) with possible common superclass RegistryRecord
Registration (actor)	Establishment Registration (FDA 2.6)	Economic Operator Registration (EU Article 31/28 + SRN)	2	Both register actors but different focus/authority workflows.	possible common abstraction: RegistrationRecord; keep distinct subtypes and verification processes
Submission / Premarket Submission	510(k), PMA, De Novo, HDE, IDE (FDA 2.14–2.22)	Notified-body application & conformity-assessment applications; EUDAMED registrations (EU: Conformity Assessment/Notified Body sections)	2	Both have submission-like actions, but FDA central submission → agency decision; EU submission often to notified body/EUDAMED with manufacturer-driven outcome.	keep separate: fda:PremarketSubmission vs eu:ConformityAssessmentApplication; possible common abstraction: RegulatorySubmission
Conformity Assessment / Notified Body	FDA: not structured as "Notified Body" (agency review exists)	EU: Notified Body designated to perform conformity assessment, issue certificate (EU: Concept: Notified Body, 3.1)	3	Jurisdiction-specific: NotifiedBody is EU-specific statutory designation.	remain EU-specific; higher-level abstraction (AssessorBody) possible but with low confidence
CE Marking / Clearance / Approval	FDA: Clearance (510(k): SE→cleared); Approval (PMA) — agency decisions (FDA 2.17,2.19)	EU: CE Marking (manufacturer affixation), EU Declaration of Conformity, certificates (EU: CE Marking, EU Declaration, Certificate)	4 (terminology & semantic difference)	Not synonymous: "cleared/approved" implies agency decision; CE marking is manufacturer-conferred evidence of conformity usually supported by certificate.	Do not conflate; consider an abstract "RegulatoryMarketAccessIndicator" with jurisdiction-specific subtypes
UDI / DI / PI / GUDID / Basic UDI-DI	UDI, DI (identifies labeler + model), PI (production info), GUDID holds DI records (FDA 2.25–2.28)	UDI, Basic UDI-DI, UDI-DI, UDI-PI, EUDAMED UDI/DEV module (EU: 2.5–2.7, 7)	1 (common concept family)	Strongly aligned semantics: both separate DI (device/model) from PI (production) and have regulatory registries. Differences: Basic UDI-DI semantics (EU) and registry flows differ.	Candidate common abstraction: RegulatoryDeviceIdentifier with jurisdiction-specific subclasses (confidence: HIGH for separation DI vs PI; MEDIUM for Basic UDI-DI semantics mapping)
SRN / Listing Number / Establishment Registration Number	FDA: Listing Number, Establishment Registration Number (FDA 2.7, 7)	EU: SRN identifies economic operator, issued by competent authority via EUDAMED (EU: Concept: SRN)	2	Similar role-as-identifier, but different target (economic operator vs device listing/establishment).	treat as distinct identifier classes; possible common abstraction RegulatoryIdentifier but preserve semantics and issuer/target
Notified Body Certificate vs PMA Approval	FDA issues PMA approvals — agency decisions	EU Notified Body issues certificates; manufacturer issues DoC and affixes CE mark	3 (structural difference)	Certificates (EU) are artifacts of a designated third-party assessment. PMA approvals (FDA) are direct agency authorizations. Not interchangeable.	Keep distinct and jurisdiction-specific; consider abstract Certificate/Authorization class with separate properties for issuer type and legal effect
Actor comparison matrix (only actors supported in source research)
Regulatory Actor	FDA (source & semantics)	MDR/IVDR (source & semantics)	Semantic relationship	Modeling implication
Manufacturer	Role/activity; organization may have ManufacturerRole; manufacturing activity may be performed at Establishment (FDA: 2.2, 6)	Explicit role-bearing economic operator with statutory duties (assign UDI, DoC, place on market) (EU: Concept: Manufacturer)	Related but semantically different emphasis: FDA separates activity & establishment, EU treats manufacturer as legal actor with clear obligations.	Model Manufacturer as a role on an Organization; preserve jurisdiction-specific obligations/events (fda:manufacturingActivity vs eu:assignsBasicUDIDI, eu:drawsUpEUDeclarationOfConformity).
Establishment / Site	FDA: primary regulated object for registration (place of business) (FDA: 2.1, 2.6)	EU: not the central registration object; EU focuses on EconomicOperator and device records, though Member State-level registration may still reference sites — EU research primarily centers on actors and EUDAMED SRN (EU: 7).	Related but different focal point	Keep Establishment distinct and maintain that EU models may require linking economic operator to place(s) of business; avoid equating Establishment = Manufacturer.
Owner/Operator / Official Correspondent	FDA: Owner/Operator (responsible entity); Official Correspondent as designated FDA contact (FDA: Actors 6)	EU: no identical concept; Authorised Representative exists for non-EU manufacturers (EU: Concept: Authorised Representative)	Not equivalent	Maintain separate roles; map to a common "RegulatoryActor" abstraction only at higher level.
Authorized Representative	FDA: not a statutory EU-style AR (no equivalent in FDA research)	EU: defined role for non-EU manufacturers with written mandate (EU: Concept: Authorised Representative)	Category 3 — Jurisdiction-specific (EU)	Treat as EU-specific role. For cross-jurisdiction modeling, represent as an optional role with EU-specific constraints.
Importer	FDA: Importer and Initial Importer are distinct (Part 807) (FDA: 2.3–2.4)	EU: Importer is Union-established actor placing third-country devices on market (EU: Concept: Importer)	Category 1 — Direct common concept with FDA-specific subrole	Common concept Importer with FDA InitialImporter as a jurisdiction-specific subclass/role.
Distributor	FDA: Wholesale Distributor referenced (Actors 6)	EU: Distributor defined by supply-chain activity and obligations (EU: Concept: Distributor)	Category 1 — Direct common concept	Common class Distributor with jurisdiction-specific verification obligations.
Notified Body / Conformity Assessor	FDA: no Notified Body concept; FDA uses internal review and advisory panels	EU: Notified Body is a designated conformity-assessment body with certificate lifecycle (EU: Concept: Notified Body)	Category 3 — Jurisdiction-specific	Represent NotifiedBody as EU-specific class; consider a high-level AssessorBody abstraction but only if semantics and authority models are preserved.
Competent Authority / FDA	FDA: FDA is regulatory authority; issues approvals/clearances (FDA: 6, 8)	EU: Competent Authorities are Member State bodies responsible for verification, SRN issuance, monitoring; they play a gatekeeping role in EUDAMED flows (EU: 3.1, Actors)	Category 2 — Similar role (regulatory authority) but different distribution	Represent RegulatoryAuthority as common abstraction with jurisdiction-specific properties (fda:FDA vs eu:CompetentAuthority).
Lifecycle comparison
Approach: describe each jurisdiction lifecycle conceptual chain(s) and then compare commonalities/differences.
A. FDA (summary lifecycle fragments — evidence: FDA sections 5.x)

Establishment registration lifecycle (FDA 5.1)
Event: EstablishmentRegistration → RegistrationUpdate → AnnualRegistrationReview → possible Failure
Regulatory object: Establishment. Outcome: Establishment registration record / registration number (FDA 2.6, 5.1)
Device listing lifecycle (FDA 5.2)
Event: DeviceListingCreation → DeviceListingUpdate → DeviceListingDiscontinuation → DeviceListingReactivation
Regulatory object: DeviceListing record; Outcome: listing number, active/discontinued listing (FDA 2.7, 5.2)
Premarket submission pathways (FDA 5.3–5.6; 2.14–2.22)
510(k) lifecycle: 510kSubmission → 510kReview → SEDetermination (SE/NSE) → 510kClearance (if SE)
PMA lifecycle: PMASubmission → PMAReview → PMAApproval / Denial / Withdrawal
De Novo lifecycle: DeNovoRequest → DeNovoReview → DeNovoGrant / Decline → classification result
IDE/HDE lifecycle: IDE approval authorizes investigation (investigational exemption) vs HDE/HUD pathways
Identifiers & registries: GUDID holds DI records; listing numbers and submission numbers track regulatory records (FDA 2.28, 7).
B. MDR / IVDR (summary lifecycle fragments — evidence: EU events E04–E11, Rules R01–R06)

Economic operator registration lifecycle
Event: EconomicOperatorRegistrationSubmission → CompetentAuthorityVerification → SRNIssuance → periodic confirmation / data updates (EU Rule R04, Event E01–E03)
Basic UDI-DI and device registration
Event: Basic UDI-DI Assignment (E04) → DeviceRegistrationSubmission to EUDAMED (E05) → device registration record stored; Basic UDI-DI required before placing on market in many routes (Rule R02, R03)
Conformity assessment & certificate lifecycle
Event: ConformityAssessmentPerformed (E06) often involving NotifiedBody → CertificateIssuance (E07) → certificate lifecycle: amendment / suspension / withdrawal (Event E13; Rules).
Market placement lifecycle
CE Marking (E08 — manufacturer affixes) → PlacingOnMarket (first making available) (E09) → MakingAvailable (supply events) (E10) → PuttingIntoService (E11)
Registries & systems: EUDAMED modules (actor, UDI/device registration, notified bodies/certificates) underpin these outcomes.
C. Comparison: shared lifecycle concepts and structural differences

Shared lifecycle concepts (high-level)
Registration/registry records exist in both jurisdictions (actor/establishment & device).
Device identification (UDI DI / PI) and registry records are present in both.
There are lifecycle events for creating/updating/withdrawing registry records.
Structural differences (key)
FDA: separates EstablishmentRegistration (site) from DeviceListing (device), with submissions to FDA (510(k), PMA) producing authority-issued decisions that explicitly enable marketing (clearance/approval).
EU: separates EconomicOperatorRegistration (SRN) from DeviceRegistration (Basic UDI-DI/UDI) and places conformity assessment (sometimes third-party Notified Body) and EU Declaration / CE marking in the center of market access. The manufacturer’s act (DoC + affix CE) is central to placing on the market; competent authorities verify actor registrations and may issue SRNs.
Modeling implication: lifecycle models should remain jurisdiction-specific: FDA lifecycle model is submission→agency-decision oriented while EU model is conformity-assessment→manufacturer-declaration oriented.
Identifier comparison (dedicated table)
For every identifier referenced in the sources:
Identifier	Jurisdiction	Identifies	Issued By	Scope	Lifecycle behavior	Potential ontology role
Establishment Registration Number	FDA	Establishment registration record (place-of-business)	FDA	Jurisdiction-specific (US)	Created at registration; updated/renewed annually; may be associated with failed-to-register states (FDA 2.6; 5.1)	fda:EstablishmentRegistrationIdentifier (registration-record identifier)
Listing Number	FDA	Device listing record	FDA	Jurisdiction-specific	Created on device listing; can be discontinued/reactivated (FDA 2.7; Rule R06/R07)	fda:DeviceListingIdentifier
Product Code	FDA	Generic regulatory category (FDA’s product classification code)	FDA	Regulatory classification/code	Stable identifier of device category; not a model-level DI (FDA 2.8)	fda:ProductCode (classification identifier)
FDA Premarket Submission Number (510(k), PMA, HDE, De Novo)	FDA	A premarket submission record	FDA	Submission-level identifier	Assigned to each submission; persists as record identifier (FDA 2.9, 7)	fda:PremarketSubmissionIdentifier
UDI — DI (Device Identifier)	FDA	Identifies labeler + specific version/model	Issuing agency based on HIBCC/GS1/ICCBBA conventions; submitted to GUDID	Device-model level (US / global if harmonized)	DI is stable for model/version; submitted to GUDID (FDA 2.25–2.28)	fda:DeviceIdentifier (DI)
UDI — PI (Production Identifier)	FDA	Lot/serial/manufacturing/expiration production data	Labeler / manufacturer	Production-level	Variable per production event (FDA 2.27)	fda:ProductionIdentifier (PI)
GUDID record	FDA	DI registry record / device identification metadata	FDA (database)	US national database (public reference)	Created/updated by labeler; contains DI-level data (FDA 2.28)	fda:GUDIDRecord
Basic UDI-DI	EU	Device grouping / regulatory grouping identifier (pre-assigned before placing on market)	Manufacturer (assigned per Annex VI rules) + provided to EUDAMED	EU-specific device-grouping identifier	Must be assigned before placing on market in many routes; submitted to EUDAMED (EU: Rule R02, E04)	eu:BasicUDIDI (device-grouping identifier)
UDI-DI	EU	Device identifier (device-model level)	Manufacturer via issuing entity	Device-level identifier	Submitted to UDI database / EUDAMED (EU: UDI sections)	eu:UDIDI
UDI-PI	EU	Production identifier (lot/serial/info)	Manufacturer	Production-level	Variable per production batch/serial (EU: Annex VI)	eu:UDIPI
Single Registration Number (SRN)	EU	Economic operator (actor) identifier	Competent Authority via EUDAMED	EU-wide (Union) unique identifier for economic operators	Issued after competent-authority verification; used in actor registration lifecycle (EU: Concept: SRN, Event E03)	eu:SRN
EUDAMED registration record / EUDAMED module identifiers	EU	Device / actor / notified body / certificate records	EUDAMED system / competent authority	EU (Union) wide	Created/updated with registration events and verification; module-specific lifecycle (EU: Concept: EUDAMED)	eu:EUDAMEDRecord / eu:EUDAMEDModuleIdentifier
Important identifier semantic notes:

Do not conflate ProductCode (FDA) with DI/Basic UDI-DI (EU). FDA ProductCode identifies a generic regulatory category (FDA 2.8); DI identifies specific model/labeler.
SRN (EU) is an economic-operator identifier and must not be treated as a device identifier.
Device identifiers (DI / UDI-DI) and production identifiers (PI / UDI-PI) represent different semantic layers in both jurisdictions and should be modeled distinctly (confidence HIGH per both sources).
Regulatory relationships: cross-jurisdiction assessment
Common relationship patterns present in both sources (but with jurisdictional differences in semantics):
Manufacturer → manufactures → Device (FDA: inferred relationships; EU: 3.1)
Organization/Owner → registers → Establishment (FDA) vs EconomicOperator → registers → SRN (EU): similar shape but different object of registration (Category 2).
Device → hasIdentifier → DI / UDI (both): direct equivalence in concept family (Category 1).
Device → undergoes → ConformityAssessment (EU) vs Device → undergoes → PremarketSubmission/Review (FDA): both are assessment events but differ in performer and legal effect (Category 2 / Structural difference).
Submission → RegulatoryAuthority → Decision (FDA) vs Manufacturer + Notified Body → Conformity → Certificate/DoC → MarketAccess (EU): structurally different chains (Category 5).
Relationship-level modeling implication: many relationships should be reified as regulatory events/determinations (e.g., SEDetermination, ConformityAssessmentPerformed) rather than simple binary object-to-object edges.
Regulatory status semantics
Be very cautious: words like "registered", "listed", "approved", "cleared", "certified", "CE marked" have jurisdiction-dependent legal meaning. Examples from the sources:
FDA: "cleared" corresponds to SE decision for 510(k). PMA leads to "approval." (FDA: 2.17, 2.19)
EU: "CE marking" is the manufacturer's indication of conformity; "certificate" can be issued by a Notified Body. Certification does not automatically equate to "approval" as in FDA. (EU: CE Marking, Certificate sections)
Ontology implication: treat regulatory status as jurisdiction-layered state models; do not collapse into a single universal "approved" state.
Key semantic differences (prioritized)
Registration vs Listing vs Device Registration:
FDA: Establishment registration and device listing are separate and operational; device listing is not a market authorization (FDA: 2.6–2.7).
EU: Device registration (Basic UDI-DI, EUDAMED) is a precondition in many paths to market, but is not equivalent to conformity assessment / CE marking / market authorization (EU: Device Registration, Rule R02).
Modeling risk: conflating "registration" with "market authorization".
Approval vs Clearance vs Certification vs CE marking:
FDA: "Approval" (PMA) is an agency-granted authorization; "Clearance" (SE) is an FDA decision language for 510(k).
EU: CE marking is a manufacturer-attested sign of conformity; certificates are issued by Notified Bodies in certain routes.
Modeling risk: treating all as equivalent to a single authorization token.
Manufacturer vs Economic Operator vs Establishment:
FDA separates establishment (place) from owner/operator and manufacturing activity; EU treats manufacturer as actor with explicit obligations and introduces EconomicOperator concept.
Modeling risk: assuming roles are static organization types rather than role-bearing relationships that can change with intended-purpose changes (EU Rule R09).
Notified Body vs FDA reviewer:
Notified Body is a designated third-party assessment entity in EU law; FDA reviews are agency internal processes.
Modeling risk: modeling assessor bodies as identical across jurisdictions without encoding designation/authority differences.
Candidate cross-jurisdiction abstractions (hypotheses)
For each candidate abstraction include: common semantic meaning, evidence from FDA, evidence from EU, differences, confidence, further research required.
RegulatoryActor (confidence: HIGH)
Common semantic meaning: an actor (natural or legal person) participating in regulated activities (manufacture, import, distribution, submission).
Evidence (FDA): Actors list (Owner/Operator, ManufacturerRole, Importer, Sponsor) and model notes about roles (FDA 6).
Evidence (EU): EconomicOperator, Manufacturer, AuthorisedRepresentative, Importer, Distributor (EU 6).
Differences: EU has specific Actor registration with SRN and EU-authorised representative role; FDA emphasizes establishment ownership and activity roles. Performer semantics and mandatory registration flows differ.
Further research required: mapping of "Owner/Operator" to EU "Manufacturer" or "EconomicOperator" in cases where a manufacturer has multiple establishments.
RegulatoryIdentifier (confidence: HIGH)
Common semantic meaning: an identifier assigned to a regulatory object (actor, device, submission, certificate).
Evidence (FDA): Establishment registration number, listing number, submission numbers, DI/PI, GUDID (FDA 7).
Evidence (EU): SRN, Basic UDI-DI, UDI-DI, UDI-PI, EUDAMED registration identifiers (EU 7).
Differences: issuer and target differences (e.g., SRN identifies economic operator and is issued by competent authority; Basic UDI-DI is assigned by manufacturer but provided to EUDAMED).
Further research: alignment rules to map identifier classes to ontology identifier type (submission vs device vs actor vs certificate).
RegulatorySubmission / RegulatoryDecision (confidence: MEDIUM)
Common semantic meaning: a submission/request to a regulatory system and its decision/outcome.
Evidence (FDA): PMA, 510(k), De Novo, HDE, IDE with explicit submission numbers and decision semantics (FDA 2.14–2.22).
Evidence (EU): ConformityAssessmentApplication / NotifiedBody interactions; certificates / DoC; EUDAMED registration flows (EU: ConformityAssessment, Certificate, DoC).
Differences: FDA decisions are agency-issued approvals/clearances; EU outcomes are often certificates/DoC with manufacturer declaration and varying third-party involvement.
Further research: clear mapping of "decision" semantics across jurisdictions and how to model reified decisions (who issues versus who signs).
Registry / RegulatoryInformationSystem (confidence: HIGH)
Common semantic meaning: a database or module holding authoritative regulatory records (device, actor, certificate).
Evidence (FDA): GUDID + FDA product/510(k)/PMA databases (FDA 2.28, 1.2 S16–S19).
Evidence (EU): EUDAMED modular system (EU: Concept: EUDAMED).
Differences: EUDAMED is explicitly modular and includes SRN issuance workflow; GUDID is primarily DI registry and FDA maintains several separate public databases.
Further research: determine mapping patterns and shared properties for registry records (createdBy, issuedBy, verifiedBy).
Concepts that MUST remain jurisdiction-specific (with reasons and risks)
Notified Body (EU)
Jurisdiction: EU
Reason: statutory designation and role for conformity assessment; no FDA analog in legal form.
Risk of merging: losing the semantics of third-party designation and certificate lifecycle.
SRN (Single Registration Number)
Jurisdiction: EU
Reason: EU-wide economic operator identifier issued after competent-authority verification.
Risk: conflation with FDA establishment registration number or listing number would obscure issuer/verification semantics.
CE Marking and EU Declaration of Conformity (EU)
Jurisdiction: EU
Reason: manufacturer-driven declaration with legal meaning under MDR/IVDR; not equivalent to FDA approvals.
Risk: modeling as generic "approval" would hide who asserts versus who grants.
EUDAMED module semantics (EU)
Jurisdiction: EU
Reason: modular DB with SRN issuance workflow and specific regulatory preconditions.
Risk: mis-modeling EUDAMED as a simple database would lose lifecycle and verification semantics.
Ontology modeling risks identified by comparison
False equivalence: equating "registration" with "market authorization" (both FDA and EU sources warn against it).
Terminology collision: terms that look similar (e.g., "registration", "listing", "certificate", "approval") have different jurisdictional legal meanings.
Lifecycle mismatch: assuming submission→approval model for both jurisdictions risks incorrectly modeling EU manufacturer-centered flows.
Actor-role mismatch: conflating Manufacturer (EU role) with Establishment (FDA site) or Applicant/Owner could cause incorrect property attributions.
Identifier conflation: collapsing DI, PI, ProductCode, SRN, submission numbers into a single "Identifier" class will lose crucial semantics.
Overly generic classes: creating a single MarketAuthorization class without encoding jurisdictional difference risks incorrect inferences.
Incorrectly shared properties: assuming the same "issuer" semantics (who issues an identifier or certificate) across jurisdictions will be wrong.
Reified relationships lost: failing to reify determinations (e.g., SEDetermination, ConformityAssessmentOutcome) will lose context like who made the determination, when, and which submission it referred to.
Unresolved semantic questions (must be resolved before ontology modeling)
Is FDA Device Listing Number semantically equivalent to EUDAMED Device Registration ID or to Basic UDI-DI? — Insufficient evidence in the current source research.
Can Product Code (FDA) be mapped to EMDN (EU) with a deterministic rule or is mapping context-dependent? — Insufficient evidence in the current source research.
How should the "authority vs manufacturer" split of market access be modeled: (a) Decision/authorization issued by authority (FDA), and (b) Manufacturer-conferred CE marking supported by certificate (EU)? Should they be separate classes or subtypes of a common abstraction? — Open (modeling question).
How to represent an actor who assumes manufacturer obligations in EU after changing intended purpose (EU Rule R09)? Is that a role change event or a creation of a new legal obligation object? — Needs design decision; sources document the behavior but not an ontology pattern.
For UDI Basic UDI-DI: does it identify a device family, a regulatory grouping, or a model? EU sources indicate it's not equal to physical device; deeper Annex VI analysis required. — [EXTERNAL SOURCE REQUIRED] (Annex VI ++ MDCG UDI guidance).
Mapping Notified Body certificate lifecycle semantics into model states: suspension, restriction, invalidity — how best to represent temporal validity and regulatory consequences across jurisdictions? — Modeling question; more detailed requirements analysis needed.
Concepts requiring special modeling treatment (candidate list)
Reified Determinations/Decisions: SEDetermination, PMAApproval, DeNovoDecision, ConformityAssessmentOutcome. These should be explicitly modeled as reified events/records (supported by FDA reification signals and EU certificate artifacts).
Identifier classes: preserve separate classes for SubmissionIdentifier, RegistrationIdentifier (establishment/listing), DeviceIdentifier (DI / UDI-DI), ProductionIdentifier (PI / UDI-PI), EconomicOperatorIdentifier (SRN), CertificateIdentifier.
Registry / System classes: GUDID vs EUDAMED are regulatory information systems and should be modeled as such (database/system → records).
Actor roles vs organizations: model roles (ManufacturerRole, AuthorizedRepresentative, InitialImporter) as roles that organizations can bear, not as static organization subclasses.
Open questions for next stage (prioritized)
Q1. Should a cross-jurisdiction abstraction "RegulatoryIdentifier" be introduced at the concept layer, or should identifiers be left as jurisdiction-layered only? (affects mapping and data ingestion)
Q2. For cross-jurisdiction device identity: is the common abstraction "DeviceModel" (identified by DI/UDI-DI) sufficient, or is an additional "DeviceGrouping" (Basic UDI-DI) required? (EU Basic UDI semantics need clarification)
Q3. How to represent authority-issued vs manufacturer-declared market-access artifacts as separate classes with explicit issuer roles?
Q4. How to represent establishment vs economic operator: as two distinct classes linked by role and place, or as an abstraction with jurisdiction-specific projections?
Q5. For status modeling: should lifecycle state be an explicit event/state resource with timestamps and provenance rather than a property value on device/actor records?
Q6. What minimal set of reified events (with required properties) is necessary to preserve legal semantics across both jurisdictions (e.g., submission event, decision event, registration event, conformity assessment event, certificate event)?
Final synthesis — Comparison Conclusions
Major common concepts (safe to treat as shared at the abstraction level, with care):
Device (medical device) defined by manufacturer-intended purpose (FDA: device concept; EU: MedicalDevice/IVD). Evidence supports a shared Device abstraction (confidence: HIGH).
UDI family (DI vs PI) — both jurisdictions separate device identifier vs production identifier and require registry records (confidence: HIGH).
Basic modeling primitives: RegulatoryActor / OrganizationRole, Registry/Database, Submission/Decision as patterns are present in both jurisdictions (confidence: MEDIUM–HIGH) but must be specialized per jurisdiction.
Importer and Distributor roles map closely across both jurisdictions (confidence: HIGH).
Major jurisdiction-specific concepts (must remain separate in the source layer):
EU: EUDAMED (module architecture), SRN (economic-operator ID), Notified Body designation and certificate model, EU Declaration of Conformity, CE marking semantics (confidence: HIGH).
US: FDA-specific Establishment concept and Part 807 device listing flows, 510(k) / PMA / De Novo / HDE / IDE submission semantics and the FDA-centric submission/decision model (confidence: HIGH).
Major semantic mismatches:
Market-access structure: FDA agency-decision-centric (submissions → agency decisions) vs EU manufacturer-declaration + conformity assessment (with Notified Body certificates where needed) (structural difference).
Identity/registration focus: FDA establishment and device listing records vs EU actor (SRN) + Basic UDI-DI device registration.
Issuer semantics: who assigns/authorizes identifiers and who issues the enabling artifact (FDA vs EU difference).
Candidate common abstractions:
RegulatoryActor, RegulatoryIdentifier, RegulatorySubmission, RegulatoryInformationSystem are plausible cross-jurisdiction abstractions. Each requires careful property-level specialization (issuer, legal effect, authority vs manufacturer issuer) (confidence: MEDIUM).
Concepts requiring separate treatment:
NotifiedBodyCertificate vs PMAApproval vs 510(k) Clearance/Decision should remain separate concepts at the jurisdiction layer; any common abstraction must preserve issuer semantics (confidence: HIGH).
SRN and EstablishmentRegistrationNumber must remain distinct identifier classes with different targets and issuance semantics.
Unresolved questions (must be resolved before 02_concepts.md):
Equivalence or mapping rules for device-listing/listing-number (FDA) vs EUDAMED device registration IDs / Basic UDI-DI (EU). (Insufficient evidence in the current source research.)
ProductCode ↔ EMDN mapping semantics and mapping strategy (Insufficient evidence in current research).
Exact semantics of Basic UDI-DI (device family vs regulatory grouping) — Annex VI and MDCG UDI guidance are needed. [EXTERNAL SOURCE REQUIRED]
Closing guidance for next stage (02_concepts.md)

Start 02_concepts.md with separate jurisdiction-layer slices that preserve the following distinctions:
FDA-layer: Establishment (site) vs Owner/Operator vs DeviceListing vs PremarketSubmission types and their decision outcomes (Clearance/Approval).
EU-layer: EconomicOperator/SRN, Basic UDI-DI/UDI-DI/UDI-PI, EUDAMED modules, NotifiedBodyCertificate and CE marking, and conformity-assessment flows.
Define candidate cross-jurisdiction abstractions (RegulatoryActor, RegulatoryIdentifier, RegulatorySubmission, Registry) as hypotheses and enumerate required jurisdictional properties (issuer, authority type, legal effect, lifecycle events) before attempting to assert equivalence or superclass/subclass links.
Preserve reified events and decisions (SEDetermination, ConformityAssessmentOutcome, CertificateIssuance) as first-class modeling objects because they carry provenance and legal-effect semantics required to avoid false equivalence.
Research artifacts used (traceability)

FDA source research: research/01_registration/sources/01_FDA.md. See especially sections: 2.1 Establishment, 2.6 Registration, 2.7 Device Listing, 2.14–2.22 (submissions), 2.25–2.28 (UDI/GUDID), 3 Relationships, 5 Lifecycle events, 7 Identifiers.
EU source research: research/01_registration/sources/02_MDR_IVDR.md. See especially: Concept: Device Registration / Basic UDI-DI (Article 29/26), Concept: SRN / Economic Operator (Articles 30–31 / 27–28), Concept: Conformity Assessment, Notified Body, CE Marking, EUDAMED, Lifecycle events E04–E11.
Final verification checklist (what this comparison satisfies)

Compared FDA and MDR/IVDR semantically, not just terminologically — each mapping includes authority, creation/change events, issuer, actor roles, and legal effect.
Distinguished common concepts from merely similar ones; documented jurisdiction-specific concepts.
Analyzed lifecycle differences and actor-role differences.
Identified and separated identifier semantics.
Documented key semantic mismatches and modeling risks (false equivalence, identifier conflation, lifecycle mismatch).
Produced candidate abstractions as modeling hypotheses (not OWL/SHACL).
Listed unresolved questions and flagged areas that require [EXTERNAL SOURCE REQUIRED] or further legal-text-level evidence.
All major claims are traceable to the two source research files above; where evidence is insufficient the text explicitly states so.
Next steps (suggested)

Use this comparison as input to 02_concepts.md: convert the candidate abstractions, per-jurisdiction classes, and event reifications into a prioritized concept list.
For unresolved questions marked [EXTERNAL SOURCE REQUIRED], collect the specific regulatory texts (e.g., Annex VI for Basic UDI-DI details; EMDN documentation; mapping guidance) before attempting cross-jurisdiction equivalence.
In 03_design_decisions.md explicitly encode which concepts remain jurisdiction-specific and the minimal common abstractions to support cross-jurisdiction reasoning without losing legal semantics.