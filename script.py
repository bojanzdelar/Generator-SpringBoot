import re
import json
from jinja2 import Template

def read_input():
    with open("input.json", "r") as input:
        data = json.load(input)
    return data["package"], data["entities"], [] # TODO: add attributes

def generate_base_class(package, class_type):
    input_path = f"templates/backend/Base{class_type}.java.j2"
    output_path = f"output/backend/{class_type.lower()}/Base{class_type}.java"

    with open(input_path, 'r') as input, open(output_path, "w") as output:
        template_string = input.read()
        template = Template(template_string)
        result = template.render(package=package)
        output.writelines(result)

# TODO: merge this two functions

def generate_backend_specific_class(package, entity, class_type):
    input_path = f"templates/backend/{class_type}.java.j2"
    output_path = f"output/backend/{class_type.lower()}/{entity}{class_type if class_type != 'Model' else ''}.java"

    with open(input_path, 'r') as input, open(output_path, "w") as output:
        template_string = input.read()
        template = Template(template_string)
        path = re.sub(r'(?<!^)(?=[A-Z])', '-', entity).lower()
        result = template.render(package=package, entity=entity, path=path)
        output.writelines(result)

def generate_frontend_specific_class(package, entity, folder, class_type):
    path = re.sub(r'(?<!^)(?=[A-Z])', '-', entity).lower()
    input_path = f"templates/frontend/{class_type}.ts.j2"
    output_path = f"output/frontend/{folder}/{path}{f'.{class_type}' if class_type != 'model' else ''}.ts"

    with open(input_path, 'r') as input, open(output_path, "w") as output:
        template_string = input.read()
        template = Template(template_string)
        result = template.render(package=package, entity=entity, path=path)
        output.writelines(result)

if __name__ == "__main__":
    package, entities, attributes = read_input()

    generate_base_class(package, "Model")
    generate_base_class(package, "DTO")
    generate_base_class(package, "Mapper")
    generate_base_class(package, "Service")
    generate_base_class(package, "Controller")
    
    for i in range(len(entities)):
        generate_backend_specific_class(package, entities[i], "Model")
        generate_backend_specific_class(package, entities[i], "DTO")
        generate_backend_specific_class(package, entities[i], "Mapper")
        generate_backend_specific_class(package, entities[i], "Repository")
        generate_backend_specific_class(package, entities[i], "Service")
        generate_backend_specific_class(package, entities[i], "Controller")

        generate_frontend_specific_class(package, entities[i], "models", "model")
        generate_frontend_specific_class(package, entities[i], "services", "service")
        generate_frontend_specific_class(package, entities[i], "services", "service.spec")