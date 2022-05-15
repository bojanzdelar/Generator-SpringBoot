import re
import os
import json
from jinja2 import Template, Environment

def read_input():
    with open("input.json", "r") as input:
        data = json.load(input)
    return data["package"], data["entities"]

def generate_app_module(entities):
    input_path = "templates/frontend/app.module.ts.j2"
    output_path = "output/frontend/app.module.ts"
    render_template(input_path, output_path, None, entities, None)

def generate_routing_module(entities):
    input_path = f"templates/frontend/app-routing.module.ts.j2"
    output_path = f"output/frontend/app-routing.module.ts"
    render_template(input_path, output_path, None, entities, None)

def generate_menu(entities):
    input_path = "templates/frontend/menu.component.html.j2"
    output_path = "output/frontend/components/menu/menu.component.html"
    render_template(input_path, output_path, None, entities, None)

def generate_app(package):
    input_path = "templates/backend/App.java.j2"
    output_path = "output/backend/App.java"
    render_template(input_path, output_path, package, None, None)

def generate_base_class(package, class_type):
    input_path = f"templates/backend/Base{class_type}.java.j2"
    output_path = f"output/backend/{class_type.lower()}/Base{class_type}.java"
    render_template(input_path, output_path, package, None, None)

def generate_backend_specific_class(package, entity, class_type):
    input_path = f"templates/backend/{class_type}.java.j2"
    output_path = f"output/backend/{class_type.lower()}/{entity['camel']}{class_type if class_type != 'Model' else ''}.java"
    render_template(input_path, output_path, package, None, entity)

def generate_frontend_specific_class(entity, folder, class_type):
    sep = "."
    if class_type.startswith('component'):
        folder = f"{folder}/{entity['kebab']}"
        os.makedirs(f"output/frontend/{folder}", exist_ok=True)
    elif class_type.startswith('form.component'):
        folder = f"{folder}/{entity['kebab']}/{entity['kebab']}-form"
        os.makedirs(f"output/frontend/{folder}", exist_ok=True)
        sep = "-"

    input_path = f"templates/frontend/{class_type}.j2"
    output_path = f"output/frontend/{folder}/{entity['kebab']}{f'{sep}{class_type}' if class_type != 'model.ts' else '.ts'}"
    render_template(input_path, output_path, None, None, entity)

def render_template(input_path, output_path, package, entities, entity):
    with open(input_path, 'r') as input, open(output_path, "w") as output:
        template_string = input.read()
        template = Template(template_string)
        template.environment = Environment(trim_blocks = True, lstrip_blocks = True)
        result = template.render(package=package, entities=entities, entity=entity)
        output.writelines(result)

if __name__ == "__main__":
    package, entities = read_input()
    for key, value in entities.items():
        value['camel'] = key
        value['lower_camel'] = key[0].lower() + key[1:]
        value['kebab'] = re.sub(r'(?<!^)(?=[A-Z])', '-', key).lower()

        for attribute in value['attributes']:
            attribute['name_kebab'] = re.sub(r'(?<!^)(?=[A-Z])', '-', attribute['name']).lower()

    generate_app_module(entities)
    generate_routing_module(entities)
    generate_menu(entities)
    generate_app(package)

    generate_base_class(package, "Model")
    generate_base_class(package, "DTO")
    generate_base_class(package, "Mapper")
    generate_base_class(package, "Service")
    generate_base_class(package, "Controller")
    
    for entity in entities.values():
        generate_backend_specific_class(package, entity, "Model")
        generate_backend_specific_class(package, entity, "DTO")
        generate_backend_specific_class(package, entity, "Mapper")
        generate_backend_specific_class(package, entity, "Repository")
        generate_backend_specific_class(package, entity, "Service")
        generate_backend_specific_class(package, entity, "Controller")

        generate_frontend_specific_class(entity, "models", "model.ts")
        generate_frontend_specific_class(entity, "services", "service.ts")
        generate_frontend_specific_class(entity, "services", "service.spec.ts")

        generate_frontend_specific_class(entity, "components", "component.ts")
        generate_frontend_specific_class(entity, "components", "component.spec.ts")
        generate_frontend_specific_class(entity, "components", "component.html")    
        generate_frontend_specific_class(entity, "components", "component.css")

        generate_frontend_specific_class(entity, "components", "form.component.ts")
        generate_frontend_specific_class(entity, "components", "form.component.spec.ts")
        generate_frontend_specific_class(entity, "components", "form.component.html")    
        generate_frontend_specific_class(entity, "components", "form.component.css")      
