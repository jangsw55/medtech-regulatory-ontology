# medtech-regulatory-ontology

> Building an open, reusable ontology for the Medical Device Regulatory domain.

---

## Current Status

🚧 **This project is currently under active development.**

This repository is not a finished ontology, but a **research-driven engineering notebook**.

The goal is **not** to build the entire ontology at once, but to develop it incrementally through well-documented domain modeling.

Each domain follows the same workflow:

```
Research
    ↓
Concept Analysis
    ↓
Ontology Design
    ↓
OWL Modeling
    ↓
SHACL Validation
    ↓
Example Dataset
    ↓
Design Review
```

The **Registration** domain is the first module being developed end-to-end.

Once the modeling approach has stabilized, the same methodology will be applied to additional domains.

The roadmap below represents the **long-term vision**, not the current implementation status.

---

## Why this project exists

Regulatory Affairs has traditionally been document-centric.

Most regulatory systems are built around Word documents, templates, spreadsheets, and disconnected databases. As organizations adopt AI, many attempt to automate these documents directly using Large Language Models.

However, through my experience designing enterprise regulatory automation initiatives, I realized that AI alone is not enough.

Before AI can reason, organizations need a shared understanding of their domain.

Products.

Registrations.

Countries.

Legal Manufacturers.

UDI.

Complaints.

CAPA.

Risk.

Documents.

These are not documents—they are **knowledge**.

This project explores how regulatory knowledge can be represented explicitly using ontologies and knowledge graphs instead of remaining hidden inside documents and human expertise.

---

## Vision

The long-term goal is to build an open semantic model for the Medical Device Regulatory domain that can serve as a foundation for:

* Knowledge Graphs
* Enterprise AI
* Agentic AI workflows
* Regulatory Information Management Systems (RIMS)
* Process Automation
* Decision Support Systems

Instead of modeling how one company works, this project focuses on modeling concepts that are common across the medical device industry using publicly available standards.

---

## Scope

The ontology is built entirely from publicly available sources, including:

* FDA regulations and guidance
* EU MDR / IVDR
* ISO 13485
* ISO 14971
* IMDRF guidance
* UDI standards
* Public regulatory terminology and reference data

No company-specific data, confidential workflows, or proprietary information are included.

---

## Project Philosophy

This project follows a simple principle:

> **Model knowledge first. Automate processes second.**

Business processes change.

Software changes.

AI models change.

Domain knowledge changes much more slowly.

By explicitly modeling regulatory concepts and their relationships, AI systems become more explainable, reusable, and maintainable.

---

## Research Approach

Each domain follows a consistent methodology:

```
Research
    ↓
Concept Analysis
    ↓
Ontology Design
    ↓
OWL Modeling
    ↓
SHACL Validation
    ↓
Example Dataset
    ↓
Design Review
```

Every module documents not only the ontology itself, but also the reasoning behind design decisions.

---

## Repository Structure

```
research/
    Public standards analysis
    Domain comparison
    Ontology design notes

ontology/
    OWL ontologies
    Object properties
    Restrictions
    SHACL validation

examples/
    Example datasets

docs/
    Architecture
    Design decisions # project level decisions. Domain decisions are in research/<domain>/design_decisions.md
    Modeling guidelines

scripts/
    RDFLib
    Neo4j
    SPARQL
```

---

## Roadmap

### Phase 1 – Core Ontology (In Progress)

* [x] Registration (in research phase)

  * [ ] Market
  * [ ] Country
  * [ ] Regulatory Authority
  * [ ] Market Authorization
  * [ ] Submission

* [ ] Product
* [ ] Organization & Economic Operators

---

### Phase 2 – Regulatory Knowledge

* [ ] Device Identification (UDI)
* [ ] Labeling
* [ ] Risk Management
* [ ] Complaint & Vigilance
* [ ] Post-Market Surveillance
* [ ] Clinical Evaluation
* [ ] Document Ontology
* [ ] Reference Data

---

### Phase 3 – Enterprise AI Layer (Future)

* [ ] Neo4j Knowledge Graph Integration
* [ ] SHACL-based validation automation
* [ ] SPARQL query layer
* [ ] GraphRAG / Retrieval layer
* [ ] Agent-based reasoning workflows

---

## Technology Stack

### Currently Used

* Protégé
* OWL
* RDF / Turtle
* SKOS
* SHACL
* Python
* GitHub

### Planned

* Neo4j
* RDFLib
* NetworkX
* SPARQL
* LangGraph
* GraphRAG

---

## Learning Goals

This repository is both a research project and a personal learning journey.

Its objectives are to:

* Bridge **Regulatory Affairs domain expertise** with **formal knowledge representation**
* Learn ontology engineering through real-world medical device regulatory modeling
* Develop reusable semantic models rather than company-specific workflows
* Explore OWL, SHACL, semantic reasoning, and Knowledge Graph technologies through practical implementation
* Build explainable AI systems grounded in explicit domain knowledge instead of document-centric automation

---

## Long-term Goal

This project is intended to evolve beyond an ontology repository.

The long-term vision is an **Agentic Knowledge Platform** where AI agents can navigate regulatory knowledge rather than simply search documents.

Example workflow:

```
Complaint Received
        ↓
Identify Product
        ↓
Identify Market
        ↓
Determine Applicable Regulations
        ↓
Reason over Knowledge Graph
        ↓
Identify Required Documents
        ↓
Generate Regulatory Checklist
```

Rather than asking AI to memorize regulations, the goal is to provide AI with an explicit semantic representation of the regulatory domain.

---

## Core Design Principle

> **Every module in this repository follows the same principle: research first, model second, implement third.**

Nothing is added unless it can be traced back to publicly available standards or documented design decisions.

---

## Disclaimer

This project is an independent educational and research initiative.

It is built exclusively from publicly available information and does not contain confidential company information, proprietary workflows, or customer data.

The ontology design decisions are my own and do not represent any employer or organization.
