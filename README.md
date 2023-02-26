# Validation

A collection of changes to generated code required to validate Turtle examples

## Validate

### Using ShEx.js webapp

Use the [manifest.yaml](manifest.yaml):
https://shex.io/webapps/packages/extension-map/doc/shexmap-simple?manifestURL=https://fhircat.github.io/validation/manifest.yaml

### Using ShEx.js locally

1. pick someplace for ShEx.js and clone it: `git clone git@github.com:shexjs/shex.js --branch main --depth 1`
2. add `shex.js/packages/shex-cli` to PATH
3. validate by `manifest.yaml` or individual command line args:
  - `validate --yaml-manifest manifest.yaml`
  - `validate -x ShExSchemas/Patient.shex -d examples/patient-example.ttl -m '{FOCUS a fhir:Patient}@<Patient>'`
