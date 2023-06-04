from sniffer.schema_processor import JSONSchemaProcessor

def main():
    data_dir = './data'
    schema_dir = './schema'
    processor = JSONSchemaProcessor(data_dir, schema_dir)
    processor.process_files()


if __name__ == '__main__':
    main()
