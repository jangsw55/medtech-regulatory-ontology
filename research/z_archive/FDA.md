# FDA Medical Device Regulatory Ontology — Concept Extraction
 
Scope: Establishment Registration, Device Listing, Premarket Notification (510(k)), Premarket Approval (PMA), Manufacturer, Regulatory Authority, Device Identification (UDI), Market Authorization Lifecycle.
 
*Revision note (v2): corrects citation-length and duplicate-quote issues from the first draft, fixes a mislabeled source reference, adds a previously-missing Class III→PMA rule, resolves a naming inconsistency between the relationship diagram and the concept sections, and flags Humanitarian Device Exemption (HDE) as an under-sourced concept.*
 
*Revision note (v3): re-verifies §2.1–§2.6 (Manufacturer/Owner-Operator, Initial Importer, Wholesale Distributor, Establishment, Establishment Registration, Device Listing) word-for-word against primary eCFR text after a paraphrase error was caught by direct comparison to the FDA source. Corrections: (1) the Initial Importer definition was missing its repackaging/relabeling proviso and had an invented clause substituted in its place — fixed; (2) the "failed to register / failed to list" status text was mis-cited to §807.25 — it is actually §807.22(c); (3) a previously-uncaptured exemption rule (§807.20(c): wholesale distributors who don't manufacture/repackage/process/relabel are exempt from registration entirely) has been added as Rule R11; (4) the device-listing premarket-submission-number requirement is now cited to its actual source (an FDA program page, not confirmed primary CFR text) and a fifth premarket pathway, PDP (Product Development Protocol), has been added; (5) the Official Correspondent role's framing as foreign-establishment-specific has been corrected — it is a general Part 807 role; (6) the annual renewal cycle (Oct 1–Dec 31, §807.22(b)(1)) is now confirmed rather than flagged as inferred. §2.8–§2.17 (classification, 510(k), PMA, UDI/GUDID) have NOT yet been re-verified against primary text in this pass and should be treated with the same caution the v1→v2 correction implies — see updated Gaps section.*
 
---
 
## 1. Source Documents
 
| # | Document Title | Issuing Organization | URL | Date | Section/Reference |
|---|---|---|---|---|---|
| S1 | 21 CFR Part 807 — Establishment Registration and Device Listing for Manufacturers and Initial Importers of Devices | FDA / eCFR (Office of the Federal Register, NARA) | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807 | As codified in eCFR, current version; originally 42 FR 42526, Aug. 23, 1977 | Subparts A (§807.3), B (§§807.20–807.39), E (510(k) procedures) |
| S2 | 21 CFR § 807.3 — Definitions | FDA / eCFR | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-A/section-807.3 | Current eCFR version | Owner/operator, initial importer, official correspondent, wholesale distributor definitions |
| S3 | 21 CFR § 807.20 — Who must register and submit a device list? | FDA / eCFR | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807/subpart-B/section-807.20 | Current eCFR version | Registration obligation scope |
| S4 | 21 CFR § 807.40 — Establishment registration and device listing for foreign establishments | Cornell LII (mirrors eCFR) | https://www.law.cornell.edu/cfr/text/21/807.40 | Current | Foreign establishment obligations, official correspondent role |
| S5 | Premarket Notification 510(k) (program landing page) | FDA / CDRH | https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k | Page last reviewed 08/22/2024 | Definition of 510(k); statutory basis section 513(i)(1)(A) FD&C Act |
| S6 | 510(k) Submission Process | FDA / CDRH | https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process | current | Review organization (ODE, OIR), MDUFA performance goals |
| S7 | 510(k) Clearances (database landing page) | FDA / CDRH | https://www.fda.gov/medical-devices/device-approvals-and-clearances/510k-clearances | current | Trigger conditions for submission (new device / significant change) |
| S8 | How To Prepare A Special 510(k) | FDA / CDRH | https://www.fda.gov/medical-devices/premarket-notification-510k/how-prepare-special-510k | Page last reviewed 06/28/2024 | Traditional / Special / Abbreviated 510(k) types |
| S9 | 21 CFR Part 814 — Premarket Approval of Medical Devices | FDA / eCFR | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-814 | Current eCFR version | Subpart B (PMA application, §814.20), PMA supplements, postapproval reporting (§814.82, §814.84) |
| S10 | PMA Approvals (program landing page) | FDA / CDRH | https://www.fda.gov/medical-devices/device-approvals-and-clearances/pma-approvals | current | Statutory basis section 515; petition for administrative review (§515(g)) |
| S11 | PMA Regulations (regulatory index) | FDA / CDRH | https://www.fda.gov/medical-devices/premarket-approval-pma/pma-regulations | current | Cross-references 21 CFR 814, 54, 801, 820; Federal Register rulemaking history |
| S12 | Annual Reports for Approved Premarket Approval Applications (PMA) — Guidance for Industry and FDA Staff | FDA / CDRH, CBER | https://www.fda.gov/regulatory-information/search-fda-guidance-documents/annual-reports-approved-premarket-approval-applications-pma | December 2019 (Final) | Postapproval periodic reporting obligation, §814.84(b) |
| S13 | 21 CFR Part 830 — Unique Device Identification | FDA / eCFR | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-830 | Current eCFR version | Subpart E — GUDID submission requirements |
| S14 | 21 CFR § 830.20 — Requirements for a unique device identifier | Cornell LII (mirrors eCFR) | https://www.law.cornell.edu/cfr/text/21/830.20 | Current | UDI issuance/standards conformance rule |
| S15 | Unique Device Identification System — Final Rule | FDA / Federal Register | https://www.federalregister.gov/documents/2013/09/24/2013-23059/unique-device-identification-system | September 24, 2013 | Establishes UDI system; amends 21 CFR Parts 16, 801, 803, 806, 810, 814, 820, 821, 822, 830 |
| S16 | 21 CFR Part 860 — Medical Device Classification Procedures | FDA / eCFR | https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-860 | Current eCFR version | Subpart A (definitions incl. "classification regulation," "De Novo request"), Subpart B (classification into Class I/II/III) |
| S17 | Medical Device Classification Product Codes — Guidance for Industry and FDA Staff | FDA / CDRH | https://www.fda.gov/media/82781/download | Dated on document (guidance) | Product code assignment logic, licensed-device product codes |
| S18 | Device Registration and Listing (program landing page) | FDA / CDRH | https://www.fda.gov/medical-devices/how-study-and-market-your-device/device-registration-and-listing | current | Confirms the premarket-submission-number listing detail (510(k)/De Novo/PMA/PDP/HDE) that could not be located verbatim in the §807.25 text retrieved — added in v3 verification pass to correct a mis-citation |
 
**Note on source tiering for ontology traceability:** S1–S4, S9, S13–S16 are primary legal text (CFR, eCFR, Federal Register) — highest evidentiary weight for `rdfs:isDefinedBy` / `skos:source` style annotations. S5–S8, S10–S12, S17 are FDA program/guidance pages — authoritative for process description and terminology but non-binding "current thinking" (guidance) rather than codified rule (see Rule R7).
 
**Citation policy applied in this revision:** each source is quoted directly at most once, and only where the exact regulatory phrasing carries legal weight; all other content from a source is paraphrased in this document's own words.
 
---
 
## 2. Extracted Domain Concepts
 
### 2.1 Manufacturer / Owner-Operator
 
- **Regulatory definition:** Part 807 defines "owner or operator" as the legal entity (corporation, subsidiary, affiliated company, partnership, or proprietor) directly responsible for a registering establishment's activities. Source: 21 CFR 807.3(f) [S2].
- The registration obligation itself is written more broadly than the "owner or operator" definition: it attaches to anyone engaged in manufacturing, preparing, propagating, compounding, assembling, or processing a device for human use — including a party who only initiates or develops specifications for a device built by someone else, or who sterilizes/processes a device on another party's behalf. Source: 21 CFR 807.20(a) [S3].
- **Ontology interpretation:**
  - Candidate Class: `Manufacturer` (subclass of `LegalEntity`); sibling classes `SpecificationDeveloper`, `SterilizerOrProcessor`, `InitialImporter`, `WholesaleDistributor`, `OfficialCorrespondent` — the CFR treats these as *roles* an entity plays relative to a device or establishment, not mutually-exclusive types.
  - Candidate Object Property: `hasEstablishment`, `isOwnerOperatorOf`, `initiatesSpecificationsFor`, `manufactures`
  - Candidate Event: none directly (Manufacturer is a persistent actor, not an event)
  - Candidate Data Property: `legalEntityName`, `dunsNumber` (used operationally in FURLS/DRLM though not defined in the 807.3 text retrieved)

### 2.2 Initial Importer
 
- **Regulatory definition (verbatim — public-domain government text, safe to quote in full):** "Initial importer means any importer who furthers the marketing of a device from a foreign manufacturer to the person who makes the final delivery or sale of the device to the ultimate consumer or user, but does not repackage, or otherwise change the container, wrapper, or labeling of the device or device package." Source: 21 CFR 807.3(g) [S2].
- **Correction note (v3):** the v2 draft dropped the repackaging/relabeling proviso and substituted an invented clause ("the first link in the domestic distribution chain, not any downstream importer/reseller") that does not appear in the regulation. This mattered for the ontology because the actual boundary condition (repackaging/relabeling) is what separates `InitialImporter` from a `Repackager`/`Relabeler` role — not chain position, which the invented clause implied instead. §807.20(a)(5) additionally confirms that acting as an initial importer as defined in §807.3(g) is itself one of the activities that triggers the registration obligation, with a partial listing-obligation carve-out for devices the importer did not initiate/develop specifications for.
- **Ontology interpretation:**
  - Candidate Class: `InitialImporter` (subclass of `LegalEntity`, role-type alongside Manufacturer); should be modeled `disjointWith` `Repackager`/`Relabeler` roles given the proviso
  - Candidate Object Property: `importsDeviceFrom` (range: `ForeignManufacturer`), `furthersMarketingOf`
  - Candidate Event: `ImportationEvent` (candidate — not explicit in source text, inferred from process)

### 2.3 Wholesale Distributor
 
- **Regulatory definition:** any party other than the manufacturer or initial importer that moves a device from its point of manufacture toward the party that ultimately delivers or sells it to the end user. Source: 21 CFR 807.3(t) [S2].
- **Exemption rule (new in v3 — previously missing from this document entirely):** a wholesale distributor is exempt from the registration and listing requirements altogether, provided it does not manufacture, repackage, process, or relabel a device. Source: 21 CFR 807.20(c) [S3]. See Rule R11.
- **Ontology interpretation:**
  - Candidate Class: `WholesaleDistributor`
  - Candidate Object Property: `distributes`, `precedesInSupplyChain`, `exemptFromRegistration` (boolean, derived from whether the distributor performs manufacturing/repackaging/processing/relabeling activity)

### 2.4 Establishment
 
- Referred to throughout Part 807 as the registered site of manufacture, preparation, propagation, compounding, assembly, or processing — distinct from the owner/operator (legal entity) that registers it. Foreign establishments have a parallel obligation. Source: [S1, S4].
- **Correction note (v3):** the v2 draft framed "official correspondent" as a role specific to foreign establishments. That is inaccurate — §807.3(e) defines Official Correspondent generally as the person the owner/operator designates to handle FDA correspondence and officer/director-list submissions, and §807.21 confirms the domestic registration contact person also serves as the official correspondent by default. Foreign establishments are not the only context in which this role appears; it is a general Part 807 role attached to any registering owner/operator. Source: 21 CFR 807.3(e), 807.21 [S2, and the eCFR page for §807.21].
- **Ontology interpretation:**
  - Candidate Class: `Establishment` (subclass of `Location`/`Facility`); subclass `ForeignEstablishment`
  - Candidate Object Property: `registeredBy` (domain: `Establishment`, range: `OwnerOperator`), `locatedIn`
  - Candidate Data Property: `registrationNumber`, `establishmentType`

### 2.5 Establishment Registration
 
- **Regulatory definition:** an owner or operator must register its name, places of business, and establishments, and list its devices, regardless of whether the establishment's output enters interstate commerce. Source: 21 CFR 807.20(a) [S3].
- **Non-compliance state:** a registration or listing that is not completed by the required deadline puts the establishment into a "failed to register" or "failed to list" status; the record is treated as inactive and is suppressed from FDA's public site until the owner/operator submits, and FDA processes, the missing information. **Source (corrected in v3): 21 CFR 807.22(c) [S1]** — the v2 draft mis-cited this to §807.25; §807.25 covers submission channel/content, while §807.22 covers timing and the consequence of missing a deadline.
- **Submission channel:** registration and listing information must be submitted through FDA's electronic system, unless the owner/operator has been granted a waiver from electronic submission (in which case paper procedures apply); electronic submissions are also subject to Part 11 recordkeeping requirements, with specified exceptions. Source: 21 CFR 807.25(a) [S1] — this citation was correct in v2 and is unchanged.
- **Annual renewal cycle (confirmed in v3, previously flagged "inferred, verify"):** all establishments must renew registration annually, during the window of October 1 through December 31 of each fiscal year; updates to registration information generally must be made within 30 days of a change. Source: 21 CFR 807.22(b)(1)–(2) [S1].
- **Ontology interpretation:**
  - Candidate Class: `EstablishmentRegistration` (an artifact/record class, not the act itself)
  - Candidate Event: `RegistrationSubmissionEvent`, `RegistrationRenewalEvent` (annual, Oct 1–Dec 31 window — confirmed against §807.22(b)(1)), `RegistrationLapseEvent`
  - Candidate Object Property: `hasStatus` (range: enumerated `RegistrationStatus`), `registeredVia` (range: `ElectronicSubmissionSystem` or `WaiverPathway`)
  - Candidate Data Property: `registrationDate`, `fiscalYear` (defined in §807.3(u) as Oct 1–Sep 30 — noted but not yet retrieved verbatim; flag for verification)

### 2.6 Device Listing
 
- **Regulatory definition:** required per-device information includes the current registration number of the establishment where the device is made, a product code (for devices exempt from premarket review, or devices in commercial distribution before May 28, 1976), and the proprietary/brand name(s). Source: 21 CFR 807.25 [S1].
- **Premarket submission number requirement — re-sourced in v3:** if a device requires marketing authorization before it can be marketed, the owner/operator must also provide the FDA premarket submission number. **Correction:** v2 attributed this specifically to §807.25, but that exact requirement could not be located verbatim in the §807.25 text retrieved during re-verification. It is confirmed instead on FDA's Device Registration and Listing program page, which lists the applicable submission types as **510(k), De Novo, PMA, PDP, and HDE** — one more pathway (PDP — Product Development Protocol, 21 CFR 814 Subpart D) than the four this document had previously captured. Source: [S18]. This should be treated as guidance-level confirmation (Rule R7 applies) until the specific CFR subsection is located directly.
- **Ontology interpretation:**
  - Candidate Class: `DeviceListing`
  - Candidate Object Property: `listedUnderEstablishment` (DeviceListing → Establishment), `referencesSubmission` (range: `PremarketSubmission` — 510(k), PMA, De Novo, PDP, HDE)
  - Candidate Data Property: `brandName`, `productCode`
  - Candidate Event: `ListingSubmissionEvent`

### 2.7 Device (regulatory sense)
 
- Registration/listing scope, per §807.20, applies to anyone engaged in manufacturing, preparing, propagating, compounding, assembling, or processing a device intended for human use (see 2.1). Note: the FD&C Act §201(h) statutory definition of "device" itself was not retrieved in this session — flagged as a gap; see §5.
- **Ontology interpretation:**
  - Candidate Class: `MedicalDevice`
  - Candidate Object Property: `classifiedAs` (range: `DeviceClassification`), `hasProductCode`, `hasUDI`, `hasListing` (range: `DeviceListing`)
  - Candidate Data Property: `deviceName`, `intendedUse`

### 2.8 Device Classification (Class I / II / III)
 
- **Regulatory definition:** device classification places a generic device type into Class I (general controls), Class II (special controls), or Class III (premarket approval), based on the level of control needed to reasonably assure safety and effectiveness. Source: 21 CFR Part 860, Subpart B [S16].
- "Classification regulation" is itself a defined term: a section under 21 CFR Parts 862–892 that identifies (general description, intended use) and classifies (Class I/II/III) a device type or related group of device types. Source: 21 CFR 860.3 [S16].
- **Ontology interpretation:**
  - Candidate Class: `DeviceClassification` (enumerated individuals: `ClassI`, `ClassII`, `ClassIII`); `ClassificationRegulation` as a separate class linking a device type to its class
  - Candidate Object Property: `classifiedAs`, `governedByRegulation`
  - Candidate Data Property: `cfrPart`, `cfrSection`

### 2.9 De Novo Request
 
- **Regulatory definition:** a De Novo request is a submission under FD&C Act §513(f)(2) asking FDA to classify a device into Class I or Class II (rather than the default Class III that applies to novel, not-substantially-equivalent devices), including all information submitted with or incorporated into it. Source: 21 CFR 860.3 [S16].
- **Ontology interpretation:**
  - Candidate Class: `DeNovoRequest` (subclass of `PremarketSubmission`)
  - Candidate Event: `DeNovoGrantEvent` — reported (in a non-primary secondary source, not yet verified against 21 CFR 860 Subpart D) to produce a new `ClassificationRegulation` and `ProductCode` as side-effects; treat as **unverified process detail** until confirmed against primary text (see §5, design question 4)
  - Candidate Object Property: `requestsClassificationInto`

### 2.10 Premarket Notification — 510(k)
 
- **Regulatory definition:** a 510(k) is a premarket submission demonstrating that a device is substantially equivalent — i.e. as safe and effective — to a legally marketed predicate device, per FD&C Act §513(i)(1)(A). Source: FDA 510(k) program page [S5].
- **Submission trigger:** required when a manufacturer intends to introduce a device into commercial distribution for the first time, or to reintroduce a device that has been changed or modified enough to potentially affect its safety or effectiveness — covering changes to design, material, chemical composition, energy source, manufacturing process, or indications for use. Source: [S7].
- **Submission types:** Traditional, Special, and Abbreviated 510(k). Source: [S8].
- **Review body:** CDRH's Office of Device Evaluation (ODE) and Office of In Vitro Diagnostics and Radiological Health (OIR) review 510(k) submissions against MDUFA performance-goal timelines. Source: [S6].
- **Ontology interpretation:**
  - Candidate Class: `PremarketNotification510k` (subclass of `PremarketSubmission`); subclasses `TraditionalFiveTenK`, `SpecialFiveTenK`, `AbbreviatedFiveTenK`
  - Candidate Object Property: `demonstratesEquivalenceTo` (range: `PredicateDevice`), `reviewedBy` (range: `ReviewOffice`), `triggeredByChange` (range: enumerated `DeviceChangeType`)
  - Candidate Event: `FiveTenKSubmissionEvent`, `SubstantialEquivalenceDeterminationEvent`, `ClearanceEvent`
  - Candidate Data Property: `submissionDate`, `decisionDate`, `kNumber`

### 2.11 Substantial Equivalence / Predicate Device
 
- Not retrieved verbatim from primary CFR/statutory text in this session — the precise legal test in FD&C Act §513(i)(1)(A) and 21 CFR 807.92(a)(3) was only referenced indirectly, via the FDA landing page's paraphrase in 2.10. **Flag: Source verification required** before this concept's formal definition is treated as settled.
- **Ontology interpretation:**
  - Candidate Class: `PredicateDevice`
  - Candidate Object Property: `isPredicateFor`, `hasSameIntendedUseAs`, `hasSameTechnologicalCharacteristicsAs`
  - Candidate Event: `SubstantialEquivalenceDeterminationEvent` (decision outcome as enumerated individual: `SE` / `NSE`)

### 2.12 Premarket Approval (PMA)
 
- **Regulatory definition (paraphrased from a non-primary source, flagged):** a PMA submission documents evidence of reasonable assurance of safety and effectiveness, for devices that are high-risk or otherwise ineligible for 510(k)/De Novo, and must include design, manufacturing, labeling, performance-testing, clinical, and risk-analysis data. Source: [S11] — treat as description pending primary-text confirmation.
- **Change-control rule:** PMA supplements are required for any change affecting safety or effectiveness, except changes limited to manufacturing procedures or method of manufacture (per FD&C Act §515(d)(6), added by FDAMA 1997). Source: [S10].
- **Changes Being Effected mechanism:** a manufacturer may implement certain safety-enhancing changes before formally receiving FDA's written approval order for the PMA supplement, provided the supplement is clearly labeled "Special PMA Supplement—Changes Being Effected," includes a full explanation of the change, and FDA has acknowledged receipt. Source: 21 CFR 814.39(d) [S9].
- **Administrative review:** any interested person may petition for review of an approval decision, via either a formal hearing under 21 CFR Part 12 or an independent advisory-committee review, per FD&C Act §515(g). Source: [S10].
- **Ontology interpretation:**
  - Candidate Class: `PremarketApproval` (subclass of `PremarketSubmission`); `PMASupplement` (subclass, with further subclass `SpecialPMASupplement`)
  - Candidate Object Property: `supplements` (PMASupplement → PMA), `requestsAdministrativeReviewOf`
  - Candidate Event: `PMAApprovalEvent`, `PMASupplementApprovalEvent`, `ChangesBeingEffectedEvent` (a self-executing state transition prior to formal FDA order — notable because the *effective date* of the change precedes the *regulatory decision event*, an important temporal-modeling case)
  - Candidate Data Property: `pmaNumber`, `supplementNumber`

### 2.13 Postapproval Reporting (PMA)
 
- **Regulatory definition:** approved PMAs are subject to periodic reporting under the terms of the approval order, per 21 CFR 814.82(a) and 814.84(b); FDA guidance describes the required annual-report content and FDA's review actions. Source: [S12].
- **Ontology interpretation:**
  - Candidate Class: `PMAAnnualReport` (subclass of `PostmarketReport`)
  - Candidate Event: `AnnualReportSubmissionEvent`, `AnnualReportReviewEvent`
  - Candidate Object Property: `reportsOn` (range: `PremarketApproval`)

### 2.14 Regulatory Authority / FDA
 
- FDA operates as issuer, reviewer, and register-keeper across all instruments above (registration acceptance, 510(k) clearance, PMA approval, GUDID accreditation of issuing agencies). CDRH is identified specifically as the reviewing center for premarket submissions. Source: [S6].
- **Ontology interpretation:**
  - Candidate Class: `RegulatoryAuthority` (individual: `FDA`); `RegulatoryCenter` (individual: `CDRH`); `ReviewOffice` (individuals: `ODE`, `OIR`)
  - Candidate Object Property: `hasSubOrganization`, `reviews`, `approves`, `accredits` (FDA accredits UDI issuing agencies — see 2.16)

### 2.15 Unique Device Identifier (UDI) / UDI System
 
- **Regulatory definition:** a UDI must be issued under a system operated by FDA or an FDA-accredited issuing agency, conform to ISO/IEC 15459-2, -4, and -6, and use only characters from the invariant character set of ISO/IEC 646. Source: 21 CFR 830.20 [S14].
- **Labeling and database obligation:** the UDI final rule requires the device label to bear a UDI (subject to defined exceptions/alternative placement), and requires the labeler to submit product information to GUDID, again subject to defined exceptions. Source: Federal Register, Sept. 24, 2013 [S15].
- **Ontology interpretation:**
  - Candidate Class: `UniqueDeviceIdentifier` (composed of `DeviceIdentifier` (fixed/DI) and `ProductionIdentifier` (variable/PI) — this DI/PI structure was retrieved only from a non-.gov secondary source; primary-text confirmation not yet obtained; **flag: source verification required**)
  - Candidate Object Property: `identifies` (UDI → MedicalDevice), `issuedBy` (range: `IssuingAgency`), `conformsToStandard` (range: `ISOStandard`)
  - Candidate Data Property: `udiString`, `lotNumber`, `expirationDate`, `manufactureDate`
  - Candidate Event: `UDIAssignmentEvent`, `UDILabelingEvent`

### 2.16 GUDID (Global Unique Device Identification Database) & Labeler
 
- **Regulatory definition:** UDI data must be submitted electronically to GUDID in an FDA-processable format, unless the labeler has obtained a waiver from electronic submission. Source: 21 CFR Part 830, Subpart E [S13].
- **Rejection conditions:** FDA may reject or remove GUDID data if the submitted device identifier does not conform to §830.20, if the device is neither manufactured in nor in U.S. interstate commerce, or if FDA determines the product is not a device (or a qualifying combination product). Source: 21 CFR 830, Subpart E [S13] — see also Rule R8.
- Issuing-agency accreditation is itself an FDA-administered process: an applicant seeking accreditation must notify FDA through a defined correspondence procedure. Source: 21 CFR Part 830 [S13].
- **Ontology interpretation:**
  - Candidate Class: `GUDIDRecord`, `Labeler` (role played by an entity submitting UDI data — often but not always the Manufacturer), `IssuingAgency`
  - Candidate Object Property: `submitsTo` (Labeler → GUDID), `waivedFrom` (Labeler → ElectronicSubmissionRequirement)
  - Candidate Event: `GUDIDSubmissionEvent`, `GUDIDRejectionEvent`, `IssuingAgencyAccreditationEvent`

### 2.17 Premarket Submission (superclass)
 
- Cross-cutting concept implied by the device-listing requirement's cross-reference to whichever premarket instrument authorizes a device — approved PMA, cleared 510(k), granted De Novo, or approved HDE — i.e. the regulation itself treats these four instruments as members of one family sharing a "submission number" data property. Source: 21 CFR 807.25 [S1].
- **Ontology interpretation:**
  - Candidate Class: `PremarketSubmission` (abstract superclass of `PremarketNotification510k`, `PremarketApproval`, `DeNovoRequest`, `HumanitarianDeviceExemption`, `ProductDevelopmentProtocol` — the fifth pathway confirmed via [S18] during v3 verification, not sourced from primary 21 CFR 814 Subpart D text yet; treat with the same caution as HDE below)
  - Candidate Data Property: `submissionNumber`
  - Candidate Object Property: `resultsInAuthorizationStatus`
- **Gap flag — Humanitarian Device Exemption (HDE):** HDE is asserted here as a peer subclass solely because §807.25 mentions "approved humanitarian device [exemption]" in passing. No dedicated HDE source (21 CFR 814, Subpart H) was retrieved in this session, so HDE currently has no independent regulatory definition, business rules, or object properties of its own in this document — it should not be treated as equivalently well-sourced to 510(k), PMA, or De Novo until Subpart H is reviewed directly.
---

## 3. Relationships
 
```
Manufacturer (OwnerOperator)
    |
    owns / operates
    |
Establishment
    |
    is subject of
    |
EstablishmentRegistration --- hasStatus ---> RegistrationStatus {active, failedToRegister, failedToList}
                                              (kept as two distinct status values per R1 — see
                                               open design question §5.3 on whether Registration
                                               and Listing status should be separate enumerations
                                               entirely rather than sharing one)
 
Manufacturer
    |
    manufactures
    |
MedicalDevice
    |
    classifiedAs
    |
DeviceClassification {ClassI, ClassII, ClassIII} --- governedByRegulation ---> ClassificationRegulation
    |
    requiresPathway (see Rule R10)
    |
PremarketSubmission {typically PremarketApproval for ClassIII;
                      typically PremarketNotification510k for ClassII;
                      typically none/exempt for ClassI}
 
MedicalDevice
    |
    hasListing
    |
DeviceListing --- referencesSubmission ---> PremarketSubmission
                                                   |
                        ---------------------------------------------------
                        |                |                |               |
              PremarketNotification510k  PremarketApproval  DeNovoRequest  HDE (under-sourced, §2.17)
                        |                       |
              demonstratesEquivalenceTo   supplementedBy
                        |                       |
                  PredicateDevice          PMASupplement
 
PremarketSubmission
    |
    reviewedBy
    |
ReviewOffice (ODE, OIR) --- partOf ---> CDRH --- partOf ---> FDA (RegulatoryAuthority)
 
MedicalDevice
    |
    hasUDI
    |
UniqueDeviceIdentifier --- issuedBy ---> IssuingAgency --- accreditedBy ---> FDA
UniqueDeviceIdentifier --- recordedIn ---> GUDIDRecord
 
Labeler
    |
    submitsTo
    |
GUDID
 
InitialImporter
    |
    importsDeviceFrom
    |
ForeignManufacturer --- registersVia ---> OfficialCorrespondent
 
WholesaleDistributor
    |
    distributes (downstream of manufacture, upstream of ultimate consumer)
    |
MedicalDevice
 
WholesaleDistributor --- exemptFromRegistration (if performsActivity NONE OF
                          {manufacture, repackage, process, relabel}) ---> EstablishmentRegistration
                          (i.e. no registration obligation exists in the first place — R11)
```
 
Additional narrower relationships extracted directly from source text:
- `Manufacturer --- initiatesSpecificationsFor ---> Device` (someone else physically manufactures) [S1/S3, §807.20(a)(1)]
- `Person --- sterilizesOrProcessesOnBehalfOf ---> SpecificationsDeveloper` [S1/S3, §807.20(a)(2)]
- `PMASupplement --- changesBeingEffectedPriorTo ---> FDAApprovalOrder` (temporal-override relationship) [S9]
- `AnyInterestedPerson --- petitionsForReviewOf ---> PMAApprovalDecision` [S10]
*Naming note (correction from prior draft): the property connecting a device to its listing is `hasListing` (MedicalDevice → DeviceListing), not `isSubjectOfListing`; the property connecting a device to its class is `classifiedAs`, not `hasClassification` — both names are now aligned with §2.7/§2.8's Ontology Interpretation blocks so the diagram and the concept sections use one consistent vocabulary.*
 
---
 
## 4. Regulatory Business Rules
 
Candidate rules, expressed informally with a target formalism suggestion.
 
**R1 — Registration completeness (SHACL candidate).**
An `EstablishmentRegistration` node that lacks required listing data by the specified deadline must transition to `hasStatus = FailedToRegister` (or `FailedToList`), and MUST NOT be exposed as `active` in any public-facing shape; FDA suppresses such records from public display until the missing information is submitted and processed. Source: 21 CFR 807.25 [S1].
 
**R2 — Electronic submission default (OWL restriction candidate).**
Every `EstablishmentRegistration` and `DeviceListing` instance must have `submittedVia = ElectronicSystem`, unless it has an associated `Waiver` instance, in which case paper-submission procedures apply instead. Suggested Manchester-syntax axiom (corrected from prior draft, which mixed a value restriction and an existential inside an invalid disjunction):
```
EstablishmentRegistration SubClassOf:
    (submittedVia value ElectronicSystem) or (hasWaiver some ElectronicSubmissionWaiver)
```
Source: 21 CFR 807.25(a) [S1].
 
**R3 — Listing must reference a valid submission number (SHACL candidate).**
Every `DeviceListing` for a device not exempt from premarket review MUST have `referencesSubmission` pointing to exactly one instance of `PremarketSubmission` (510(k), PMA, De Novo, or HDE) bearing a valid `submissionNumber`. Devices that are exempt, or that predate May 28, 1976, instead require a `productCode` value. Source: [S1, S3].
 
**R4 — PMA change classification (reasoning rule candidate).**
IF a proposed device change `affectsSafetyOrEffectiveness = true` AND `changeType ≠ ManufacturingProcedureChange`, THEN the change REQUIRES a `PMASupplement` (it cannot be handled through an annual report alone). Source: FD&C Act §515(d)(6) [S10].
 
**R5 — Changes Being Effected exception (temporal reasoning rule candidate).**
A `PMASupplement` marked "Changes Being Effected" MAY have `effectiveDate < approvalOrderDate`, provided (a) it is explicitly labeled as such, (b) it includes a full explanation, and (c) FDA has acknowledged receipt. This is a modeling exception to the general rule that market-authorization changes take effect only upon formal approval. Source: 21 CFR 814.39(d) [S9].
 
**R6 — 510(k) trigger condition (SHACL / reasoning candidate).**
A `MedicalDevice` instance MUST have an associated `PremarketNotification510k` (or other `PremarketSubmission`) if `firstCommercialDistribution = true` OR `significantChange = true`, where `significantChange` ranges over the enumerated set {design, material, chemicalComposition, energySource, manufacturingProcess, indicationsForUse}. Source: [S7].
 
**R7 — Guidance vs. binding rule distinction (modeling/annotation rule).**
Any concept sourced solely from an FDA guidance document (rather than CFR/Federal Register text) should carry an annotation property such as `bindingness = nonBinding` or `sourceType = Guidance`, since FDA guidance documents describe the agency's current thinking and recommendations rather than legally enforceable requirements, unless they cite a specific statutory or regulatory requirement. Source: [S12]. This rule should propagate: any class or property whose sole source is a guidance document (e.g., some 510(k)-submission-type detail in §2.10, or the PMA content description in §2.12) inherits `sourceType = Guidance` unless corroborated by a CFR citation.
 
**R8 — GUDID rejection conditions (SHACL candidate).**
A GUDID submission SHALL be rejected if any of: the DI does not conform to §830.20; the device is neither manufactured in nor in U.S. interstate commerce; or FDA determines the product is not a device (or a qualifying combination product). Source: 21 CFR Part 830, Subpart E [S13].
 
**R9 — UDI standards conformance (OWL restriction candidate).**
Every `UniqueDeviceIdentifier` must conform to all three of ISO/IEC 15459-2, 15459-4, and 15459-6, and must use only the invariant character set of ISO/IEC 646. Suggested Manchester-syntax axiom (corrected from prior draft, which used an unsupported "exactly N from an enumerated set" shorthand that OWL does not natively express):
```
UniqueDeviceIdentifier SubClassOf:
    (conformsToStandard value ISO_15459_2) and
    (conformsToStandard value ISO_15459_4) and
    (conformsToStandard value ISO_15459_6) and
    (usesCharacterSet value ISO_646_Invariant)
```
Source: 21 CFR 830.20 [S14].
 
**R11 — Wholesale distributor registration exemption (SHACL / OWL restriction candidate; NEW — found during v3 primary-source verification, absent from v1/v2).**
A `WholesaleDistributor` instance is exempt from `EstablishmentRegistration`/`DeviceListing` obligations entirely IF it does NOT perform any of {manufacture, repackage, process, relabel} with respect to the device. This is a genuine class-level exemption, not merely a status value — such a distributor never needs an `EstablishmentRegistration` record in the first place, as distinct from one that fails to register when it should have. Suggested Manchester-syntax axiom:
```
WholesaleDistributor and
  not (performsActivity some {manufacture, repackage, process, relabel})
SubClassOf: exemptFromRegistration value true
```
Source: 21 CFR 807.20(c) [S3].
 
**R10 — Classification-to-pathway mapping (reasoning rule candidate; NEW — identified during validation, not present in the original extraction).**
As a general pattern reflected across the classification and PMA sources reviewed: Class III devices are the population for which PMA is the applicable premarket pathway (PMA descriptions in §2.12 explicitly describe PMA as covering devices that are high-risk or ineligible for 510(k)/De Novo, and Part 860's Class III definition ties that class to "premarket approval" by name); Class II devices are typically the 510(k) population, unless individually exempted by their classification regulation; Class I devices are typically exempt from premarket review entirely, again unless their classification regulation says otherwise. **This mapping was absent from the original document — no explicit `DeviceClassification → PremarketSubmission` object property or rule had been captured, even though it is one of the more commonly asked competency questions ("does this Class III device need a PMA?").** Before formalizing as a strict OWL/SHACL constraint, this should be verified directly against FD&C Act §513 and 21 CFR Part 860, since classification-regulation-level exemptions can override the general pattern for specific device types.
 
---
 
## 5. Modeling Notes
 
**Ambiguous concepts:**
- *Manufacturer vs. Owner/Operator vs. Labeler.* The CFR text retrieved treats these as overlapping but distinct roles — "owner or operator" is precisely defined (§807.3(f)), while "manufacturer" is used descriptively (through the list of activities in §807.20(a)) rather than given its own standalone definition in the passages retrieved. "Labeler" (used for UDI/GUDID purposes) is not defined in the Part 830 passages retrieved either. Recommend modeling all three as **roles** an entity can hold (possibly simultaneously) rather than as a rigid class hierarchy, and flag `Manufacturer` and `Labeler` for a follow-up primary-source definition lookup (likely 21 CFR 820.3 for "manufacturer" under QMSR, not yet retrieved this session).
- *Substantial equivalence.* The precise legal test (513(i)(1)(A) FD&C Act / 807.92) was only retrieved via a paraphrasing FDA landing page, not the primary statutory/regulatory text itself. Marked **Source verification required** in §2.11.
- *UDI internal structure (DI/PI split).* Retrieved only from a non-.gov secondary source; the primary regulatory text for this specific structural claim (likely §830.20 combined with definitions in §830.3) should be fetched directly before this becomes a firm class/property design. Marked **Source verification required** in §2.15.
- *Device (statutory definition, FD&C Act §201(h)).* Not retrieved in this session — foundational term for the whole ontology and should be sourced directly from Cornell LII or eCFR text of 21 U.S.C. 321(h) in a follow-up pass rather than assumed from training knowledge.
- *Humanitarian Device Exemption.* Currently a placeholder subclass with no independent sourcing — see gap flag at end of §2.17.
**Concepts likely to differ across jurisdictions** (relevant if this ontology is later aligned with EU MDR/IVDR, matching the project's already-planned MDR_IVDR.md source file):
- FDA's "Establishment Registration + Device Listing" (Part 807) has a structural analogue in EU MDR's Economic Operator registration (EUDAMED), but the actor taxonomy differs: EU MDR Art. 10–14 formally distinguishes Manufacturer / Authorised Representative / Importer / Distributor, whereas the US text retrieved here defines Owner/Operator, Initial Importer, and Wholesale Distributor with different boundaries.
- FDA's three-class system (Class I/II/III, risk- and control-based) maps only loosely to the EU's four-class risk system (I, IIa, IIb, III) — a `DeviceClassification` class designed only against FDA sources will need a jurisdiction-scoped subclassing strategy (e.g., `FDADeviceClass` vs. `EUDeviceClass` as siblings under an abstract `RiskClassification`) rather than a single shared enumeration.
- GUDID vs. EUDAMED as parallel-but-distinct identifier databases — a non-primary secondary source frames GUDID as the US functional equivalent of EUDAMED, which is a useful modeling signal (candidate `equivalentDatabaseFunctionTo` relationship between jurisdiction-specific database classes) but is not itself a primary regulatory-text claim and should be treated as an analytical note, not a rule.
**Potential ontology design questions:**
1. Should `PremarketSubmission` be modeled as an event, a document/artifact, or both (an artifact that *has* lifecycle events)? The CFR text supports the artifact-with-events reading (a submission has a number, is reviewed, and results in a decision), suggesting `PremarketSubmission` as an artifact class linked via `hasEvent` to `SubmissionEvent`, `DecisionEvent`, etc., rather than modeling the submission itself as an event.
2. How should "role" vs. "class" be handled for actors (Manufacturer, Labeler, Owner/Operator, Initial Importer)? A single legal entity can hold multiple roles simultaneously or over time (e.g., a manufacturer that is also its own labeler and initial importer). This argues for an OWL pattern where `LegalEntity` is the core class and roles are modeled as either (a) subclasses with multiple inheritance, or (b) n-ary relations / reified role-assignment individuals with validity periods — the latter is more defensible if registration/labeler status changes over time and that history needs to be queryable.
3. Should `RegistrationStatus` and `ListingStatus` be separate enumerations, given the CFR text couples but does not fully merge them ("failed to register" **or** "failed to list" — implying independently trackable states for the establishment vs. the individual device listing)? **Note:** the relationship diagram in §3 currently keeps both values inside one shared `RegistrationStatus` enumeration as an interim choice — that is a modeling decision, not a resolution of this open question, and should be revisited once registration and listing are worked through as separate SHACL shapes.
4. Where does `De Novo` sit relative to `PremarketNotification510k` and `PremarketApproval`? Structurally it is its own submission type (§860.3), but is reported (in a secondary source only) to also *create* new `ClassificationRegulation` and `ProductCode` instances upon grant — should `DeNovoGrantEvent` have `createsClassificationRegulation` as an explicit side-effect property? This process detail was only found in a non-primary source; verify against §860 Subpart D before encoding as a firm rule.
5. Annotation strategy for guidance-derived vs. CFR-derived concepts (see Rule R7) — worth deciding early, since a meaningful share of process detail (review timelines, submission-type distinctions like Traditional/Special/Abbreviated 510(k)) currently traces only to FDA guidance/program pages rather than codified CFR text.
6. **(New)** Now that Rule R10 introduces a `DeviceClassification → PremarketSubmission` pathway mapping, should that mapping live as a default/derived inference (defeasible — overridable by a specific classification regulation), or as a hard OWL restriction? Given that individual classification regulations under Parts 862–892 can exempt a Class II device type from 510(k), a hard restriction risks being wrong for real device types; a defeasible/rule-based approach (e.g., SWRL rule with an explicit exception clause) is likely more defensible than an OWL cardinality restriction here.
---
 
## Verification status (added in v3)
 
**Re-verified word-for-word against primary eCFR text in this pass:** §2.1 Manufacturer/Owner-Operator, §2.2 Initial Importer, §2.3 Wholesale Distributor, §2.4 Establishment, §2.5 Establishment Registration, §2.6 Device Listing (§807.3, §807.20, §807.21, §807.22, §807.25). One material paraphrase error was found and fixed (Initial Importer, §2.2), one citation was found pointing to the wrong CFR section and fixed (§2.5), one genuinely missing business rule was found and added (R11), and one under-sourced claim was re-attributed to its actual source (§2.6 premarket submission number → S18).
 
**NOT yet re-verified against primary text in this pass — carry the same risk profile that §2.2/§2.5/§2.6 turned out to have before verification:** §2.7 Device, §2.8 Device Classification, §2.9 De Novo Request, §2.10 Premarket Notification 510(k), §2.11 Substantial Equivalence, §2.12 Premarket Approval, §2.13 Postapproval Reporting, §2.14 Regulatory Authority, §2.15 UDI, §2.16 GUDID. These sections should be treated as **candidate paraphrases pending the same word-for-word check**, not as confirmed-accurate the way §2.1–§2.6 now are.
 
## Gaps flagged for follow-up sourcing (not filled in this pass)
- FD&C Act §201(h) statutory definition of "device"
- 21 CFR 807.92(a)(3) and FD&C Act §513(i)(1)(A) — primary text for "substantial equivalence"
- 21 CFR 820.3 — QMSR definition of "manufacturer" (distinct from Part 807's descriptive usage)
- 21 CFR 830.3 — UDI system definitions (DI/PI terminology, "labeler")
- 21 CFR 860 Subpart D — De Novo classification process detail (side-effects on classification regulations/product codes)
- 21 CFR 814, Subpart H — Humanitarian Device Exemption, currently unsourced (see §2.17 gap flag)
- 21 CFR 814, Subpart D — Product Development Protocol (PDP), the fifth premarket pathway found in v3 via a program page but not yet sourced to primary CFR text
- FD&C Act §513 / 21 CFR Part 860 — direct primary-text confirmation for the classification→pathway mapping introduced as Rule R10
- Word-for-word verification of §2.7–§2.16 against primary text (see Verification status above) — this is now the single highest-priority next step, since the same class of error just found in §2.2 could equally be present anywhere in the unverified sections