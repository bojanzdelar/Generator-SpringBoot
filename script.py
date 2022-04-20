import re
from jinja2 import Template

def read_input():
    package = input("Enter name of package containing code: ")
    number_of_entities = int(input("Enter number of entities: "))
    entities = []
    attributes = []
    for i in range(number_of_entities):
        print("--------------------------")
        entity = input(f"Enter name of entity number {i}: ")
        entities.append(entity)

        # number_of_entities = int(input("Enter number of attributes: "))
        # entity_attributes = []
        # for i in range(number_of_entities):
        #     attribute = {}
        #     attribute["name"] = input(f"Enter name of attribute number {i + 1}: ")
        #     attribute["type"] = input(f"Enter type of attribute number {i + 1}: ")
        #     entity_attributes.append(attribute)

        # atributi.append(entity_attributes)

    return package, entities, attributes

def generate_base_class(package, class_type):
    input_path = f"templates/Base{class_type}.j2"
    output_path = f"output/{class_type.lower()}/Base{class_type}.java"

    with open(input_path, 'r') as input, open(output_path, "w") as output:
        template_string = input.read()
        template = Template(template_string)
        result = template.render(package=package)
        output.writelines(result)

def generate_specific_class(package, entity, class_type):
    input_path = f"templates/{class_type}.j2"
    output_path = f"output/{class_type.lower()}/{entity}{class_type if class_type != 'Model' else ''}.java"

    with open(input_path, 'r') as input, open(output_path, "w") as output:
        template_string = input.read()
        template = Template(template_string)
        path = re.sub(r'(?<!^)(?=[A-Z])', '-', entity).lower()
        result = template.render(package=package, entity=entity, path=path)
        output.writelines(result)

if __name__ == "__main__":
    # TODO: implement reading data from file
    package, entities, attributes = read_input()

    generate_base_class(package, "Model")
    generate_base_class(package, "DTO")
    generate_base_class(package, "Mapper")
    generate_base_class(package, "Service")
    generate_base_class(package, "Controller")
    
    for i in range(len(entities)):
        generate_specific_class(package, entities[i], "Model")
        generate_specific_class(package, entities[i], "DTO")
        generate_specific_class(package, entities[i], "Mapper")
        generate_specific_class(package, entities[i], "Repository")
        generate_specific_class(package, entities[i], "Service")
        generate_specific_class(package, entities[i], "Controller")