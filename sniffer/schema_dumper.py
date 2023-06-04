import os, json


class JSONSchemaDumper:
    def __init__(self, schema, output_dir):
        self.schema = schema
        self.output_dir = output_dir

    def dump_schema(self, file_name):
        schema_file = os.path.join(self.output_dir, file_name)
        with open(schema_file, 'w') as file:
            json.dump(self.schema, file, indent=4)

        print(f"Schema dumped to: {schema_file}")
