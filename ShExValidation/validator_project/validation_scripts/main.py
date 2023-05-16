import os
import re
from pathlib import Path
from os import listdir


def list_files_with_content(directory):
    for child in Path(directory).iterdir():
        if child.is_file():
            print(f"{child.name}:\n{child.read_text()}\n")


def get_shex_schema_from_examples(examples, shex, output):
    matching_resource_examples = []
    unique_yamls = []
    ext = '.ttl'

    output_loc = os.path.abspath(output)
    if not (os.path.exists(output_loc)):
        os.makedirs(output_loc)

    listd = listdir(output_loc)
    for fileName in listd:
        try:
            os.remove(output_loc+fileName)
        except OSError:
            pass

    readme = os.path.join(output_loc, 'README.md')
    with open(readme, 'a+') as rm:
        rm.write('# FHIR RDF Data Validation Mainfests\n\n| Example | Description |\n| ------- | ----------- |')

    shex_validator='https://shex.io/webapps/packages/extension-map/doc/shexmap-simple?manifestURL=https://fhircat.github.io/validation/2023JBISubmissionSupport/fhir_rdf_examples_validation/'
    for root, dirs, files in os.walk(os.path.join(output_loc,examples)):
        for x in files:
            if ext in x:
                print(f'Processing File: {x}')
                with open(os.path.join(root, x), "r") as f:
                    print(x)
                    contents = f.read()
                    m = re.search('a fhir:(.+?);', contents)
                    if m:
                        matching_name = m.group(1)
                        matching_resource_examples.append(x + ':' + matching_name)
                        shex_name = matching_name.strip()
                        shex_loc = shex_name + '.shex'
                        example_loc = x.split(".")[0]
                        filepath = os.path.join(output_loc, shex_name + '.yaml')
                        with open(filepath, 'a+') as outf:
                            outf.write(f'\n- schemaLabel: {shex_name}\n  schemaURL: {shex}{shex_loc}\n  dataLabel: {example_loc}\n  dataURL: {examples}{x}\n  queryMap: "{{FOCUS a fhir:{shex_name}}}@<{shex_name}>"\n  status: conformant\n');

                        if not (shex_name in unique_yamls):
                            with open(readme, 'a+') as rma:
                                rma.write(f'\n| {shex_name} | [{example_loc}]({shex_validator}{shex_name}.yaml) |')
                            unique_yamls.append(shex_name)
                    else:
                        print(f'Could not map for File: {x}')
        file_count = len(files)
        print(f'Total files: {file_count}')
    return matching_resource_examples


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    example_dir = 'FHIR_RDF_Examples/R5/'
    shex_dir = 'ShExSchemas/R5Plus/'
    output_dir = '../../../2023JBISubmissionSupport/fhir_rdf_examples_validation'
    resource_examples = get_shex_schema_from_examples(example_dir, shex_dir, output_dir)

    print(f"Resource Examples: {len(resource_examples)}")
