# Validation

A collection of changes to generated code required to validate Turtle examples

## Manual edits

Here's a list of edits that got this validating

### Data (turtle)

* add `^^xsd:anyURI` to the `fhir:v` for each `fhir:url` and for each `fhir:system` that isn't in a [ContactPoint](https://build.fhir.org/datatypes.html#ContactPoint) (heuristically implemented with perl -pi) ([commit](commit/243013a7e8461db1545356957b4510a8ca0e40f4))

## Validating

Here are some ways to execute the validation.

### Using ShEx.js webapp

Use the [manifest.yaml](manifest.yaml) in [shex-simple](https://shex.io/webapps/packages/extension-map/doc/shexmap-simple?manifestURL=https://fhircat.github.io/validation/manifest.yaml).

### Using ShEx.js locally

1. pick someplace for ShEx.js and clone it: `git clone git@github.com:shexjs/shex.js --branch main --depth 1`
2. add `shex.js/packages/shex-cli` to PATH
3. validate by `manifest.yaml` or individual command line args:
  - `validate --yaml-manifest manifest.yaml`
  - `validate -x ShExSchemas/R5/Patient.shex -d FHIR_RDF_Examples/R5/patient-example.ttl -m '{FOCUS a fhir:Patient}@<Patient>'`
