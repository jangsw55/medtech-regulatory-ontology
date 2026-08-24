# FDA Medical Device Registration / Market Authorization — Source-Grounded Ontology Research

**Target file:** `research/registration/sources/01_FDA.md`
**Jurisdiction:** United States — FDA
**Research date:** 2026-08-09
**Research status:** Source-grounded research artifact
**Primary regulatory scope:** Registration, listing, classification, UDI, premarket submissions, regulatory decisions, and related market-access mechanisms.

> **Important modeling principle:** This document separates FDA regulatory evidence from ontology interpretation. Candidate classes, properties, events, and rules below are modeling hypotheses, not FDA terminology.

---

# 1. SOURCE DOCUMENTS

## 1.1 Primary legal / regulatory sources

### S01 — 21 CFR Part 807

**Document:** Establishment Registration and Device Listing for Manufacturers and Initial Importers of Devices
**Regulation:** 21 CFR Part 807
**Issuing organization:** U.S. Food and Drug Administration / U.S. Government
**Source type:** CFR
**Current version inspected:** Title 21 displayed by eCFR as of 2026-08-06
**Relevant sections:** §§807.3, 807.20–807.28, 807.81–807.87
**URL:** [21 CFR Part 807 — eCFR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807?utm_source=chatgpt.com)

This is the principal regulatory source for:

* Establishment
* Manufacturer-related activities
* Specification development
* Initial importer
* Importer
* Registration
* Device listing
* Listing number
* Product code
* FDA premarket submission number
* registration/listing updates
* commercial distribution
* 510(k) submission requirements

The current eCFR page identifies Part 807 as **“Establishment Registration and Device Listing for Manufacturers and Initial Importers of Devices.”** ([eCFR][1])

---

### S02 — 21 CFR Part 814

**Document:** Premarket Approval of Medical Devices
**Regulation:** 21 CFR Part 814
**Source type:** CFR
**Relevant sections:** §§814.3, 814.20, 814.42–814.46, 814.100–814.126
**URL:** [21 CFR Part 814 — eCFR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-814?utm_source=chatgpt.com)

Primary source for:

* PMA
* PMA applicant
* PMA amendment/supplement
* PMA approval
* denial
* withdrawal
* HDE
* HUD
* HDE approval

---

### S03 — 21 CFR Part 860

**Document:** Medical Device Classification Procedures
**Regulation:** 21 CFR Part 860
**Source type:** CFR
**Relevant sections:** §§860.1, 860.3, 860.120–860.140, 860.200–860.250
**URL:** [21 CFR Part 860 — eCFR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-860?utm_source=chatgpt.com)

Primary source for:

* classification
* Class I
* Class II
* Class III
* classification procedure
* reclassification
* De Novo classification procedure

21 CFR §860.1 explicitly states that Part 860 implements statutory provisions concerning classification and reclassification and describes the regulatory-control classes applicable to devices. ([eCFR][2])

---

### S04 — 21 CFR Part 812

**Document:** Investigational Device Exemptions
**Regulation:** 21 CFR Part 812
**Source type:** CFR
**Relevant sections:** §§812.1–812.3, 812.20, 812.30, 812.7
**URL:** [21 CFR Part 812 — eCFR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812?utm_source=chatgpt.com)

Primary source for:

* IDE
* investigational device
* investigation
* sponsor
* investigator
* sponsor-investigator
* significant risk device
* IDE exemption from certain marketing-related requirements

The regulation explicitly states that an approved IDE permits a device otherwise subject to performance-standard or PMA requirements to be shipped lawfully for investigation. ([eCFR][3])

---

### S05 — 21 CFR Part 801

**Document:** Labeling
**Regulation:** 21 CFR Part 801
**Source type:** CFR
**Relevant sections:** §§801.20, 801.30, 801.40, 801.45, 801.50, 801.55, 801.57
**URL:** [21 CFR Part 801 — eCFR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-801?utm_source=chatgpt.com)

Primary source for UDI labeling requirements.

---

### S06 — 21 CFR Part 830

**Document:** Unique Device Identification
**Regulation:** 21 CFR Part 830
**Source type:** CFR
**Relevant section:** §830.300 and related provisions
**URL:** [21 CFR Part 830 — eCFR](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-830?utm_source=chatgpt.com)

Primary regulatory source for device-identification-data submission requirements.

---

### S07 — FD&C Act §513

