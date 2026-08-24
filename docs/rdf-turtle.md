# RDF/Turtle quick rules

- Use prefixes for namespaces (e.g., @prefix reg: <https://example.org/.../registration#> .)
- Group triples per subject using ; and . to end blocks
- Use xsd datatypes for literal dates and URIs for document refs
- Keep ontologies modular: separate core classes, shapes, and examples

Example

ex:Device001 a reg:Device ;
  reg:deviceName "Example Analyzer A" ;
  reg:hasIdentifier ex:Device001Identifier .
