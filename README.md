
# JSON Schema Generator

The JSON Schema Generator is a Python program that reads a JSON file, sniffs its schema, and generates a corresponding JSON schema. The generated schema captures the attributes within the "message" key of the input JSON source data, excluding attributes within the "attributes" key. The program sets all properties in the JSON schema as "required": false.


## Installation

1. Clone the repository: `git clone https://github.com/Adeakim/json-schema-generator.git`
2. Navigate to the project directory: `cd json-schema-generator`

## Usage

1. Run the program: `python main.py`
2. The generated JSON schemas will be saved in the `schema` directory.

## Testing
1. Run the unit tests: `python -m unittest discover`


