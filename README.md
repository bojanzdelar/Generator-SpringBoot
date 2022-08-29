# Generator - Spring Boot

## Usage:

- Rename example-input.json to input.json
- Run script with `bash start.sh` or `./start.sh`
- Generated code will be available in output folder
- Mapper methods have to be defined manually to prevent infinite recursion
- Rename API paths to be in plural form of nouns

### Dependencies:

- Spring MVC
- Spring Data JPA
- Lombok
- MapStruct
- Shared library with base classes