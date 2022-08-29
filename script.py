import re
import json
from jinja2 import Template, Environment

def read_input():
    with open("input.json", "r") as input:
        data = json.load(input)
    return data["package"], data["entities"]

def generate_class(package, entity, class_type):
    input_path = f"templates/{class_type}.java.j2"
    output_path = f"output/{class_type.lower()}/{entity['camel']}{class_type if class_type != 'Model' else ''}.java"
    render_template(input_path, output_path, package, None, entity)

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
        value['kebab'] = re.sub(r'(?<!^)(?=[A-Z])', '-', key).lower()
 
    for entity in entities.values():
        generate_class(package, entity, "Model")
        generate_class(package, entity, "DTO")
        generate_class(package, entity, "Mapper")
        generate_class(package, entity, "Repository")
        generate_class(package, entity, "Service")
        generate_class(package, entity, "Controller")