**Statute:** 21 U.S.C. §360c
**Source type:** U.S. Code
**Relevant provisions:** classification; substantial equivalence; De Novo
**URL:** [21 U.S.C. §360c — Classification of devices](https://uscode.house.gov/view.xhtml?req=%28title%3A21+section%3A360c%29&utm_source=chatgpt.com)

The statute defines substantial equivalence in relation to a device and a predicate device and establishes the statutory basis for the De Novo pathway. 

---

### S08 — FD&C Act §515

**Statute:** 21 U.S.C. §360e
**Source type:** U.S. Code
**Relevant provisions:** §§360e(a), 360e(c)
**URL:** [21 U.S.C. §360e — Premarket approval](https://uscode.house.gov/view.xhtml?req=%28title%3A21+section%3A360e%29&utm_source=chatgpt.com)

Primary statutory source for PMA.

---

### S09 — FD&C Act §520(g)

**Statute:** 21 U.S.C. §360j(g)
**Source type:** U.S. Code
**Relevant provision:** Investigational Device Exemption
**Source verification:** Statutory provision referenced directly by 21 CFR Part 812.

---

### S10 — FD&C Act §520(m)

**Statute:** 21 U.S.C. §360j(m)
**Source type:** U.S. Code
**Relevant provision:** Humanitarian Device Exemption
**URL:** [21 U.S.C. §360j — General provisions respecting control of devices](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=granuleid%3AUSC-prelim-title21-section360j&utm_source=chatgpt.com)

The current statutory text uses the **8,000-person threshold** for the humanitarian-device mechanism. 

---

# 1.2 Official FDA sources

### S11 — FDA: Who Must Register, List and Pay the Fee

**Source type:** FDA regulatory information
**URL:** [Who Must Register, List and Pay the Fee](https://www.fda.gov/medical-devices/device-registration-and-listing/who-must-register-list-and-pay-fee?utm_source=chatgpt.com)

FDA states that establishments involved in production and distribution of medical devices intended for commercial distribution generally must register annually and that most establishments subject to registration must also list devices and activities. ([U.S. Food and Drug Administration][4])

---

### S12 — FDA: Premarket Notification 510(k)

**Source type:** FDA official regulatory explanation
**URL:** [Premarket Notification 510(k)](https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k?utm_source=chatgpt.com)

Used to clarify:

* 510(k) purpose
* substantial equivalence
* predicate device
* SE decision
* clearance terminology

FDA explicitly describes an SE decision as a decision that **“clears”** the device for commercial distribution. ([U.S. Food and Drug Administration][5])

---

### S13 — FDA: Premarket Approval (PMA)

**URL:** [Premarket Approval (PMA)](https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-approval-pma?utm_source=chatgpt.com)

Used to clarify PMA's market-access role and distinction from 510(k). ([U.S. Food and Drug Administration][6])

---

### S14 — FDA: De Novo Classification Request

**URL:** [De Novo Classification Request](https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request?utm_source=chatgpt.com)

Used to clarify the De Novo classification request and resulting Class I/II pathway. ([U.S. Food and Drug Administration][7])

---

### S15 — FDA: UDI Basics

**URL:** [UDI Basics](https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics?utm_source=chatgpt.com)

Used for UDI, DI, PI, labeler, and GUDID concepts. ([U.S. Food and Drug Administration][8])

---

### S16 — FDA: Global Unique Device Identification Database

**URL:** [Global Unique Device Identification Database](https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/global-unique-device-identification-database-gudid?utm_source=chatgpt.com)

Used for GUDID semantics and DI records. ([U.S. Food and Drug Administration][9])

---

### S17 — FDA Product Classification Database

**Database:** Product Classification
**URL:** [FDA Product Classification Database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/classification.cfm?utm_source=chatgpt.com)

The database contains medical devices together with classification, product code, FDA premarket review organization, regulation number and other regulatory information. ([FDA Access Data][10])

---

### S18 — FDA 510(k) Database

**Database:** 510(k) Premarket Notification
**URL:** [FDA 510(k) Database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?utm_source=chatgpt.com)

An inspected FDA record exposes structured fields including:

* 510(k) number
* device name
* applicant
* regulation number
* product code
* date received
* decision date
* decision
* submission type
* review panel

For example, FDA database records use **“Decision: Substantially Equivalent (SESE)”** as a decision value. ([FDA Access Data][11])

---

### S19 — FDA PMA Database

**URL:** [FDA PMA Database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm?utm_source=chatgpt.com)

The database exposes fields including applicant, device, product code, PMA number, decision date, advisory committee and supplement type. ([FDA Access Data][12])

---

### S20 — FDA HDE Database

**URL:** [FDA HDE Database](https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfHDE/hde.cfm?utm_source=chatgpt.com)

---

# 2. EXTRACTED DOMAIN CONCEPTS

## 2.1 Establishment

### Concept: Establishment

**Source**

* Regulation: 21 CFR §807.3(c)
* URL: [21 CFR Part 807](https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807?utm_source=chatgpt.com)

**Regulatory text:**

> “Establishment means a place of business under one management at one general physical location”

**Context**

The term is defined within the FDA registration/listing framework. It is therefore not simply synonymous with a legal organization or manufacturer.

**Ontology interpretation**

* Candidate Class: `fda:Establishment`
* Candidate Object Property: `fda:hasOwnerOperator`
* Candidate Object Property: `fda:performsDeviceActivity`
* Candidate Data Property: `fda:physicalLocation`
* Candidate Event: `fda:EstablishmentRegistration`

**Modeling note**

This is one of the most important FDA-specific distinctions. An establishment is spatial/operational in the regulation, while owner/operator is the entity responsible for its activities. The ontology should therefore **not initially model Establishment as a subclass of Manufacturer**.

([eCFR][1])

---

## 2.2 Manufacturer-related activity

### Concept: Manufacture / processing

**Source**

* Regulation: 21 CFR §807.3(d)

**Regulatory text:**

> “manufacture, preparation, propagation, compounding, assembly, or processing of a device”

**Context**

FDA uses a broad activity concept encompassing manufacturing and several other activities. The definition specifically includes initial importation, repackaging/relabeling and specification initiation.

**Ontology interpretation**

* Candidate Class: `fda:DeviceActivity`
* Candidate subclasses:

  * `fda:Manufacturing`
  * `fda:Repackaging`
  * `fda:Relabeling`
  * `fda:SpecificationDevelopment`
  * `fda:InitialImportation`
  * `fda:Reprocessing`

**Modeling note**

The regulatory model is activity-centric. This is important because the same owner/operator may have an establishment performing multiple activities.

([eCFR][1])

---

## 2.3 Initial Importer

### Concept: Initial Importer

**Source**

* Regulation: 21 CFR §807.3(g)

**Regulatory text:**

> “Initial importer means any importer who furthers the marketing of a device from a foreign manufacturer”

**Context**

The initial importer is a specifically defined role. It is not equivalent to every importer.

**Ontology interpretation**

* Candidate Class: `fda:InitialImporter`
* Candidate subclass: `fda:ImporterRole`
* Candidate Object Property: `fda:importsDeviceFrom`
* Candidate Object Property: `fda:furthersMarketingOf`

**Modeling note**

The distinction between `Importer` and `InitialImporter` should be preserved. FDA's registration rules assign specific obligations to initial importers. ([eCFR][1])

---

## 2.4 Importer

### Concept: Importer

**Source**

* Regulation: 21 CFR §807.3(x)

**Regulatory text:**

> “Importer means, for purposes of this part, a company or individual in the United States”

**Context**

The definition is specific to Part 807 and concerns the U.S. entity associated with an imported foreign-establishment device.

**Ontology interpretation**

* Candidate Class: `fda:Importer`
* Candidate Object Property: `fda:importsDevice`
* Candidate Data Property: `fda:location`

**Modeling note**

`Importer` must not automatically be equated with `InitialImporter`. The ontology should retain both concepts until cross-provision analysis establishes a justified abstraction.

([eCFR][1])

---

## 2.5 Specification Developer

### Concept: Specification Developer

**Source**

* Regulation: 21 CFR §§807.3(d), 807.20(a)(1)

**Regulatory text:**

> “Initiates or develops specifications for a device that is to be manufactured by a second party”

**Context**

The FDA registration framework explicitly recognizes specification development as a regulated activity even where another party manufactures the device.

**Ontology interpretation**

* Candidate Class: `fda:SpecificationDeveloper`
* Candidate Object Property: `fda:developsSpecificationFor`
* Candidate Event: `fda:SpecificationDevelopment`

**Modeling note**

This supports separating the organization performing specification development from the establishment physically manufacturing the device.

([eCFR][1])

---

## 2.6 Registration

### Concept: Establishment Registration

**Source**

* Regulation: 21 CFR §§807.20–807.22

**Regulatory text:**

> “shall register and submit listing information”

**Context**

Registration applies to qualifying establishments/owners/operators. Initial registration and annual/update obligations are separately specified.

21 CFR §807.22 establishes initial registration timing, annual registration, 30-day update requirements and consequences of failure to register. ([eCFR][1])

**Ontology interpretation**

* Candidate Class: `fda:EstablishmentRegistration`
* Candidate Object Property: `fda:registers`
* Candidate Object Property: `fda:registeredEstablishment`
* Candidate Data Property: `fda:registrationNumber`
* Candidate Event: `fda:InitialRegistration`
* Candidate Event: `fda:RegistrationUpdate`
* Candidate State: `fda:ActiveRegistration`
* Candidate State: `fda:FailedToRegister`

**Modeling note**

Registration is a **regulatory record/process concerning an establishment**, not a market authorization for a device.

---

## 2.7 Device Listing

### Concept: Device Listing

**Source**

* Regulation: 21 CFR §§807.20, 807.21, 807.25, 807.28

**Regulatory text:**

> “submit listing information for those devices in commercial distribution”

**Context**

Listing is associated with devices and the establishments/activities associated with them. Listing information can be created, updated, discontinued and reactivated. ([eCFR][1])

**Ontology interpretation**

* Candidate Class: `fda:DeviceListing`
* Candidate Object Property: `fda:listsDevice`
* Candidate Object Property: `fda:listingEstablishment`
* Candidate Object Property: `fda:listingActivity`
* Candidate Data Property: `fda:listingNumber`
* Candidate Event:

  * `fda:DeviceListingCreation`
  * `fda:DeviceListingUpdate`
  * `fda:DeviceListingDiscontinuation`
  * `fda:DeviceListingReactivation`

**Modeling note**

**Registration and listing should be modeled separately.** §807.21 explicitly distinguishes establishment registration information from device listing information, while §807.28 defines listing-specific lifecycle behavior. ([Cornell Law School][13])

---

## 2.8 Product Code

### Concept: Product Code

**Source**

* Regulation: 21 CFR §807.3(k)
* FDA Product Classification Database

**Regulatory text:**

> “Product code means the code used by FDA to identify the generic category of a device.”

**Context**

Product Code is part of FDA's device-classification and registration/listing information architecture.

**Ontology interpretation**

* Candidate Class: `fda:ProductCode`
* Candidate Object Property: `fda:hasProductCode`
* Candidate Data Property: `fda:codeValue`

**Modeling note**

Product Code is not a device identifier in the same sense as UDI-DI. It identifies a **generic regulatory category**, not necessarily a specific physical/model-level device.

([eCFR][1])

---

## 2.9 FDA Premarket Submission Number

### Concept: FDA Premarket Submission Number

**Source**

* Regulation: 21 CFR §807.3(w)

**Regulatory text:**

> “FDA premarket submission number means the number assigned by FDA to a premarket device submission”

**Context**

The regulation explicitly includes PMA, HDE, De Novo and 510(k) within the examples of submissions receiving such numbers. ([eCFR][1])

**Ontology interpretation**

* Candidate Class: `fda:PremarketSubmissionIdentifier`
* Candidate Object Property: `fda:identifiesSubmission`
* Candidate Data Property: `fda:identifierValue`

**Modeling note**

This should be modeled as a **submission identifier**, not as a device identifier or establishment identifier.

---

# 2.10 Device Classification

### Concept: Class

**Source**

* Regulation: 21 CFR §860.3

**Regulatory text:**

> “Class means one of the three categories of regulatory control for medical devices”

**Context**

The three classes correspond to different levels/forms of regulatory control.

**Ontology interpretation**

* Candidate Class: `fda:DeviceClassification`
* Candidate Individuals:

  * `fda:ClassI`
  * `fda:ClassII`
  * `fda:ClassIII`
* Candidate Object Property: `fda:hasClassification`

**Modeling note**

Classification is a regulatory characteristic of a device/type. It should not be represented merely as a numeric field because Class I/II/III carry different regulatory-control semantics.

([eCFR][2])

---

## 2.11 Class I

**Source:** 21 CFR §860.3(c)(1)

**Regulatory text:**

> “Class I means the class of devices that is subject only to the general controls”

**Ontology interpretation**

* Candidate Class: `fda:ClassI`
* Candidate superclass: `fda:DeviceClassification`

**Modeling note**

Class I is defined by regulatory controls rather than simply “low risk.” The latter is a common explanatory characterization but should not replace the regulatory definition.

([eCFR][2])

---

## 2.12 Class II

**Source:** 21 CFR §860.3(c)(2)

**Regulatory text:**

> “Class II means the class of devices that is or eventually will be subject to special controls.”

**Ontology interpretation**

* Candidate Class: `fda:ClassII`

**Modeling note**

Class II introduces special controls as an explicit regulatory-control construct.

([eCFR][2])

---

## 2.13 Class III

**Source:** 21 CFR §860.3(c)(3)

**Regulatory text:**

> “Class III means the class of devices for which premarket approval is or will be required”

**Ontology interpretation**

* Candidate Class: `fda:ClassIII`
* Candidate relationship: `fda:requiresPremarketApproval`

**Modeling note**

Class III therefore has a direct semantic relationship with PMA, but the ontology should not encode `ClassIII → PMA` as an unconditional universal rule without accounting for statutory exemptions and specific regulatory circumstances.

([eCFR][2])

---

# 2.14 510(k)

### Concept: Premarket Notification / 510(k)

**Source**

* 21 CFR §807.81
* 21 CFR §807.87
* FDA 510(k) page

**Regulatory text:**

> “Premarket notification submission”

**Context**

A qualifying person must submit a premarket notification before certain devices enter commercial distribution. §807.81 specifies conditions triggering the submission requirement, including first introduction and certain significant changes. ([Cornell Law School][14])

**Ontology interpretation**

* Candidate Class: `fda:PremarketNotification`
* Candidate subclass: `fda:PremarketSubmission`
* Candidate Object Property: `fda:submittedBy`
* Candidate Object Property: `fda:concernsDevice`
* Candidate Data Property: `fda:submissionNumber`
* Candidate Event: `fda:510kSubmission`

**Modeling note**

A 510(k) is not simply an “authorization.” It is a **premarket submission** whose regulatory decision can result in an SE determination and clearance.

---

# 2.15 Substantial Equivalence

### Concept: Substantial Equivalence

**Source**

* 21 U.S.C. §360c(i)
* FDA 510(k) guidance/pages

**Regulatory text:**

> “has the same intended use as the predicate device”

**Context**

Substantial equivalence is the central regulatory determination underlying the 510(k) pathway. The statutory definition also addresses technological characteristics and safety/effectiveness questions. 

**Ontology interpretation**

* Candidate Class: `fda:SubstantialEquivalenceDetermination`
* Candidate Object Property: `fda:comparesDeviceToPredicate`
* Candidate Object Property: `fda:hasSameIntendedUseAs`
* Candidate Event: `fda:SEDetermination`
* Candidate Data Property: `fda:determinationOutcome`

**Modeling note**

Substantial equivalence should be modeled as a **regulatory determination**, not as a permanent intrinsic property equivalent to “same device.”

---

# 2.16 Predicate Device

### Concept: Predicate Device

**Source**

* 21 U.S.C. §360c(i)
* FDA 510(k) materials

**Regulatory text:**

> “with respect to a device being compared to a predicate device”

**Context**

The predicate is the comparison reference used in a substantial-equivalence determination.

**Ontology interpretation**

* Candidate Class: `fda:PredicateDevice`
* Candidate Object Property: `fda:hasPredicateDevice`
* Candidate Relationship: `fda:subjectDevice → comparedWith → predicateDevice`

**Modeling note**

The ontology should represent the predicate relationship as contextual to a **particular 510(k)/SE determination**, rather than asserting that one device is universally a predicate of another.



---

# 2.17 510(k) Clearance

### Concept: Clearance

**Source**

* FDA 510(k) Submission Process

**Regulatory evidence**

FDA states that an SE decision is considered **“cleared.”** ([U.S. Food and Drug Administration][15])

**Ontology interpretation**

* Candidate Class: `fda:Clearance`
* Candidate Event: `fda:510kClearance`
* Candidate Object Property: `fda:clearsDevice`
* Candidate State: `fda:ClearedForCommercialDistribution`

**Modeling note**

Clearance is not synonymous with PMA approval.

The FDA's own terminology differentiates:

* 510(k) → SE determination → cleared
* PMA → approval
* HDE → approval/exemption
* De Novo → classification / marketing pathway

This distinction should be preserved in the ontology.

---

# 2.18 PMA

### Concept: Premarket Approval Application

**Source**

* 21 CFR §814.3(e)
* 21 CFR §814.20
* 21 U.S.C. §360e

**Regulatory text:**

> “PMA means any premarket approval application for a class III medical device”

**Context**

PMA is the application mechanism for obtaining premarket approval for applicable Class III devices. ([eCFR.io][16])

**Ontology interpretation**

* Candidate Class: `fda:PMA`
* Candidate subclass: `fda:PremarketApplication`
* Candidate Object Property: `fda:submittedBy`
* Candidate Object Property: `fda:seeksApprovalFor`
* Candidate Data Property: `fda:pmaNumber`
* Candidate Event: `fda:PMASubmission`

---

# 2.19 PMA Approval

### Concept: PMA Approval

**Source**

* 21 CFR Part 814
* 21 U.S.C. §360e
* FDA PMA database

**Context**

FDA's PMA system produces approval/denial decisions, and the FDA database represents PMA approval records and approval-order statements. ([U.S. Food and Drug Administration][17])

**Ontology interpretation**

* Candidate Class: `fda:PMAApproval`
* Candidate Event: `fda:PMAApproval`
* Candidate Object Property: `fda:approvesDevice`
* Candidate State: `fda:PMAApproved`

**Modeling note**

Approval is a regulatory decision associated with a PMA. It should not be generalized to mean every FDA market-access decision.

---

# 2.20 De Novo Classification

### Concept: De Novo Classification Request

**Source**

* 21 U.S.C. §360c(f)(2)
* 21 CFR §860.220
* FDA De Novo guidance

**Regulatory evidence**

FDA describes De Novo as a pathway for novel devices for which general controls or general and special controls can provide reasonable assurance of safety and effectiveness but for which there is no legally marketed predicate device. ([U.S. Food and Drug Administration][18])

**Ontology interpretation**

* Candidate Class: `fda:DeNovoRequest`
* Candidate subclass: `fda:PremarketSubmission`
* Candidate Object Property: `fda:requestsClassificationOf`
* Candidate Event: `fda:DeNovoClassificationDecision`
* Candidate State: `fda:ClassifiedThroughDeNovo`

**Modeling note**

De Novo is **not merely another marketing submission type**. Its primary legal semantic is classification, while the resulting classification may permit marketing. FDA explicitly describes it as a risk-based classification process and a marketing pathway. ([U.S. Food and Drug Administration][7])

---

# 2.21 Humanitarian Use Device / HDE

### Concept: HUD

**Source**

* 21 CFR §814.3(n)
* 21 CFR §814.100
* 21 U.S.C. §360j(m)

**Regulatory text:**

> “HUD (humanitarian use device) means a medical device intended to benefit patients”

**Context**

The HUD designation is linked to diseases/conditions affecting not more than 8,000 individuals annually. The HDE mechanism provides marketing approval notwithstanding the absence of the ordinary reasonable-assurance-of-effectiveness requirement. ([Cornell Law School][19])

**Ontology interpretation**

* Candidate Class: `fda:HumanitarianUseDevice`
* Candidate Event: `fda:HUDDesignation`
* Candidate Object Property: `fda:hasHUDDesignation`

---

### Concept: HDE

**Source**

* 21 CFR §§814.3(m), 814.100

**Regulatory evidence**

HDE is an application seeking a humanitarian device exemption.

**Ontology interpretation**

* Candidate Class: `fda:HDE`
* Candidate subclass: `fda:PremarketApplication`
* Candidate Event: `fda:HDEApproval`
* Candidate State: `fda:HDEApproved`

**Important ambiguity**

Current statutory and regulatory materials use the 8,000-person threshold. Older HDE materials may contain the historical 4,000-person threshold. The FDA explicitly states that the threshold was changed from fewer than 4,000 to not more than 8,000 by the 21st Century Cures Act. ([U.S. Food and Drug Administration][20])

Therefore historical source versions must not be silently normalized.

---

# 2.22 IDE

### Concept: Investigational Device Exemption

**Source**

* 21 CFR §§812.1–812.3
* 21 U.S.C. §360j(g)

**Regulatory text:**

> “An approved investigational device exemption (IDE) permits a device”

**Context**

IDE concerns lawful investigation of devices and creates exemptions from specified statutory/regulatory requirements during investigation. It is therefore fundamentally different from a commercial-market authorization. ([eCFR][3])

**Ontology interpretation**

* Candidate Class: `fda:IDE`
* Candidate subclass: `fda:RegulatoryExemption`
* Candidate Object Property: `fda:authorizesInvestigationOf`
* Candidate Event: `fda:IDEApproval`
* Candidate State: `fda:InvestigationalAuthorization`

**Modeling note**

IDE should not be modeled as a market authorization.

---

# 2.23 Sponsor

### Concept: Sponsor

**Source**

* 21 CFR §812.3(n)

**Regulatory text:**

> “Sponsor means a person who initiates, but who does not actually conduct, the investigation”

**Ontology interpretation**

* Candidate Class: `fda:Sponsor`
* Candidate Object Property: `fda:initiatesInvestigation`
* Candidate Object Property: `fda:hasInvestigator`

**Modeling note**

Sponsor is an investigational role and should not automatically be equated with applicant, manufacturer or marketing-authorization holder.

([Cornell Law School][21])

---

# 2.24 Investigator

### Concept: Investigator

**Source**

* 21 CFR §812.3(i)

**Regulatory text:**

> “Investigator means an individual who actually conducts a clinical investigation”

**Ontology interpretation**

* Candidate Class: `fda:Investigator`
* Candidate Object Property: `fda:conductsInvestigation`

**Modeling note**

The regulation makes investigator an individual role, which is particularly important when modeling organizational actors.

([Cornell Law School][21])

---

# 2.25 UDI

### Concept: Unique Device Identifier

**Source**

* 21 CFR §801.40
* FDA UDI Basics

**Regulatory evidence**

FDA describes UDI as comprising a device identifier and, where applicable, production identifier. ([U.S. Food and Drug Administration][8])

**Ontology interpretation**

* Candidate Class: `fda:UDI`
* Candidate Object Property: `fda:hasDeviceIdentifier`
* Candidate Object Property: `fda:hasProductionIdentifier`

---

# 2.26 Device Identifier

### Concept: DI

**Source**

* FDA UDI Basics
* 21 CFR Part 830

**Regulatory evidence**

FDA identifies DI as the mandatory fixed portion of UDI and states that it identifies the labeler and specific version/model. FDA explicitly distinguishes DI (the fixed, model-level device identifier) from PI (production-level variable data such as lot, batch, or serial number). FDA guidance and 21 CFR Part 830 indicate that GUDID captures DI-level metadata while production identifiers (PIs) are not stored in GUDID. Ontology-relevant observations:  
- DI should be modelled as a device-model identifier (DeviceIdentifier / UDI-DI) distinct from ProductionIdentifier (PI / UDI-PI).  
- DI functions as a registry key within GUDID; PI is associated with production/instance events and should be modelled as production-identification data attached to productionEvent or deviceInstance.  
- ProductCode is a separate regulatory classification code and should not be conflated with DI.  
([U.S. Food and Drug Administration][8]; 21 CFR Part 830).

**Ontology interpretation**

* Candidate Class: `fda:DeviceIdentifier`
* Candidate Object Property: `fda:identifiesDeviceModel`
* Candidate Object Property: `fda:identifiesLabeler`
* Candidate Data Property: `fda:identifierValue`

---

# 2.27 Production Identifier

### Concept: PI

**Source**

* FDA UDI Basics
* 21 CFR §801.40

**Regulatory evidence**

PI can encode production information such as lot/batch, serial number, manufacturing date or expiration date. ([U.S. Food and Drug Administration][8])

**Ontology interpretation**

* Candidate Class: `fda:ProductionIdentifier`
* Candidate subclasses:

  * `fda:LotNumber`
  * `fda:SerialNumber`
  * `fda:ManufacturingDate`
  * `fda:ExpirationDate`

**Modeling note**

PI should not be treated as equivalent to DI. DI identifies the device/model-level identity, while PI represents variable production information.

---

# 2.28 GUDID

### Concept: Global Unique Device Identification Database

**Source**

* FDA GUDID guidance
* FDA GUDID page

**Regulatory evidence**

FDA describes GUDID as an FDA-administered database/reference catalog containing device identification information and specifically states that GUDID contains DI-level records (device-model identification) rather than production identifiers (PIs). Ontology-relevant observations:  
- Model GUDID as a regulatory information system (Registry) and GUDID records as data records (GUDIDRecord) that reference DeviceIdentifier (DI).  
- Do not model the registry itself as a DeviceIdentifier; instead model the relation: GUDID contains → GUDIDRecord; GUDIDRecord references → DeviceIdentifier (DI).  
- Because GUDID omits PI values, production identifiers must be linked to production events or device-instance artefacts, not to GUDID records.  
([U.S. Food and Drug Administration][9]; FDA GUDID guidance).

**Ontology interpretation**

* Candidate Class: `fda:GUDID`
* Candidate Class: `fda:GUDIDRecord`
* Candidate Object Property: `fda:containsDeviceIdentifierRecord`
* Candidate Object Property: `fda:referencesDevice`

**Modeling note**

GUDID is best modeled as a **regulatory information system/database**, while a GUDID record is a regulatory data record. It should not itself be modeled as a device identifier.

---

# 3. RELATIONSHIPS

| Subject          | Relationship                          | Object                      | Type                                       | Source                         |
| ---------------- | ------------------------------------- | --------------------------- | ------------------------------------------ | ------------------------------ |
| Owner/Operator   | registers                             | Establishment               | Explicit                                   | 21 CFR §807.20                 |
| Owner/Operator   | submits listing information for       | Device                      | Explicit                                   | 21 CFR §807.20                 |
| Establishment    | performs                              | Device Activity             | Explicit                                   | 21 CFR §§807.3, 807.20         |
| Establishment    | manufactures                          | Device                      | Explicit                                   | 21 CFR §§807.3, 807.25         |
| Establishment    | develops specifications for           | Device                      | Explicit                                   | 21 CFR §§807.3, 807.25         |
| Establishment    | repackages                            | Device                      | Explicit                                   | 21 CFR §§807.20, 807.25        |
| Establishment    | relabels                              | Device                      | Explicit                                   | 21 CFR §§807.20, 807.25        |
| Establishment    | lists                                 | Device                      | Explicit                                   | 21 CFR §§807.20–807.28         |
| Device Listing   | has                                   | Product Code                | Explicit                                   | 21 CFR §807.25                 |
| Device Listing   | references                            | Premarket Submission Number | Explicit                                   | 21 CFR §807.25                 |
| Device Listing   | has                                   | Listing Number              | Explicit                                   | 21 CFR §807.28                 |
| 510(k)           | concerns                              | Device                      | Explicit / regulatory structure            | 21 CFR §§807.81–807.87         |
| 510(k)           | compares subject device with          | Predicate Device            | Explicit                                   | 21 U.S.C. §360c(i); FDA 510(k) |
| FDA              | determines                            | Substantial Equivalence     | Explicit                                   | 21 U.S.C. §360c(i)             |
| SE determination | results in                            | Clearance                   | Explicit FDA terminology                   | FDA 510(k)                     |
| PMA              | seeks approval for                    | Class III Device            | Explicit                                   | 21 CFR Part 814                |
| FDA              | approves                              | PMA                         | Explicit                                   | 21 CFR Part 814                |
| PMA Approval     | authorizes marketing of               | Device                      | Regulatory interpretation supported by FDA | 21 U.S.C. §360e; FDA PMA       |
| De Novo Request  | requests classification of            | Device                      | Explicit                                   | 21 CFR §860.220                |
| De Novo decision | classifies                            | Device                      | Explicit                                   | 21 CFR Part 860                |
| HUD designation  | designates                            | Device                      | Explicit                                   | 21 CFR §814.100                |
| HDE              | seeks humanitarian exemption/approval | HUD                         | Explicit                                   | 21 CFR Part 814                |
| IDE              | authorizes investigation of           | Investigational Device      | Explicit                                   | 21 CFR §812.1                  |
| Sponsor          | initiates                             | Investigation               | Explicit                                   | 21 CFR §812.3                  |
| Investigator     | conducts                              | Investigation               | Explicit                                   | 21 CFR §812.3                  |
| Labeler          | submits                               | GUDID information           | Explicit                                   | FDA UDI / 21 CFR Part 830      |
| UDI              | contains                              | DI                          | Explicit                                   | 21 CFR §801.40                 |
| UDI              | may contain                           | PI                          | Explicit                                   | 21 CFR §801.40                 |
| GUDID            | contains                              | DI record                   | Explicit                                   | FDA GUDID                      |

### Important inferred relationships

**Inferred relationship 1**

`Establishment → associatedWith → Owner/Operator`

Reason: §807.25 requires registration information for both the establishment and owner/operator. The source structure supports modeling the two as distinct entities connected by responsibility/ownership, but the exact preferred property semantics are an ontology design question.

**Inferred relationship 2**

`DeviceListing → associatedWith → Establishment`

This follows from §807.25, which requires the current registration number and name of establishments where the device is manufactured, repackaged, relabeled, processed or specifications are developed. ([eCFR][1])

**Inferred relationship 3**

`PremarketSubmission → hasIdentifier → FDA Premarket Submission Number`

The regulation explicitly defines the number but the property name is an ontology modeling decision.

---

# 4. REGULATORY BUSINESS RULES

## Rule R01 — Registration eligibility

**Regulatory text**

21 CFR §807.20 requires qualifying owners/operators of establishments engaged in specified device activities to register and submit listing information. ([eCFR][1])

**Rule interpretation**

A registration obligation is conditional on the establishment/person performing specified activities and not falling within applicable exemptions.

**Potential representation**

* OWL restriction: `Establishment ⊓ performsSome(DeviceActivity) → RegistrationObligation`
* SHACL: qualifying establishment must have registration record
* Conditional constraint: exemptions must be evaluated before obligation
* Lifecycle rule: registration obligation precedes active regulatory registration status

---

## Rule R02 — Initial registration timing

**Source:** 21 CFR §807.22(a)

An establishment entering a qualifying operation for the first time must register within the specified 30-day period.

**Potential representation**

* Temporal constraint
* Event: `CommencementOfQualifyingActivity`
* Event: `InitialEstablishmentRegistration`
* Constraint: registration date within required period

---

## Rule R03 — Annual registration

**Source:** 21 CFR §807.22(b)(1)

Annual registration is required for establishments.

**Potential representation**

* SHACL temporal validation
* recurring lifecycle obligation
* registration-period state

---

## Rule R04 — Registration information update

**Source:** 21 CFR §807.22(b)(2)

Specified registration information must be updated within 30 days after a change.

**Potential representation**

`RegistrationInformationChange → requires → RegistrationUpdate`

---

## Rule R05 — Annual listing review

**Source:** 21 CFR §807.22(b)(3)

Device listing information must be reviewed and updated annually, including confirmation of accuracy.

**Potential representation**

* recurring validation event
* `ListingReview`
* `ListingAccuracyConfirmation`

---

## Rule R06 — Listing discontinuation

**Source:** 21 CFR §807.28(d)

When commercial distribution of a listed device is discontinued, the listing is discontinued under the specified conditions. ([Customs Mobile][22])

**Potential representation**

* Event: `DeviceListingDiscontinuation`
* State transition:

  * `ActiveListing → DiscontinuedListing`

---

## Rule R07 — Listing reactivation

**Source:** 21 CFR §807.28(e)

If commercial distribution resumes, the previously discontinued listing is reactivated.

**Potential representation**

* Event: `DeviceListingReactivation`
* State transition:

  * `DiscontinuedListing → ActiveListing`

This is particularly relevant for temporal ontology modeling.

---

## Rule R08 — Foreign establishment listing

**Source:** 21 CFR §807.28(c)

Foreign-establishment listings must be submitted before importation or offer for import.

**Potential representation**

`ForeignEstablishment + DeviceListing → prerequisiteFor → Import`

This is a strong candidate for a conditional SHACL rule.

---

## Rule R09 — 510(k) submission trigger

**Source:** 21 CFR §807.81

A premarket notification submission is required for specified devices before commercial distribution, subject to stated exceptions. ([Cornell Law School][14])

**Potential representation**

* conditional submission obligation
* `Device → requiresPremarketNotification`
* exception logic for PMA/De Novo/PCCP/etc.

---

## Rule R10 — Substantial equivalence

**Source:** 21 U.S.C. §360c(i)

A substantial-equivalence determination evaluates intended use and technological characteristics, with additional statutory criteria where technological characteristics differ. 

**Potential representation**

* `SEDetermination` must reference:

  * subject device
  * predicate device
  * intended use
  * technological characteristics
  * safety/effectiveness evidence
  * determination result

This is a strong candidate for a **reified relationship/event**, rather than a simple binary `isSubstantiallyEquivalentTo` property.

---

## Rule R11 — Class III / PMA

**Source:** 21 U.S.C. §360e

Applicable Class III devices require PMA approval unless an applicable exemption applies. 

**Potential representation**

* conditional OWL restriction
* SHACL validation
* exception mechanism for IDE or other statutory conditions

---

## Rule R12 — De Novo classification outcome

**Source:** 21 CFR §860.220; FDA De Novo

A De Novo request can result in classification into Class I or Class II when the statutory criteria are satisfied. ([Cornell Law School][23])

**Potential representation**

`DeNovoDecision → classifiesDeviceAs → ClassI|ClassII`

This should not be represented as equivalent to PMA approval.

---

## Rule R13 — IDE exemption

**Source:** 21 CFR §812.1

An approved/considered-approved IDE exempts a device from specified requirements during investigation. ([eCFR][3])

**Potential representation**

`IDE → createsRegulatoryExemption → DeviceRequirement`

This is a particularly important candidate for a rule/exemption ontology pattern.

---

## Rule R14 — GUDID submission

**Source:** FDA UDI / 21 CFR Part 830

Labelers must provide required device identification information for applicable device versions/models. ([U.S. Food and Drug Administration][8])

**Potential representation**

`Labeler + UDI-bearingDevice → hasGUDIDSubmissionObligation`

---

# 5. LIFECYCLE EVENTS AND STATES

## 5.1 Registration lifecycle

### Events

1. `EstablishmentRegistration`
2. `RegistrationUpdate`
3. `AnnualRegistrationReview`
4. `RegistrationFailure`

### Candidate states

* `Unregistered`
* `Registered`
* `RegistrationPendingUpdate`
* `FailedToRegister`
* `Inactive`

**Source:** 21 CFR §§807.20–807.22. ([eCFR][1])

---

# 5.2 Device listing lifecycle

### Events

1. `DeviceListingCreation`
2. `DeviceListingUpdate`
3. `DeviceListingDiscontinuation`
4. `DeviceListingReactivation`

### Candidate states

`NotListed → Listed → Discontinued → Reactivated`

This is directly supported by §807.28. ([Customs Mobile][22])

---

# 5.3 510(k) lifecycle

### Events

1. `510kSubmission`
2. `510kReview`
3. `SEDetermination`
4. `NSEDetermination`
5. `510kClearance`

### Candidate states

* `Submitted`
* `UnderReview`
* `SubstantiallyEquivalent`
* `NotSubstantiallyEquivalent`
* `Cleared`

FDA explicitly describes SE and NSE as 510(k) decision outcomes and identifies an SE 510(k) as cleared. ([U.S. Food and Drug Administration][15])

---

# 5.4 PMA lifecycle

### Events

1. `PMASubmission`
2. `PMAFiling`
3. `PMASubstantiveReview`
4. `PMAApproval`
5. `PMADenial`
6. `PMAWithdrawal`
7. `PMAApprovalWithdrawal`

### Candidate states

* `Pending`
* `Filed`
* `UnderReview`
* `Approved`
* `Denied`
* `Withdrawn`
* `ApprovalWithdrawn`

FDA's PMA review process explicitly separates filing, substantive review, panel review and final decision. ([U.S. Food and Drug Administration][24])

---

# 5.5 De Novo lifecycle

### Events

1. `DeNovoRequestSubmission`
2. `DeNovoReview`
3. `DeNovoGrant`
4. `DeNovoDecline`
5. `DeNovoWithdrawal`

### Result

`Device → classifiedAs → ClassI/ClassII`

FDA explicitly identifies accepting, granting, declining and withdrawing De Novo requests as distinct processes. ([U.S. Food and Drug Administration][7])

---

# 5.6 HDE lifecycle

### Events

1. `HUDDesignation`
2. `HDESubmission`
3. `HDEApproval`
4. `HDEDenial`
5. `HDEWithdrawal`

### Candidate state

`HUD → HDEApproved → HumanitarianMarketingStatus`

The regulation explicitly separates HUD designation from subsequent HDE submission. ([Cornell Law School][19])

---

# 5.7 IDE lifecycle

### Events

1. `IDEApplication`
2. `IDEApproval`
3. `Investigation`
4. `IDETermination`

### Candidate states

* `Investigational`
* `IDEApproved`
* `InvestigationTerminated`

The definition of termination specifically refers to discontinuance by the sponsor or withdrawal of IRB/FDA approval. ([Cornell Law School][21])

---

# 6. ACTORS AND ROLES

| Actor / Role            | Regulatory meaning                                               | Ontology candidate           |
| ----------------------- | ---------------------------------------------------------------- | ---------------------------- |
| Owner/Operator          | Entity directly responsible for establishment activities         | `fda:OwnerOperator`          |
| Establishment           | Physical business location under one management                  | `fda:Establishment`          |
| Manufacturer            | Role/activity defined through device manufacturing framework     | `fda:ManufacturerRole`       |
| Specification Developer | Initiates/develops specifications for second-party manufacturing | `fda:SpecificationDeveloper` |
| Initial Importer        | U.S. importer role with specific Part 807 definition             | `fda:InitialImporter`        |
| Importer                | U.S. company/individual associated with foreign device import    | `fda:Importer`               |
| Wholesale Distributor   | Distributor role distinct from manufacturer/initial importer     | `fda:WholesaleDistributor`   |
| Official Correspondent  | Designated FDA contact for establishment registration/listing    | `fda:OfficialCorrespondent`  |
| Applicant               | Party submitting PMA/HDE etc.                                    | `fda:Applicant`              |
| Requester               | Party submitting De Novo request                                 | `fda:Requester`              |
| Sponsor                 | Party initiating investigation                                   | `fda:Sponsor`                |
| Investigator            | Individual conducting investigation                              | `fda:Investigator`           |
| FDA                     | Regulatory authority                                             | `fda:FDA`                    |
| Classification Panel    | Advisory/classification role                                     | `fda:ClassificationPanel`    |

### Critical modeling observation

**Manufacturer ≠ Establishment**

The strongest evidence is §807.3's separate definition of establishment and the requirement that listing information identify establishments where manufacturing, repackaging, relabeling, processing or specification development occurs. ([eCFR][1])

Therefore:

```text
Organization
   ├── may have role → Manufacturer
   ├── may have role → SpecificationDeveloper
   └── may own/operator → Establishment
```

is currently a **modeling hypothesis**, while:

```text
Establishment ≠ Manufacturer
```

is strongly supported by the regulatory structure.

---

# 7. IDENTIFIERS, REGISTRATIONS AND REFERENCES

| Identifier / Record               | Identifies                                 | Assigned/managed by                       | Semantic category                             |
| --------------------------------- | ------------------------------------------ | ----------------------------------------- | --------------------------------------------- |
| Establishment Registration Number | Establishment registration                 | FDA                                       | Registration identifier                       |
| Listing Number                    | Device listing                             | FDA                                       | Regulatory record identifier                  |
| Product Code                      | Generic device category                    | FDA                                       | Regulatory classification/category identifier |
| 510(k) Number                     | 510(k) submission                          | FDA                                       | Submission identifier                         |
| PMA Number                        | PMA application                            | FDA                                       | Submission/application identifier             |
| HDE Number                        | HDE application                            | FDA                                       | Submission/application identifier             |
| De Novo Number                    | De Novo request                            | FDA                                       | Submission/request identifier                 |
| IDE identifier                    | IDE submission/exemption                   | FDA                                       | Investigational submission identifier         |
| UDI                               | Device/model + production information      | Issuing agency system under FDA framework | Device identifier                             |
| DI                                | Labeler + specific version/model           | Issuing agency                            | Device identifier                             |
| PI                                | Production characteristics                 | Labeler/UDI system                        | Production identifier                         |
| GUDID record                      | Device identification record               | FDA                                       | Database record                               |
| Regulation Number                 | Device regulatory classification provision | FDA/CFR                                   | Regulatory reference                          |

### Important distinction

`ProductCode` and `UDI-DI` should **not** be merged.

The FDA defines Product Code as identifying a generic category of device, whereas DI identifies a specific version/model and labeler. ([eCFR][1])

Likewise:

```text
510(k) Number ≠ Device Identifier
PMA Number ≠ Device Identifier
Listing Number ≠ Device Identifier
Registration Number ≠ Device Identifier
Product Code ≠ Device Identifier
```

These should remain distinct identifier classes.

---

# 8. REGULATORY PATHWAYS

| Pathway | Primary semantic                | Submission             | Decision/result              | Market-access role                               |
| ------- | ------------------------------- | ---------------------- | ---------------------------- | ------------------------------------------------ |
| 510(k)  | Substantial-equivalence pathway | Premarket Notification | SE/NSE                       | SE → clearance                                   |
| PMA     | Premarket approval              | PMA                    | Approval/denial              | Approval                                         |
| De Novo | Classification pathway          | De Novo Request        | Class I/II classification    | May enable marketing                             |
| HDE     | Humanitarian exemption/approval | HDE                    | Approval/denial              | Humanitarian marketing                           |
| IDE     | Investigational pathway         | IDE                    | Approval/considered approval | Investigation, not ordinary commercial marketing |

### 510(k)

FDA describes 510(k) as a premarket submission demonstrating substantial equivalence to a legally marketed device. ([U.S. Food and Drug Administration][5])

**Ontology category candidate:** `PremarketNotification`

---

### PMA

PMA is the premarket approval mechanism applicable to relevant Class III devices. 

**Ontology category candidate:** `PremarketApprovalApplication`

---

### De Novo

De Novo is explicitly a classification process that can provide a marketing pathway for novel Class I/II devices without a legally marketed predicate. ([U.S. Food and Drug Administration][7])

**Ontology category candidate:** `ClassificationRequest`

---

### HDE

HDE provides a humanitarian exemption/approval mechanism and is structurally distinct from ordinary PMA. The regulation explicitly states that HDE marketing approval involves HUD designation followed by HDE submission. ([Cornell Law School][19])

**Ontology category candidate:** `HumanitarianMarketingAuthorization`

---

### IDE

IDE is an investigational exemption and is structurally distinct from commercial-market authorization. ([eCFR][3])

**Ontology category candidate:** `InvestigationalExemption`

---

# 9. MODELING NOTES

## 9.1 Ambiguous concepts

### Manufacturer vs Establishment

**Question:** Is Manufacturer an organization, a role, an activity, or a regulatory designation?

**Evidence:** Part 807 separately defines establishment and manufacturing activity.

**Current decision:** Do not collapse.

---

### Registration vs Listing

**Question:** Is listing a subtype of registration?

**Evidence:** §§807.21–807.28 treat establishment registration and device listing as distinct information and lifecycle mechanisms.

**Current decision:** Model separately.

---

### Clearance vs Approval

**Question:** Can both be represented as subclasses of `MarketingAuthorization`?

Potentially, but this is an ontology abstraction rather than FDA terminology.

FDA uses:

```text
510(k) → SE → cleared
PMA → approved
HDE → approved
De Novo → classified
IDE → investigational exemption
```

These should remain distinct at the FDA layer.

---

### Approval vs Authorization

The term **authorization** appears at a higher abstraction level in FDA materials, particularly for De Novo and other mechanisms. It should not automatically replace the legally specific terms `approval`, `clearance`, `classification`, or `exemption`.

---

### Device vs Product

FDA regulatory sources frequently use “device,” while database interfaces may use product-oriented terminology.

**Current modeling position:** retain `Device` as the regulatory concept and treat `Product` as a potential broader ontology abstraction only in a later design phase.

---

### Applicant vs Manufacturer

PMA §814.20 explicitly requires an applicant. 510(k) materials refer to submitter/applicant-like roles. Registration rules separately refer to owner/operator/manufacturer/specification developer.

**Current decision:** do not assume:

```text
Applicant = Manufacturer
```

---

### Submission vs Authorization

A submission is an input/request to FDA.

A regulatory decision/authorization is an outcome.

Therefore:

```text
PremarketSubmission
        ↓
FDA Review
        ↓
RegulatoryDecision
        ↓
RegulatoryStatus
```

is a much stronger modeling pattern than:

```text
Submission = Authorization
```

---

# 10. REGULATORY PATHWAY DIFFERENCES

## 510(k)

Core semantic:

```text
Device
   ↓
Premarket Notification
   ↓
Substantial Equivalence Determination
   ↓
SE
   ↓
Clearance
```

Predicate relationship is central.

---

## PMA

Core semantic:

```text
Class III Device
   ↓
PMA
   ↓
Scientific / regulatory review
   ↓
Approval / denial
```

Safety/effectiveness evidence is central.

---

## De Novo

Core semantic:

```text
Novel Device
   ↓
De Novo Request
   ↓
Risk-based classification
   ↓
Class I / Class II
```

Classification is central.

---

## HDE

Core semantic:

```text
Device
   ↓
HUD Designation
   ↓
HDE
   ↓
Humanitarian Approval
```

Rare-disease/condition eligibility and humanitarian exemption are central.

---

## IDE

Core semantic:

```text
Investigational Device
   ↓
IDE
   ↓
Investigation
```

The resulting legal effect is exemption for specified investigational requirements rather than ordinary commercial market authorization.

---

# 11. POTENTIAL CROSS-DOMAIN ABSTRACTIONS

These are **not FDA concepts yet**. They are candidate abstractions to consider only in the later ontology-design phase.

### Regulatory Actor

Potential superclass:

```text
RegulatoryActor
├── ManufacturerRole
├── SpecificationDeveloper
├── Importer
├── InitialImporter
├── Applicant
├── Sponsor
├── Investigator
└── RegulatoryAuthority
```

### Regulatory Submission

Potential superclass:

```text
RegulatorySubmission
├── PremarketNotification
├── PMA
├── DeNovoRequest
├── HDE
└── IDE
```

**Warning:** This abstraction is useful structurally but does not imply that all five have the same legal semantics.

### Regulatory Decision

Potential superclass:

```text
RegulatoryDecision
├── SubstantialEquivalenceDecision
├── PMAApproval
├── PMADenial
├── DeNovoClassificationDecision
├── HDEApproval
└── IDEApproval
```

### Regulatory Identifier

Potential superclass:

```text
RegulatoryIdentifier
├── RegistrationNumber
├── ListingNumber
├── PremarketSubmissionNumber
├── ProductCode
├── UDI
├── DeviceIdentifier
└── ProductionIdentifier
```

Again, this is a modeling abstraction, not FDA terminology.

---

# 12. RESEARCH QUALITY CHECK

| Requirement                                             | Status |
| ------------------------------------------------------- | ------ |
| Every major extracted concept has source evidence       | ✓      |
| Primary legal/regulatory sources prioritized            | ✓      |
| FDA official sources used for terminology clarification | ✓      |
| CFR sections identified                                 | ✓      |
| Statutory provisions identified where relevant          | ✓      |
| Regulatory text separated from ontology interpretation  | ✓      |
| Registration/listing distinction preserved              | ✓      |
| Clearance/approval distinction preserved                | ✓      |
| Submission/decision distinction preserved               | ✓      |
| 510(k)/PMA/De Novo/HDE/IDE distinguished                | ✓      |
| Inferred relationships explicitly identified            | ✓      |
| Company-specific workflow excluded                      | ✓      |
| Unsupported concepts avoided                            | ✓      |
| Historical/current HDE threshold ambiguity recorded     | ✓      |
| Product Code/UDI distinction preserved                  | ✓      |
| Manufacturer/Establishment distinction preserved        | ✓      |

---

# 13. KEY ONTOLOGY DESIGN SIGNALS FOR THE NEXT PHASE

The strongest findings from this FDA research are not individual classes such as `Manufacturer` or `PMA`. They are the **structural patterns** in FDA's regulatory model.

### 1. FDA separates the physical/operational establishment from the responsible organization

```text
Organization / Owner-Operator
             │
             └── Establishment
                    │
                    ├── Manufacturing
                    ├── Repackaging
                    ├── Relabeling
                    ├── Specification Development
                    └── Other Device Activities
```

### 2. Registration and listing are separate regulatory records

```text
Establishment
      │
      └── Establishment Registration

Device
      │
      └── Device Listing
             │
             ├── Establishment
             ├── Activity
             ├── Product Code
             └── Premarket Submission Number
```

This distinction is strongly supported by §§807.20–807.28. ([eCFR][1])

### 3. FDA market access is not a single concept

A useful FDA-layer model is:

```text
                    Regulatory Submission
                           │
          ┌────────────────┼─────────────────┐
          ↓                ↓                 ↓
       510(k)             PMA             De Novo
          │                │                 │
          ↓                ↓                 ↓
         SE             Approval         Classification
          │                │                 │
          ↓                ↓                 ↓
      Clearance         Approved        Class I / II
```

with HDE and IDE maintained as separate pathways.

### 4. Regulatory relationships often need reification

For example, rather than:

```text
Device A ──isPredicateOf──> Device B
```

a better future ontology structure may be:

```text
510(k) Submission
    │
    ├── concerns → Subject Device
    ├── comparesWith → Predicate Device
    ├── evaluates → Intended Use
    ├── evaluates → Technological Characteristics
    └── resultsIn → SE Determination
                         │
                         └── resultsIn → Clearance
```

This is supported by the statutory structure of substantial equivalence. 

### 5. Lifecycle state should be modeled separately from regulatory event

For example:

```text
Device Listing
    │
    ├── Listing Creation       → Listed
    ├── Listing Update         → Listed
    ├── Discontinuation        → Discontinued
    └── Reactivation           → Listed
```

rather than representing `Discontinued` as merely a Boolean.

### 6. Identifiers form different semantic layers

```text
Device
 ├── Product Code          → generic regulatory category
 ├── UDI
 │    ├── DI               → model/version identity
 │    └── PI               → production information
 │
 └── Regulatory records
      ├── Listing Number
      ├── 510(k) Number
      ├── PMA Number
      ├── HDE Number
      └── De Novo Number
```

FDA sources provide strong evidence that these identifiers should remain distinct. ([eCFR][1])

---

# 14. OPEN MODELING QUESTIONS TO CARRY FORWARD

1. Should `Manufacturer` be modeled as an **Organization Role**, `DeviceActivity`, or both?
2. What is the precise ontology relationship between `OwnerOperator` and `Establishment`?
3. Should `Registration` and `Listing` share a superclass such as `RegulatoryRecord`?
4. Should `Clearance`, `Approval`, `Classification`, and `Exemption` share a superclass such as `RegulatoryDecision`?
5. Should `MarketingAuthorization` be a higher-level abstraction or remain outside the FDA source layer?
6. Is `DeNovoClassification` simultaneously a classification decision and a market-access mechanism?
7. Should `HDEApproval` be modeled as an authorization, an exemption, an approval, or a compound regulatory construct?
8. Should `IDE` be represented as a submission, exemption, authorization, or all three through different classes?
9. Should `SubstantialEquivalence` be reified as a `Determination` rather than represented as a direct device-to-device property?
10. Should `ProductCode` be modeled as a classification identifier, a regulatory category, or both?
11. Is `RegulationNumber` a property of a `DeviceType`, `Classification`, or `RegulatoryProvision`?
12. How should historical regulatory statuses be represented when FDA changes classification or regulatory requirements?
13. How should a device with multiple premarket submissions be represented?
14. How should a device listing associated with multiple establishments and activities be represented?
15. How should supplements/amendments to PMA and other submissions be represented?
16. How should historical 4,000-person versus current 8,000-person HDE thresholds be modeled without overwriting historical legal meaning?

These questions should remain **open** for `02_concepts.md`, `03_design_decisions.md`, and `04_open_questions.md`.

---

## Final evidence hierarchy

The FDA research therefore supports the following modeling progression:

```text
FDA legal/regulatory source
        ↓
Regulatory concept
        ↓
Regulatory relationship
        ↓
Regulatory event / state
        ↓
Constraint / business rule
        ↓
Ontology candidate
        ↓
Later OWL / SHACL design
```

The critical point for the next phase is that **the ontology should not begin by creating a generic “FDA Medical Device” class hierarchy**. The source evidence instead suggests beginning with a graph of:

**Actor → Establishment → Activity → Device → Classification → Regulatory Record → Submission → Regulatory Decision → Regulatory Status → Identifier**

and only afterward deciding which of those concepts deserve reusable higher-level abstractions.

[1]: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-807 "eCFR :: 21 CFR Part 807 -- Establishment Registration and Device Listing for Manufacturers and Initial Importers of Devices"
[2]: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-860 "eCFR :: 21 CFR Part 860 -- Medical Device Classification Procedures"
[3]: https://www.ecfr.gov/current/title-21/chapter-I/subchapter-H/part-812 "eCFR :: 21 CFR Part 812 -- Investigational Device Exemptions"
[4]: https://www.fda.gov/medical-devices/device-registration-and-listing/who-must-register-list-and-pay-fee?utm_source=chatgpt.com "Who Must Register, List and Pay the Fee | FDA"
[5]: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-notification-510k?utm_source=chatgpt.com "Premarket Notification 510(k) | FDA"
[6]: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/premarket-approval-pma?utm_source=chatgpt.com "Premarket Approval (PMA) | FDA"
[7]: https://www.fda.gov/medical-devices/premarket-submissions-selecting-and-preparing-correct-submission/de-novo-classification-request?utm_source=chatgpt.com "De Novo Classification Request | FDA"
[8]: https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/udi-basics?utm_source=chatgpt.com "UDI Basics | FDA"
[9]: https://www.fda.gov/medical-devices/unique-device-identification-system-udi-system/global-unique-device-identification-database-gudid?utm_source=chatgpt.com "Global Unique Device Identification Database (GUDID) | FDA"
[10]: https://www.accessdata.fda.gov/SCRIPTs/cdrh/cfdocs/cfPCD/classification.cfm?utm_source=chatgpt.com "Product Classification"
[11]: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?id=K211900&utm_source=chatgpt.com "510(k) Premarket Notification"
[12]: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm?utm_source=chatgpt.com "Premarket Approval (PMA)"
[13]: https://www.law.cornell.edu/cfr/text/21/807.21?utm_source=chatgpt.com "21 CFR § 807.21 - How to register establishments and list devices. | Electronic Code of Federal Regulations (e-CFR) | US Law | LII / Legal Information Institute"
[14]: https://www.law.cornell.edu/cfr/text/21/807.81?utm_source=chatgpt.com "21 CFR § 807.81 - When a premarket notification submission is required. | Electronic Code of Federal Regulations (e-CFR) | US Law | LII / Legal Information Institute"
[15]: https://www.fda.gov/medical-devices/premarket-notification-510k/510k-submission-process?utm_source=chatgpt.com "510(k) Submission Process | FDA"
[16]: https://ecfr.io/Title-21/Section-814.3?utm_source=chatgpt.com "21 CFR 814.3 | Definitions. | eCFR.io"
[17]: https://www.fda.gov/medical-devices/device-approvals-and-clearances/pma-approvals?utm_source=chatgpt.com "PMA Approvals | FDA"
[18]: https://www.fda.gov/regulatory-information/search-fda-guidance-documents/de-novo-classification-process-evaluation-automatic-class-iii-designation?utm_source=chatgpt.com "De Novo Classification Process (Evaluation of Automatic Class III Designation) | FDA"
[19]: https://www.law.cornell.edu/cfr/text/21/814.100?utm_source=chatgpt.com "21 CFR § 814.100 - Purpose and scope. | Electronic Code of Federal Regulations (e-CFR) | US Law | LII / Legal Information Institute"
[20]: https://www.fda.gov/industry/medical-products-rare-diseases-and-conditions/humanitarian-use-device-hud-designation-program?utm_source=chatgpt.com "Humanitarian Use Device (HUD) Designation Program | FDA"
[21]: https://www.law.cornell.edu/cfr/text/21/812.3?utm_source=chatgpt.com "21 CFR § 812.3 - Definitions. | Electronic Code of Federal Regulations (e-CFR) | US Law | LII / Legal Information Institute"
[22]: https://www.customsmobile.com/regulations/expand/title21_chapterI-i7_part807_subpartB_section807.28?utm_source=chatgpt.com "21 CFR 807.28 - Updating device listing information."
[23]: https://www.law.cornell.edu/cfr/text/21/860.220?utm_source=chatgpt.com "21 CFR § 860.220 - De Novo request content. | Electronic Code of Federal Regulations (e-CFR) | US Law | LII / Legal Information Institute"
[24]: https://www.fda.gov/medical-devices/premarket-approval-pma/pma-review-process?utm_source=chatgpt.com "PMA Review Process | FDA"
