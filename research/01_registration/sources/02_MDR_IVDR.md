# MDR / IVDR — Registration & Market Authorization Domain Research

**Research artifact:** `research/registration/sources/02_MDR_IVDR.md`
**Jurisdiction:** European Union
**Primary domain:** Registration / Market Access / Economic Operators / Device Identification
**Regulatory instruments:** Regulation (EU) 2017/745 (MDR), Regulation (EU) 2017/746 (IVDR)

---

## 0. Research Scope and Evidence Policy

This document extracts ontology-relevant regulatory concepts from the EU medical device regulatory framework.

The research focuses on:

* regulatory entities and actors
* devices and device categories
* economic operators
* identifiers
* registrations
* EUDAMED
* conformity assessment
* certificates
* CE marking
* market access events
* regulatory lifecycle events
* regulatory relationships
* constraints and business rules

This is **not a regulatory summary**.

The distinction between evidence and interpretation is maintained as follows:

> **Regulatory text / source evidence** → what the legislation explicitly establishes
> **Ontology interpretation** → a candidate semantic representation for later ontology design

Where a relationship or abstraction is not directly established by the legislation, it is explicitly labelled as **Inferred relationship**, **Potential ontology relationship**, or **Modeling question**.

---

# 1. Source Documents

## 1.1 Primary legal sources

### Source S01 — MDR

**Document title:** Regulation (EU) 2017/745 of the European Parliament and of the Council of 5 April 2017 on medical devices

**Identifier:** Regulation (EU) 2017/745 (MDR)

**Issuing organization:** European Parliament and Council

**Source type:** Primary EU legislation

**Current consolidated version inspected:** 1 January 2026

**CELEX:** 02017R0745-20260101

**URL:** EUR-Lex consolidated MDR

[EUR-Lex — MDR consolidated text, current version](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02017R0745-20260101&utm_source=chatgpt.com)

The inspected consolidated text incorporates amendments including Regulation (EU) 2024/1860 and Regulation (EU) 2025/2457.

---

### Source S02 — IVDR

**Document title:** Regulation (EU) 2017/746 of the European Parliament and of the Council of 5 April 2017 on in vitro diagnostic medical devices

**Identifier:** Regulation (EU) 2017/746 (IVDR)

**Issuing organization:** European Parliament and Council

**Source type:** Primary EU legislation

**Current consolidated version inspected:** 10 January 2025

**CELEX:** 02017R0746-20250110

**URL:** EUR-Lex consolidated IVDR

[EUR-Lex — IVDR consolidated text](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A02017R0746-20250110&utm_source=chatgpt.com)

The consolidated IVDR incorporates amendments including Regulation (EU) 2024/1860.

---

## 1.2 European Commission sources

### Source S03 — European Commission UDI / Device Registration

**Title:** UDI/Device registration

**Issuing organization:** European Commission, Directorate-General for Health and Food Safety

**Source type:** Official European Commission implementation information

**URL:**

