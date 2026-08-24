# Validation (SHACL)

Purpose: describe how to validate instance data against shapes.

Why validation
- Ensure required properties exist (e.g., registrationNumber for RegistrationRecord)
- Ensure correct datatypes (xsd:date, xsd:anyURI)
- Catch missing human-readable labels if queries expect them

How to run
- Use pyshacl or TopBraid SHACL tools
- Example: `pyshacl -s ontology/registration/registration-shapes.ttl -d ontology/registration/example_registration.ttl -v`

Design notes
- Start with permissive shapes, then tighten as evidence accumulates.
- Prefer clear error messages and link to example fixes in docs.
