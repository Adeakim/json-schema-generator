import unittest
import os
import json


from sniffer.schema_processor import JSONSchemaProcessor

class JSONSchemaProcessorTests(unittest.TestCase):
    def setUp(self):
        self.data_dir = './data'
        self.schema_dir = './schema'
        self.processor = JSONSchemaProcessor(self.data_dir, self.schema_dir)
        self.data_file = 'data.json'

        self.data = {
            "attributes": {
                "appName": "MyApp",
                "eventType": "Event",
                "subEventType": "SubEvent",
                "sensitive": True
            },
            "message": {
                "key_one": [1, 2, 3, "ss"],
                "key_two": ["a", "b", "c"],
                "key_three": "Hello World",
                "key_four": [{
                    "key_one": "value_one",
                    "key_two": "value_two"
                }]
            }
        }

        with open(os.path.join(self.data_dir, self.data_file), 'w') as f:
            json.dump(self.data, f)
           

    def tearDown(self):

        os.remove(os.path.join(self.data_dir, self.data_file))
        os.remove(os.path.join(self.schema_dir, self.data_file))

    def test_process_files(self):
        self.processor.process_files()
        schema_file = os.path.join(self.schema_dir, self.data_file)
        self.assertTrue(os.path.exists(schema_file))

    def test_process_files_schema_attributes(self):
        self.processor.process_files()

        schema_file = os.path.join(self.schema_dir, self.data_file)
        self.assertTrue(os.path.exists(schema_file))

        with open(schema_file, 'r') as f:
            schema = json.load(f)

        self.assertNotIn("attributes", schema)
        self.assertIn("key_one", schema)
        self.assertIn("key_two", schema)
        self.assertIn("key_three", schema)
        self.assertIn("tag", schema["key_one"])
        self.assertIn("description", schema["key_one"])

    def test_process_files_schema_data_types(self):
        self.processor.process_files()

        schema_file = os.path.join(self.schema_dir, self.data_file)
        self.assertTrue(os.path.exists(schema_file))

        with open(schema_file, 'r') as f:
            schema = json.load(f)

        self.assertEqual(schema["key_one"]["type"], "enum")
        self.assertEqual(schema["key_two"]["type"], "enum")
        self.assertEqual(schema["key_three"]["type"], "string")
        self.assertEqual(schema["key_four"]["type"], "array")


if __name__ == '__main__':
    unittest.main()