[European Commission — UDI/Device registration](https://health.ec.europa.eu/medical-devices-eudamed/udidevice-registration_en?utm_source=chatgpt.com)

The Commission states that MDR and IVDR introduce a device identification system based on UDI and that manufacturers submit UDI/device information to EUDAMED. The Commission page also records the transition to mandatory use of the UDI/Devices module from 28 May 2026.

---

### Source S04 — European Commission Actor Registration

**Title:** Actor registration module

**Issuing organization:** European Commission

**Source type:** Official EUDAMED implementation information

**URL:**

[European Commission — Actor registration module](https://health.ec.europa.eu/medical-devices-eudamed/actor-registration-module_en?utm_source=chatgpt.com)

The page describes the Actor Registration module, Actor ID/SRN, registration requests, competent-authority assessment, and EUDAMED actor registration.

---

### Source S05 — European Commission Guidance

**Title:** Guidance — MDCG endorsed documents and other guidance

**Issuing organization:** European Commission / MDCG

**Source type:** Official EU regulatory guidance index

**URL:**

[European Commission — MDCG guidance index](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en?utm_source=chatgpt.com)

The Commission explicitly describes MDCG guidance as non-legally-binding guidance intended to support consistent implementation of MDR/IVDR.

---

## 1.3 MDCG sources

### Source S06 — MDCG 2021-13 Rev.1

**Title:** Questions and answers on obligations and related rules for the registration in EUDAMED of actors other than manufacturers, authorised representatives and importers subject to the obligations of Article 31 MDR and Article 28 IVDR

**Identifier:** MDCG 2021-13 Rev.1

**Issuing organization:** Medical Device Coordination Group

**Publication:** July 2021

**Source type:** Official EU regulatory guidance

Referenced by the European Commission's Actor Registration module page.

---

### Source S07 — MDCG 2022-7

**Title:** Q&A on the Unique Device Identification system under Regulation (EU) 2017/745 and Regulation (EU) 2017/746

**Identifier:** MDCG 2022-7

**Publication:** May 2022

**Source type:** Official EU regulatory guidance

Referenced by the European Commission UDI guidance index.

---

### Source S08 — MDCG 2024-11

**Title:** Q&A on practical aspects related to the implementation of the gradual roll-out of EUDAMED

**Identifier:** MDCG 2024-11

**Source type:** Official EU regulatory guidance

The document addresses the practical implementation of the gradual EUDAMED roll-out and the interpretation of device/SPP registration in the UDI/DEV module.

---

# 2. Extracted Domain Concepts

## Concept: Medical Device

### Source

* Regulation / Document: MDR
* Exact reference: Article 2(1)
* URL: S01

### Regulatory text

> “medical device” means any instrument, apparatus, appliance, software, implant, reagent, material or other article intended by the manufacturer...

MDR Article 2(1) defines the concept through both the intended use specified by the manufacturer and the means by which the principal intended action is achieved. It also explicitly includes several additional product categories.

### Context

The MDR definition establishes `medical device` as a central regulatory classification concept. The definition is manufacturer-intent-dependent and is not simply equivalent to a physical product.

### Ontology interpretation

* Candidate Class: `mdr:MedicalDevice`
* Candidate Object Property: `mdr:hasIntendedPurpose`
* Candidate Object Property: `mdr:manufacturedBy`
* Candidate Data Property: `mdr:deviceName`
* Candidate Data Property: `mdr:tradeName`

### Modeling note

`MedicalDevice` should not automatically be treated as synonymous with every physical product. The legal definition incorporates intended purpose and regulatory classification.

---

## Concept: In Vitro Diagnostic Medical Device

### Source

* Regulation / Document: IVDR
* Exact reference: Article 2(2)
* URL: S02

### Regulatory text

IVDR defines an IVD as a medical device intended for in-vitro examination of specimens derived from the human body for specified informational purposes.

### Context

IVDR explicitly defines IVDs as a subset of medical devices and additionally specifies specimen receptacles as IVDs.

### Ontology interpretation

* Candidate Class: `ivdr:InVitroDiagnosticMedicalDevice`
* Candidate Object Property: `ivdr:examinesSpecimen`
* Candidate Object Property: `ivdr:hasIntendedPurpose`

### Modeling note

A potential subclass relationship with `MedicalDevice` is strongly supported because IVDR Article 2(1) directly references MDR Article 2(1).

**Potential ontology relationship:**

`InVitroDiagnosticMedicalDevice rdfs:subClassOf MedicalDevice`

This is an ontology interpretation rather than a direct OWL statement in the regulation.

---

## Concept: Accessory

### Source

* MDR: Article 2(2)
* IVDR: Article 2(4)

### Regulatory text

MDR and IVDR both define an accessory as an article that is not itself the regulated device but is intended for use with one or more particular devices to enable or support their intended functionality.

### Ontology interpretation

* Candidate Class: `mdr:Accessory`
* Candidate Object Property: `accessoryFor`
* Candidate Object Property: `supportsIntendedPurpose`

### Modeling note

Accessory is legally distinguished from Device. Do not automatically model it as a subclass of Device.

---

## Concept: Custom-made Device

### Source

* MDR: Article 2(3)
* IVDR: Article 2 contains the corresponding device terminology but does not reproduce an equivalent MDR custom-made-device framework in the same manner.

### Regulatory text

MDR Article 2(3) defines a custom-made device by reference to a written prescription, specific design characteristics, and exclusive use by a particular patient.

### Ontology interpretation

* Candidate Class: `mdr:CustomMadeDevice`
* Candidate Object Property: `hasPrescription`
* Candidate Object Property: `intendedForPatient`
* Candidate Object Property: `hasSpecificDesignCharacteristic`

### Modeling note

**MDR/IVDR distinction:** Do not assume a symmetric `CustomMadeDevice` class across MDR and IVDR without further source analysis.

---

## Concept: System

### Source

* MDR: Article 2(10)/(11) and Article 22

### Regulatory text

MDR defines a system as a combination of products intended to be interconnected or combined to achieve a specific medical purpose.

### Context

Systems have a special regulatory treatment under Article 22.

### Ontology interpretation

* Candidate Class: `mdr:System`
* Candidate Object Property: `hasComponent`
* Candidate Object Property: `hasMedicalPurpose`
* Candidate Event: `SystemAssembly`

### Modeling note

System is not necessarily equivalent to a physical device. Article 22 creates a distinct regulatory object with its own statement and conformity implications.

---

## Concept: Procedure Pack

### Source

* MDR: Article 2(10)
* MDR: Article 22

### Regulatory text

> “procedure pack” means a combination of products packaged together and placed on the market...

### Ontology interpretation

* Candidate Class: `mdr:ProcedurePack`
* Candidate Object Property: `containsProduct`
* Candidate Object Property: `hasSpecificMedicalPurpose`

### Modeling note

Procedure pack should be represented separately from `System` even though both are combination constructs.

---

## Concept: Intended Purpose

### Source

* MDR: Article 2(12)
* IVDR: Article 2(12)

### Regulatory text

Both regulations define intended purpose by reference to information supplied by the manufacturer, including labeling and instructions for use. IVDR additionally references performance evaluation.

### Ontology interpretation

* Candidate Class: `reg:IntendedPurpose`
* Candidate Object Property: `hasIntendedPurpose`
* Candidate Object Property: `specifiedBy`
* Candidate Object Property: `specifiedInLabel`
* Candidate Object Property: `specifiedInInstructionsForUse`

### Modeling note

`IntendedPurpose` is likely a central semantic object because it participates in:

* device definition
* classification
* conformity assessment
* labeling
* market access
* claims
* changes that may trigger manufacturer obligations

---

## Concept: Making Available on the Market

### Source

* MDR: Article 2(27)
* IVDR: Article 2(20)

### Regulatory text

> “making available on the market” means any supply of a device...

MDR Article 2(27) and IVDR Article 2(20) establish this as a supply event on the Union market in the course of commercial activity.

### Ontology interpretation

* Candidate Event: `MakingAvailableOnMarket`
* Candidate Object Property: `makesAvailable`
* Candidate Actor: `EconomicOperator`
* Candidate Object: `Device`
* Candidate Data Property: `eventDate`

### Modeling note

This is an event/process concept rather than simply a device state.

---

## Concept: Placing on the Market

### Source

* MDR: Article 2(28)
* IVDR: Article 2(21)

### Regulatory text

> “placing on the market” means the first making available of a device...

Both regulations explicitly distinguish placing on the market from making available.

### Ontology interpretation

* Candidate Event: `PlacingOnMarket`
* Candidate Object Property: `firstMakesAvailable`
* Candidate Data Property: `placingOnMarketDate`

### Modeling note

`PlacingOnMarket` must not be modeled as synonymous with `MakingAvailableOnMarket`.

The defining distinction is **first** making available.

---

## Concept: Putting into Service

### Source

* MDR: Article 2(29)
* IVDR: Article 2(22)

### Regulatory text

The regulations define this as the stage at which a device has first been made available to the final user as ready for use for its intended purpose.

### Ontology interpretation

* Candidate Event: `PuttingIntoService`
* Candidate Object Property: `hasFinalUser`
* Candidate Object Property: `concernsDevice`
* Candidate Data Property: `puttingIntoServiceDate`

### Modeling note

`PuttingIntoService` is temporally distinct from `PlacingOnMarket`.

---

## Concept: Manufacturer

### Source

* MDR: Article 2(30)
* IVDR: Article 2(23)

### Regulatory text

> “manufacturer” means a natural or legal person who manufactures or fully refurbishes a device...

Both regulations additionally capture the case where the person has the device designed/manufactured and markets it under its name or trademark.

### Ontology interpretation

* Candidate Class: `reg:Manufacturer`
* Candidate Object Property: `manufactures`
* Candidate Object Property: `marketsUnderName`
* Candidate Object Property: `hasTradeMark`

### Modeling note

Manufacturer is a **role-bearing legal actor**, not simply a company type.

---

## Concept: Authorised Representative

### Source

* MDR: Article 2(32)
* IVDR: Article 2(25)

### Regulatory text

> “authorised representative” means any natural or legal person established within the Union...

The role requires a written mandate from a manufacturer located outside the Union.

### Ontology interpretation

* Candidate Class: `reg:AuthorisedRepresentative`
* Candidate Object Property: `representsManufacturer`
* Candidate Object Property: `hasMandate`
* Candidate Object Property: `actsOnBehalfOf`

### Modeling note

The mandate is semantically important and should not be reduced to a simple organization-to-organization relation.

---

## Concept: Importer

### Source

* MDR: Article 2(33)
* IVDR: Article 2(26)

### Regulatory text

> “importer” means any natural or legal person established within the Union that places a device from a third country on the Union market.

### Ontology interpretation

* Candidate Class: `reg:Importer`
* Candidate Object Property: `placesOnMarket`
* Candidate Object Property: `importsFromThirdCountry`

---

## Concept: Distributor

### Source

* MDR: Article 2(34)
* IVDR: Article 2(27)

### Regulatory text

Both regulations define the distributor by its position in the supply chain and its activity of making the device available before putting into service.

### Ontology interpretation

* Candidate Class: `reg:Distributor`
* Candidate Object Property: `makesAvailable`
* Candidate Object Property: `suppliesDevice`

---

## Concept: Economic Operator

### Source

* MDR: Article 2(35)
* IVDR: Article 2(28)

### Regulatory text

MDR includes manufacturer, authorised representative, importer, distributor, and specified Article 22 persons. IVDR's definition lists manufacturer, authorised representative, importer and distributor.

### Ontology interpretation

* Candidate Class: `reg:EconomicOperator`
* Candidate Property: `hasEconomicOperatorRole`

### Modeling note

This is an important **MDR/IVDR divergence**.

MDR's definition explicitly includes persons referred to in Article 22(1) and 22(3), while IVDR does not use the same wording.

Therefore:

`EconomicOperator(MDR) ≠ EconomicOperator(IVDR)` as an assumption.

The shared superclass may be an ontology design decision for later analysis, but must not erase the regulatory distinction.

---

## Concept: Conformity Assessment

### Source

* MDR: Article 2(40)
* IVDR: Article 2(32)

### Regulatory text

> “conformity assessment” means the process demonstrating whether the requirements of this Regulation relating to a device have been fulfilled.

### Ontology interpretation

* Candidate Class: `reg:ConformityAssessment`
* Candidate Event: `ConformityAssessmentPerformed`
* Candidate Object Property: `assessesDevice`
* Candidate Object Property: `performedBy`
* Candidate Object Property: `resultsInCertificate`

### Modeling note

Conformity assessment should be modeled as a process/activity rather than merely a Boolean `isConform`.

---

## Concept: Notified Body

### Source

* MDR: Article 2(42)
* IVDR: Article 2(34)

### Regulatory text

> “notified body” means a conformity assessment body designated in accordance with this Regulation.

### Ontology interpretation

* Candidate Class: `reg:NotifiedBody`
* Candidate Object Property: `performsConformityAssessment`
* Candidate Object Property: `isDesignatedBy`
* Candidate Object Property: `hasDesignationScope`

### Modeling note

Notified Body is a regulatory role/status of a conformity assessment body, not merely an organization category.

---

## Concept: CE Marking

### Source

* MDR: Article 2(43)
* IVDR: Article 2(35)

### Regulatory text

> “CE marking of conformity” ... means a marking by which a manufacturer indicates that a device is in conformity...

### Ontology interpretation

* Candidate Class: `reg:CEMarking`
* Candidate Object Property: `indicatesConformityOf`
* Candidate Object Property: `appliedBy`
* Candidate Object Property: `associatedWithNotifiedBody`

### Modeling note

CE marking should not be modeled as equivalent to a certificate.

It is a **manufacturer indication of conformity**, whereas certificates are outputs of specified conformity assessment activities.

---

## Concept: UDI

### Source

* MDR: Article 27 and Annex VI
* IVDR: Article 24 and Annex VI

### Regulatory text

IVDR defines UDI as a series of numeric or alphanumeric characters created through internationally accepted device identification and coding standards allowing unambiguous identification of specific devices on the market.

### Ontology interpretation

* Candidate Class: `reg:UDI`
* Candidate Object Property: `identifiesDevice`
* Candidate Object Property: `assignedBy`
* Candidate Object Property: `issuedAccordingTo`

### Modeling note

UDI should be treated as an identifier construct, not as a device itself.

---

## Concept: Basic UDI-DI

### Source

* MDR: Article 29(1), Annex VI Part C
* IVDR: Article 26(1), Annex VI Part C

### Regulatory text

MDR and IVDR require assignment of a Basic UDI-DI before placing the relevant device on the market and require submission to the UDI database together with specified core data elements.

### Ontology interpretation

* Candidate Class: `reg:BasicUDIDI`
* Candidate Object Property: `identifiesDeviceGroup`
* Candidate Object Property: `assignedToDevice`
* Candidate Object Property: `providedToUDIDatabase`

### Modeling note

The Basic UDI-DI is not simply another identifier value. Its position in the regulatory information model is distinct from UDI-DI and UDI-PI.

---

## Concept: UDI-DI / UDI-PI

### Source

* MDR: Article 27, Annex VI
* IVDR: Article 24, Annex VI
* MDCG 2024-11

### Context

The regulations distinguish device-identification information from production-identification information.

MDCG 2024-11 further clarifies that EUDAMED UDI/DEV registration operates at the device-identifier level, while different production identifiers can exist under the same device registration.

### Ontology interpretation

* Candidate Class: `reg:UDIDI`
* Candidate Class: `reg:UDIPI`
* Candidate Object Property: `hasUDIDI`
* Candidate Object Property: `hasUDIPI`
* Candidate Object Property: `identifiesProduction`

### Modeling note

Do not collapse UDI-DI and UDI-PI into one generic `identifier`.

---

## Concept: Single Registration Number (SRN)

### Source

* MDR: Article 31(2)
* IVDR: Article 28(2)
* European Commission Actor Registration

### Regulatory text

MDR and IVDR provide that, after competent-authority verification of submitted registration data, the competent authority obtains a single registration number from the electronic system and issues it to the relevant economic operator.

### Ontology interpretation

* Candidate Class: `reg:SRN`
* Candidate Object Property: `identifiesEconomicOperator`
* Candidate Object Property: `issuedBy`
* Candidate Object Property: `obtainedThrough`

### Modeling note

SRN identifies an economic operator.

It must not be modeled as a device identifier.

The European Commission describes the Actor ID/SRN as an EU-wide unique identification for economic operators in the medical-device sector.

---

## Concept: EUDAMED

### Source

* MDR: Articles 33–34
* IVDR: Article 30
* European Commission EUDAMED pages

### Context

EUDAMED is the European Database on Medical Devices and contains multiple electronic systems/modules rather than functioning as a single undifferentiated registration table.

The IVDR explicitly identifies systems for:

* device registration
* UDI database
* economic-operator registration
* notified bodies and certificates
* performance studies
* vigilance/post-market surveillance
* market surveillance.

The Commission currently describes the first four modules as mandatory from 28 May 2026, while the remaining modules are under development.

### Ontology interpretation

* Candidate Class: `reg:EUDAMED`
* Candidate Class: `reg:EUDAMEDModule`
* Candidate Object Property: `hasModule`
* Candidate Object Property: `storesRegistration`
* Candidate Object Property: `makesInformationAvailable`

### Modeling note

EUDAMED should likely be modeled as a **regulatory information system / registry**, not merely as an organization or database table.

---

## Concept: Registration of Devices

### Source

* MDR: Article 29
* IVDR: Article 26

### Regulatory text

MDR requires the manufacturer, before placing a non-custom-made device on the market, to assign the Basic UDI-DI and provide it to the UDI database with the required core data.

IVDR establishes the corresponding device-registration mechanism in Article 26.

### Ontology interpretation

* Candidate Class: `reg:DeviceRegistration`
* Candidate Event: `DeviceRegistrationSubmission`
* Candidate Object Property: `registersDevice`
* Candidate Object Property: `submittedBy`
* Candidate Object Property: `registeredIn`
* Candidate Object Property: `hasRegistrationData`

### Modeling note

`DeviceRegistration` should not automatically be interpreted as equivalent to `MarketAuthorization`.

The regulations establish a registration mechanism and separately establish conformity/CE/market-access requirements.

This distinction is central to later ontology design.

---

## Concept: Registration of Economic Operators

### Source

* MDR: Articles 30–31
* IVDR: Articles 27–28

### Regulatory text

Economic operators subject to registration submit prescribed information to the electronic system. After competent-authority verification, an SRN is issued.

### Ontology interpretation

* Candidate Class: `reg:EconomicOperatorRegistration`
* Candidate Event: `EconomicOperatorRegistrationSubmission`
* Candidate Event: `SRNIssuance`
* Candidate Object Property: `registersEconomicOperator`
* Candidate Object Property: `verifiedBy`
* Candidate Object Property: `issuedBy`
* Candidate Object Property: `hasSRN`

---

## Concept: EU Declaration of Conformity

### Source

* MDR: Article 19
* IVDR: Article 17

### Ontology interpretation

* Candidate Class: `reg:EUDeclarationOfConformity`
* Candidate Object Property: `declaresConformityOf`
* Candidate Object Property: `issuedByManufacturer`
* Candidate Object Property: `referencesBasicUDIDI`

### Modeling note

The declaration is a regulatory document/artifact associated with the manufacturer's conformity claim.

It should not be collapsed with:

* CE marking
* notified-body certificate
* conformity assessment activity

---

## Concept: Certificate

### Source

* MDR: Article 56–57
* IVDR: Article 51–52

### Ontology interpretation

* Candidate Class: `reg:Certificate`
* Candidate Class: `reg:NotifiedBodyCertificate`
* Candidate Object Property: `issuedBy`
* Candidate Object Property: `certifies`
* Candidate Object Property: `hasValidityPeriod`
* Candidate Object Property: `hasCertificateStatus`

### Modeling note

Certificate lifecycle is explicitly relevant to ontology design because the regulations contemplate issuance, amendment, suspension, restriction, withdrawal and invalidity in different regulatory contexts.

---

## Concept: Certificate of Free Sale

### Source

* MDR: Article 60

### Context

MDR Article 60 establishes a certificate of free sale for export purposes. It confirms that the relevant manufacturer or authorised representative has its registered place of business in the Member State and that the CE-marked device may be marketed in the Union.

### Ontology interpretation

* Candidate Class: `mdr:CertificateOfFreeSale`
* Candidate Object Property: `issuedTo`
* Candidate Object Property: `issuedByMemberState`
* Candidate Object Property: `concernsDevice`

### Modeling note

This is distinct from a notified-body conformity certificate.

---

# 3. Relationships

## 3.1 Explicit regulatory relationships

| Subject                   | Relationship                     | Object                              | Source                          |
| ------------------------- | -------------------------------- | ----------------------------------- | ------------------------------- |
| Manufacturer              | manufactures                     | Device                              | MDR Art. 2(30); IVDR Art. 2(23) |
| Manufacturer              | markets under name/trademark     | Device                              | MDR Art. 2(30); IVDR Art. 2(23) |
| Authorised Representative | acts on behalf of                | Manufacturer                        | MDR Art. 2(32); IVDR Art. 2(25) |
| Authorised Representative | acts under                       | Written mandate                     | MDR Art. 11; IVDR Art. 11       |
| Importer                  | places on market                 | Device from third country           | MDR Art. 2(33); IVDR Art. 2(26) |
| Distributor               | makes available                  | Device                              | MDR Art. 2(34); IVDR Art. 2(27) |
| Economic Operator         | submits registration information | Registration system                 | MDR Art. 30–31; IVDR Art. 27–28 |
| Competent Authority       | verifies                         | Economic operator registration data | MDR Art. 31; IVDR Art. 28       |
| Competent Authority       | obtains/issues                   | SRN                                 | MDR Art. 31(2); IVDR Art. 28(2) |
| Manufacturer              | assigns                          | Basic UDI-DI                        | MDR Art. 29; IVDR Art. 26       |
| Manufacturer              | provides information to          | UDI database                        | MDR Art. 29; IVDR Art. 26       |
| Manufacturer              | enters/verifies                  | EUDAMED device information          | MDR Art. 29; IVDR Art. 26       |
| Notified Body             | performs                         | Conformity assessment               | MDR Art. 52; IVDR Art. 48       |
| Notified Body             | issues                           | Certificate                         | MDR Art. 56; IVDR Art. 51       |
| Manufacturer              | affixes                          | CE marking                          | MDR Art. 20; IVDR Art. 18       |
| CE marking                | indicates                        | Conformity                          | MDR Art. 2(43); IVDR Art. 2(35) |

---

## 3.2 Inferred relationships

### Inferred relationship: Device Registration → Market Access

**Supporting sources:**

* MDR Article 29
* MDR Article 5
* IVDR Article 26
* IVDR Article 5

The regulations connect registration requirements temporally with placing a device on the market.

However, registration itself should **not** be treated as equivalent to authorization.

**Modeling question:**

Should:

`DeviceRegistration`

be modeled as a prerequisite activity for:

`PlacingOnMarket`

rather than as:

`MarketAuthorization`?

This requires further legal analysis.

---

### Inferred relationship: Conformity Assessment → CE Marking

The regulations establish conformity assessment requirements and separately establish CE marking.

Therefore a candidate semantic chain is:

`Device`
→ `subjectTo`
→ `ConformityAssessment`

→ `supports`
→ `CE Marking`

But the ontology should not assert a universal one-to-one relationship between every conformity assessment and every CE marking without considering the applicable conformity-assessment route.

---

### Potential ontology relationship: Economic Operator → Role

A shared conceptual structure may be:

`EconomicOperator`
→ `hasRole`
→ `Manufacturer | AuthorisedRepresentative | Importer | Distributor`

However, this is an ontology abstraction and not itself regulatory language.

---

# 4. Regulatory Business Rules

## Rule R01 — Market access requires compliance

### Regulatory text

MDR Article 5 and IVDR Article 5 establish that a device may be placed on the market or put into service only when the applicable regulatory requirements are met.

### Rule interpretation

A `Device` entering market-access events must satisfy applicable regulatory requirements.

### Potential representation

* OWL restriction: `PlacingOnMarket only Device`
* SHACL: market-access event must reference a device with required conformity evidence
* Conditional constraint: applicability depends on device category and regulatory route
* Lifecycle rule: `RegulatoryReady → PlacingOnMarket`

---

## Rule R02 — Basic UDI-DI precedes placing on market

MDR Article 29 and IVDR Article 26 require assignment of the Basic UDI-DI before placing the relevant device on the market.

### Potential representation

* Temporal constraint:
  `BasicUDIDIAssignmentTime < PlacingOnMarketTime`
* SHACL: device registration requires Basic UDI-DI
* Conditional constraint: custom-made devices are treated differently under MDR Article 29

---

## Rule R03 — Certain conformity-assessment routes require Basic UDI-DI before notified-body application

MDR Article 29(3) and IVDR Article 26(2) establish that, for specified conformity-assessment routes, the Basic UDI-DI must be assigned before the manufacturer applies to the notified body.

### Potential representation

* Temporal rule
* Process prerequisite
* SHACL conditional constraint

---

## Rule R04 — Economic operator registration precedes market placement

MDR Article 31 and IVDR Article 28 require manufacturers, authorised representatives and importers to submit registration information before placing a device on the market, subject to the specified conditions.

### Potential representation

```text
EconomicOperator
    mustHave
EconomicOperatorRegistration
    before
PlacingOnMarket
```

This is a candidate temporal rule, not final OWL.

---

## Rule R05 — Registration data must be updated after changes

MDR Article 31(4) and IVDR Article 28(4) require economic operators to update the registration information after changes.

### Potential representation

* Trigger: `RegistrationDataChanged`
* Event: `UpdateEconomicOperatorRegistration`
* Constraint: update required within specified regulatory period
* SHACL: stale registration data detection

---

## Rule R06 — Periodic confirmation of economic-operator data

MDR and IVDR require confirmation of data after one year and every second year thereafter.

### Potential representation

* Temporal constraint
* Recurring compliance event
* SHACL validation against `lastDataConfirmationDate`

---

## Rule R07 — Importer verification

MDR Article 30 and IVDR Article 27 require importers to verify, within two weeks of placing a device on the market, that the manufacturer or authorised representative has provided the required information.

### Potential representation

```text
PlacingOnMarket
    triggers
ImporterRegistrationVerification
```

with:

`verificationDeadline = placingOnMarketDate + 14 days`

---

## Rule R08 — CE marking and EU Declaration of Conformity

Distributor and importer obligations include verification that the device bears CE marking and that the EU declaration of conformity has been drawn up. MDR Article 13 and IVDR Article 14 establish these checks.

### Potential representation

* SHACL:

  * `Device hasCEMarking`
  * `Device hasEUDeclarationOfConformity`
* Conditional based on applicable regulatory route

---

## Rule R09 — Change of intended purpose can transfer manufacturer obligations

IVDR Article 16 establishes that an importer, distributor or other person can assume manufacturer obligations where it changes the intended purpose of a device already placed on the market or put into service.

MDR contains corresponding provisions in Article 16.

### Potential representation

```text
Actor
    changesIntendedPurposeOf
Device
    →
Actor assumes
ManufacturerObligations
```

### Modeling note

This is highly relevant to role-based ontology design because `Manufacturer` is not necessarily a static organization identity.

---

## Rule R10 — Device information must remain updated

MDR Article 29(4) and IVDR Article 26(3) require manufacturers to enter/verify specified information in EUDAMED and subsequently keep it updated.

### Potential representation

* `DeviceRegistration`
* `hasRegistrationData`
* `lastUpdatedAt`
* `updatedBy`

---

# 5. Lifecycle Events and States

## Event E01 — Economic Operator Registration

**Trigger:** economic operator becomes subject to registration requirement

**Actor:** Manufacturer / Authorised Representative / Importer

**Subject:** Economic Operator

**Object:** EUDAMED registration system

**Result:** registration record submitted

**Source:** MDR Art. 31; IVDR Art. 28

**Modeling status:** Legally established regulatory activity

---

## Event E02 — Economic Operator Data Verification

**Actor:** Competent Authority

**Subject:** Economic Operator registration data

**Result:** verified registration data

**Source:** MDR Art. 31(2), (6); IVDR Art. 28(2), (6)

**Modeling status:** Legally established regulatory activity

---

## Event E03 — SRN Issuance

**Actor:** Competent Authority / EUDAMED system interaction

**Subject:** Economic Operator

**Result:** Single Registration Number

**Source:** MDR Art. 31(2); IVDR Art. 28(2)

**Modeling status:** Legally established event

---

## Event E04 — Basic UDI-DI Assignment

**Actor:** Manufacturer

**Subject:** Device

**Result:** Basic UDI-DI

**Source:** MDR Art. 29; IVDR Art. 26

**Modeling status:** Legally established activity

---

## Event E05 — Device Registration

**Actor:** Manufacturer / relevant responsible person

**Subject:** Device / System / Procedure Pack

**Object:** UDI database / EUDAMED

**Result:** device registration data

**Source:** MDR Art. 29; IVDR Art. 26

**Modeling status:** Legally established activity

---

## Event E06 — Conformity Assessment

**Actor:** Manufacturer and, where applicable, Notified Body

**Subject:** Device

**Result:** conformity assessment outcome / certificate where applicable

**Source:** MDR Articles 52–56; IVDR Articles 48–51

**Modeling status:** Legally established process

---

## Event E07 — Certificate Issuance

**Actor:** Notified Body

**Subject:** Device / conformity assessment

**Result:** Certificate

**Source:** MDR Article 56; IVDR Article 51

**Modeling status:** Legally established event

---

## Event E08 — CE Marking

**Actor:** Manufacturer

**Subject:** Device

**Result:** CE marking

**Source:** MDR Article 20; IVDR Article 18

**Modeling status:** Regulatory act / marking activity

---

## Event E09 — Placing on the Market

**Actor:** Economic Operator depending on legal role

**Subject:** Device

**Result:** device becomes first made available on Union market

**Source:** MDR Article 2(28); IVDR Article 2(21)

**Modeling status:** Legally defined market event

---

## Event E10 — Making Available on the Market

**Actor:** Economic Operator / supply-chain actor

**Subject:** Device

**Result:** supply on Union market

**Source:** MDR Article 2(27); IVDR Article 2(20)

**Modeling status:** Legally defined market event

---

## Event E11 — Putting into Service

**Actor:** Supply chain / final user context

**Subject:** Device

**Result:** device available to final user as ready for intended use

**Source:** MDR Article 2(29); IVDR Article 2(22)

**Modeling status:** Legally defined lifecycle event

---

## Event E12 — Registration Data Update

**Trigger:** change in registered information

**Actor:** Economic Operator

**Subject:** Economic Operator registration

**Result:** updated registration record

**Source:** MDR Art. 31(4); IVDR Art. 28(4)

**Modeling status:** Legally established activity

---

## Event E13 — Certificate Suspension / Restriction / Withdrawal

**Actor:** Authority responsible for notified bodies

**Subject:** Notified Body designation / certificates

**Result:** certificate lifecycle state change

**Source:** MDR Article 46; IVDR Article 42 and related provisions.

**Modeling status:** Legally established lifecycle activity

---

# 6. Actors and Roles

## Manufacturer

**Regulatory role**

Primary device-responsible economic operator.

**Key relationships**

* manufactures Device
* defines intended purpose
* assigns UDI
* performs/initiates conformity activities
* draws up EU Declaration of Conformity
* places device on market
* maintains registration information

**Sources**

MDR Articles 2, 10, 27, 29–31
IVDR Articles 2, 10, 24, 26–28

---

## Authorised Representative

**Regulatory role**

EU-established actor representing a manufacturer located outside the Union under a written mandate.

**Key relationships**

* `represents Manufacturer`
* `hasMandate`
* `interactsWithCompetentAuthority`
* `supportsRegistration`

**Sources**

MDR Articles 2(32), 11
IVDR Articles 2(25), 11

---

## Importer

**Regulatory role**

Union-established actor placing a device from a third country on the Union market.

**Key relationships**

* `importsFromThirdCountry`
* `placesOnMarket`
* `verifiesManufacturerInformation`
* `addsRegistrationInformation`

---

## Distributor

**Regulatory role**

Supply-chain actor other than manufacturer/importer making a device available before putting into service.

**Key relationships**

* `makesAvailable`
* `verifiesCE`
* `verifiesEUDeclarationOfConformity`
* `maintainsComplaintRegister`

---

## Competent Authority

**Regulatory role**

National regulatory authority participating in registration verification, market surveillance and corrective measures.

**Key relationships**

* `verifiesRegistrationData`
* `issuesSRN`
* `authorisesCertainMarketAccessDerogations`
* `takesCorrectiveAction`

MDR Article 59 provides an example of a competent authority authorising placing on the market or putting into service in specified exceptional circumstances.

---

## Notified Body

**Regulatory role**

Designated conformity assessment body.

**Key relationships**

* `performsConformityAssessment`
* `issuesCertificate`
* `maintainsCertificate`
* `uploadsRelevantEUDAMEDInformation`

---

## Authority Responsible for Notified Bodies

**Regulatory role**

National authority responsible for assessment, designation, notification and monitoring of notified bodies.

**Source**

MDR Article 35 onward
IVDR Article 31 onward

IVDR explicitly establishes this role and its responsibility for assessment, designation, notification and monitoring.

---

# 7. Identifiers and Registrations

| Identifier / Registration | Identifies                         | Assigned / Issued by                           | Lifecycle                        | Source                      |
| ------------------------- | ---------------------------------- | ---------------------------------------------- | -------------------------------- | --------------------------- |
| SRN                       | Economic Operator                  | Competent Authority via EUDAMED                | registration/update/confirmation | MDR 31; IVDR 28             |
| Basic UDI-DI              | Device / device grouping           | Manufacturer according to issuing-entity rules | assignment/update                | MDR 29; IVDR 26             |
| UDI-DI                    | Device identifier                  | Manufacturer via issuing-entity system         | identifier lifecycle             | MDR 27; IVDR 24             |
| UDI-PI                    | Production information             | Manufacturer                                   | production-level lifecycle       | MDR Annex VI; IVDR Annex VI |
| Certificate identifier    | Certificate                        | Notified Body                                  | issue/amend/suspend/withdraw     | MDR 56–57; IVDR 51–52       |
| EUDAMED registration      | Regulatory record                  | EUDAMED                                        | create/update                    | MDR 29–31; IVDR 26–28       |
| EMDN code                 | Device nomenclature classification | EMDN system                                    | classification/nomenclature      | European Commission         |

The Commission states that EMDN is the nomenclature manufacturers use when registering medical devices in EUDAMED.

---

# 8. Registration Architecture Observations

A major semantic distinction emerging from the sources is that the EU regulatory framework does **not** have one single concept called "registration".

At minimum, the following should be kept distinct:

```text
Economic Operator
        │
        └── Economic Operator Registration
                    │
                    └── SRN

Device
  │
  └── Device / UDI Registration
             │
             ├── Basic UDI-DI
             ├── UDI-DI
             ├── Device data
             └── EMDN classification

Device
  │
  └── Conformity Assessment
             │
             ├── EU Declaration of Conformity
             ├── Notified Body Certificate (where applicable)
             └── CE Marking

Device
  │
  ├── Placing on Market
  ├── Making Available on Market
  └── Putting into Service
```

This distinction is important because a later ontology must avoid collapsing:

* `Registration`
* `Conformity Assessment`
* `Certification`
* `CE Marking`
* `Market Access`
* `Placing on Market`

into one `Authorization` class.

---

# 9. Ambiguous Concepts

## 9.1 Market Authorization

**Status:** Modeling question

The MDR/IVDR establish legal requirements for placing devices on the market but do not appear to define a single generic legal object called "Market Authorization" equivalent to the authorization construct used in some other regulatory jurisdictions.

Relevant concepts include:

* conformity assessment
* CE marking
* EU Declaration of Conformity
* notified-body certificate
* registration
* placing on the market
* competent-authority derogation

**Question for later ontology design:**

Should `MarketAuthorization` be:

1. excluded as a regulatory-native class;
2. modeled as an abstract derived concept;
3. modeled as a cross-jurisdiction abstraction only in a later comparison ontology?

Current recommendation: **do not introduce it as a source-native concept yet.**

---

## 9.2 Registration vs Authorization

Registration in EUDAMED establishes regulatory information records.

It should not automatically be interpreted as authorization to market.

The legislation separately establishes market-access conditions and conformity requirements.

---

## 9.3 Device vs Device Registration

MDCG 2024-11 explicitly clarifies that EUDAMED device registration operates at the device-identifier level rather than creating one EUDAMED record for every physical sales unit.

Therefore:

```text
PhysicalDevice
    ≠
EUDAMEDDeviceRegistrationRecord
```

This is an important ontology distinction.

---

# 10. Overlapping Concepts

## Device / Medical Device / IVD

IVDR explicitly imports the MDR definition of `medical device` and separately defines `in vitro diagnostic medical device`.

Potential ontology hierarchy:

```text
MedicalDevice
    └── InVitroDiagnosticMedicalDevice
```

but this should remain an ontology interpretation rather than being treated as the literal structure of the legislation.

---

## Making Available / Placing on Market / Putting into Service

These are legally distinct concepts:

```text
MakingAvailableOnMarket
    = supply on Union market

PlacingOnMarket
    = first making available

PuttingIntoService
    = first availability to final user ready for intended purpose
```

Sources:

MDR Article 2(27)–(29)
IVDR Article 2(20)–(22)

---

## UDI / Basic UDI-DI / UDI-DI / UDI-PI

These must remain separate identifier concepts.

Potential hierarchy:

```text
DeviceIdentifier
├── BasicUDIDI
├── UDIDI
└── UDIPI
```

However, the exact semantic hierarchy should be validated against Annex VI and MDCG UDI guidance before implementation.

---

# 11. MDR vs IVDR Differences

## Economic Operator

**MDR**

Economic operator includes:

* manufacturer
* authorised representative
* importer
* distributor
* persons referred to in Article 22(1) and 22(3)

**IVDR**

Economic operator includes:

* manufacturer
* authorised representative
* importer
* distributor

**Modeling implication:**

Do not define one jurisdiction-neutral `EconomicOperator` class at the evidence layer without preserving these differences.

---

## Device definition

MDR contains the broad medical-device definition.

IVDR explicitly references the MDR medical-device definition and then defines IVD specifically.

---

## Performance vs Clinical Evaluation

MDR uses:

* clinical evaluation
* clinical investigation
* clinical evidence

IVDR uses:

* performance evaluation
* performance study
* analytical performance
* clinical performance
* scientific validity

These should not be normalized prematurely.

---

## System / Procedure Pack

MDR contains an explicit system/procedure-pack framework in Article 22.

The equivalent IVDR structure is different and should be investigated separately before creating a common abstraction.

---

## Custom-made Device

MDR has an explicit custom-made-device framework.

No assumption should currently be made that the same ontology class and lifecycle applies identically to IVDR.

---

# 12. Jurisdiction-Specific Concepts

The following concepts appear particularly EU-specific or EU-framework-specific:

* EUDAMED
* SRN
* MDCG
* Notified Body designation
* NANDO
* EMDN
* Basic UDI-DI
* EU Declaration of Conformity
* Certificate of Free Sale
* Authority responsible for notified bodies
* European Database on Medical Devices
* EU-level UDI database
* EU market placement terminology

These should initially remain in the EU regulatory namespace rather than being generalized prematurely.

---

# 13. Potential Abstractions

The following may later become reusable ontology abstractions, but should **not yet be treated as regulatory-native concepts**:

```text
reg:RegulatoryActor
reg:Organization
reg:RegulatoryRole
reg:RegulatedProduct
reg:Identifier
reg:Registration
reg:RegulatoryDocument
reg:ConformityAssessment
reg:Certificate
reg:RegulatoryEvent
reg:MarketAccessEvent
reg:RegulatoryStatus
reg:CompetentAuthority
reg:RegulatorySystem
```

Potential abstraction:

```text
EconomicOperator
        │
        └── hasRole
             ├── Manufacturer
             ├── AuthorisedRepresentative
             ├── Importer
             └── Distributor
```

Potential abstraction:

```text
RegulatedProduct
        │
        ├── MedicalDevice
        └── InVitroDiagnosticMedicalDevice
```

These are **ontology hypotheses**, not extracted legal structures.

---

# 14. Potential Regulatory Status Model

The research supports investigating a state model rather than a single `status` field.

Candidate states include:

```text
Unregistered
Registered
ConformityAssessmentInProgress
ConformityAssessmentCompleted
Certified
CEMarked
EligibleForMarketPlacement
PlacedOnMarket
MadeAvailable
PutIntoService
Withdrawn
Recalled
CertificateSuspended
CertificateWithdrawn
RegistrationUpdated
```

However, the regulations do not provide one unified lifecycle-state vocabulary containing all of these terms.

Therefore these should be treated as **candidate lifecycle states/events**, not source-native statuses.

---

# 15. Key Modeling Questions for Later Design

## MQ01

Is `MarketAuthorization` a valid EU regulatory-native class?

**Current status:** unresolved.

---

## MQ02

Should `Registration` be modeled as:

```text
RegistrationEvent
```

or:

```text
RegistrationRecord
```

or both?

The sources support both a regulatory activity and a persistent information record.

---

## MQ03

Should EUDAMED be modeled as:

```text
RegulatoryDatabase
```

with modules as subclasses/components?

Current evidence strongly supports a modular system representation because MDR/IVDR explicitly enumerate separate electronic systems.

---

## MQ04

Should SRN be modeled as:

```text
Identifier
```

with:

```text
identifies → EconomicOperator
```

rather than as a property directly attached to the organization?

Current modeling direction: **yes**.

---

## MQ05

Should Basic UDI-DI identify a physical device, a device family, or another regulatory grouping?

The exact semantics require deeper analysis of Annex VI Part C and MDCG UDI guidance.

---

## MQ06

How should `Certificate` lifecycle be represented?

Potential model:

```text
Certificate
   ├── issued
   ├── amended
   ├── suspended
   ├── restricted
   ├── withdrawn
   └── invalidated
```

The legal provisions demonstrate that certificate lifecycle is not binary.

---

## MQ07

Should CE marking be represented as an object or event?

Potential alternatives:

```text
Device --hasCEMarking--> CEMarking
```

or:

```text
Manufacturer --affixes--> CEMarking
```

Current evidence favors representing the CE marking itself as a regulatory artifact/marking while separately modeling the manufacturer's act of affixing it.

---

## MQ08

Should `PlacingOnMarket` be represented as an event with temporal properties?

Strong candidate because the legal definition explicitly depends on **first** making available.

---

# 16. Research Quality Check

### Source traceability

All major extracted concepts in this artifact have an identified MDR, IVDR, European Commission or MDCG source.

### Regulatory quotation integrity

Direct quotations have been deliberately limited to short legally relevant excerpts. Where a full legal definition is too long to reproduce, the exact Article/definition reference is provided.

### MDR / IVDR separation

MDR and IVDR definitions have not been silently merged.

Differences have been explicitly recorded where identified.

### Regulatory text vs ontology interpretation

The document separates:

```text
Regulatory text
        ↓
Context
        ↓
Ontology interpretation
        ↓
Modeling question
```

### Inferred relationships

Relationships not directly stated as simple subject–predicate–object assertions are explicitly identified as inferred or potential ontology relationships.

### Unsupported concepts

`MarketAuthorization` is intentionally **not** promoted to a source-native regulatory class.

### Company-specific workflow

No company-specific workflow has been introduced.

### Secondary evidence

The primary evidence layer is based on EUR-Lex MDR/IVDR text. European Commission and MDCG sources are used primarily to clarify EUDAMED/UDI implementation.

### Current implementation status

As of the current research date, the European Commission states that the first four EUDAMED modules became mandatory from **28 May 2026**:

* Actor registration
* UDI/device registration
* Notified Bodies and Certificates
* Market Surveillance

The remaining Post-Market Surveillance/Vigilance and Clinical Investigation/Performance Studies modules are described as still under development.

---

# 17. Evidence-to-Ontology Traceability Backbone

The strongest candidate traceability chain emerging from the research is:

```text
EUR-Lex Article / Annex
        │
        ▼
Regulatory Concept
        │
        ▼
Regulatory Relationship
        │
        ▼
Regulatory Rule / Constraint
        │
        ▼
Lifecycle Event
        │
        ▼
Ontology Candidate
        │
        ├── Class
        ├── Object Property
        ├── Data Property
        ├── Event
        └── Constraint
```

For example:

```text
MDR Article 31
    │
    ├── Economic Operator
    ├── Registration
    ├── Competent Authority
    ├── SRN
    ├── Registration Data
    └── Data Update
             │
             ▼
    EconomicOperatorRegistration
             │
             ├── submittedBy → EconomicOperator
             ├── verifiedBy → CompetentAuthority
             ├── resultsIn → SRN
             ├── storedIn → EUDAMED
             └── hasRegistrationData → RegistrationData
```

And:

```text
MDR Article 29
    │
    ├── Device
    ├── Basic UDI-DI
    ├── UDI database
    ├── EUDAMED
    └── Placing on Market
             │
             ▼
       DeviceRegistration
             │
             ├── registers → Device
             ├── hasBasicUDIDI → BasicUDIDI
             ├── storedIn → EUDAMED
             └── precedes → PlacingOnMarket
```

These structures are **candidate ontology representations**, not final ontology design decisions.

---

# 18. Primary Research Conclusions

The registration / market-access domain in MDR/IVDR is better represented as a network of related regulatory objects than as a single registration workflow.

The evidence supports at least the following distinct semantic layers:

```text
ACTOR LAYER
Manufacturer
Authorised Representative
Importer
Distributor
Competent Authority
Notified Body

        ↓

IDENTITY LAYER
SRN
Basic UDI-DI
UDI-DI
UDI-PI
Certificate identifier

        ↓

DEVICE LAYER
Medical Device
IVD
Accessory
System
Procedure Pack
Custom-made Device

        ↓

REGULATORY EVIDENCE LAYER
Technical Documentation
EU Declaration of Conformity
Certificate
CE Marking
Registration Data

        ↓

REGULATORY PROCESS LAYER
Registration
Conformity Assessment
Certification
CE Marking
Data Verification
Data Update

        ↓

MARKET LIFECYCLE LAYER
Placing on Market
Making Available
Putting into Service
Withdrawal
Recall

        ↓

REGULATORY INFORMATION SYSTEM
EUDAMED
├── Actor Registration
├── UDI / Device Registration
├── Notified Bodies / Certificates
├── Market Surveillance
├── Vigilance / PMS
└── Clinical Investigation / Performance Study
```

The most important modeling conclusion for the next phase is:

> **Do not model EU "registration" as a single class.**

At minimum, the evidence indicates distinct concepts for:

1. **Economic Operator Registration**
2. **Device / UDI Registration**
3. **Conformity Assessment**
4. **Certificate**
5. **CE Marking**
6. **Market Placement**
7. **Market Availability**
8. **Putting into Service**

The ontology should preserve these distinctions before attempting any higher-level `MarketAuthorization` abstraction.
