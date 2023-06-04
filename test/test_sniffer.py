import unittest
import os
import json
from sniffer.schema_sniffer import JSONSchemaSniffer


class JSONSchemaSnifferTestCase(unittest.TestCase):
    def setUp(self):
        self.data_dir = "./data"
        self.file_name = "sample.json"
        self.file_path = os.path.join(self.data_dir, self.file_name)
        self.data = {
            "attributes": {
                "appName": "ABCDEFG",
                "eventType": "ABCDEFGHIJ",
                "subEventType": "ABCDEFGHIJKLMNOPQRSTU",
                "sensitive": True
            },
            "message": {
                "key_one": [
                    {"name": "ABC", "value": 123},
                    {"name": "DEF", "value": 456}
                ],
                "key_two": ["ABC", "DEF", "GHI"],
                "key_three": "XYZ",
                "key_four": 234
            }
        }

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_sniff_schema_padding(self):
        schema_sniffer = JSONSchemaSniffer(self.data)
        schema = schema_sniffer.sniff_schema()

        for attribute in schema.values():
            self.assertIn("tag", attribute)
            self.assertIn("description", attribute)

    def test_sniff_schema_only_message_attributes(self):
        schema_sniffer = JSONSchemaSniffer(self.data)
        schema = schema_sniffer.sniff_schema()

        self.assertNotIn("attributes", schema)
        self.assertIn("key_one", schema)
        self.assertIn("key_two", schema)
        self.assertIn("key_three", schema)

    def test_sniff_schema_required_properties(self):
        schema_sniffer = JSONSchemaSniffer(self.data)
        schema = schema_sniffer.sniff_schema()

        for attribute in schema.values():
            self.assertFalse(attribute["required"])

    def test_sniff_schema_data_type(self):
        schema_sniffer = JSONSchemaSniffer(self.data)
        schema = schema_sniffer.sniff_schema()

        self.assertEqual(schema["key_three"]["type"], "string")
        self.assertEqual(schema["key_one"]["type"], "array")
        self.assertEqual(schema["key_two"]["type"], "enum")
        self.assertEqual(schema["key_four"]["type"], "integer")




if __name__ == "__main__":
    unittest.main()
