import os, json
from sniffer.schema_sniffer import JSONSchemaSniffer
from sniffer.schema_dumper import JSONSchemaDumper

class JSONSchemaProcessor:
    def __init__(self, data_dir, schema_dir):
        self.data_dir = data_dir
        self.schema_dir = schema_dir

    def process_files(self):
        if not os.path.exists(self.schema_dir):
            os.makedirs(self.schema_dir)

        for file_name in os.listdir(self.data_dir):
            if file_name.endswith('.json'):
                file_path = os.path.join(self.data_dir, file_name)
                try:
                    with open(file_path, 'r') as file:
                        data = json.load(file)
                except (IOError, json.JSONDecodeError) as e:
                    print(f"Error loading JSON file: {file_path}")
                    continue

                schema_sniffer = JSONSchemaSniffer(data)
                schema = schema_sniffer.sniff_schema()
                schema_dumper = JSONSchemaDumper(schema, self.schema_dir)
                schema_dumper.dump_schema(file_name)
                print(f'Schema extracted and dumped for {file_name}')

        print("Processing complete.")
