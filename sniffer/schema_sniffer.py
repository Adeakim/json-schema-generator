import json
import os

class JSONSchemaSniffer:
    def __init__(self, data):
        self.data = data

    def sniff_schema(self):
        message_data = self.data.get('message', {})
        schema = self._generate_schema_model(message_data)
        return schema

    def _generate_schema_model(self, data):
        properties = {}
        for key, value in data.items():
            if isinstance(value, dict):
                nested_model = self._generate_schema_model(value)
                properties[key] = nested_model
            else:
                field_type = self._infer_data_type(value)
                properties[key] = {
                    'type': field_type,
                    'tag': '',
                    'description': '',
                    'required': False
                }
        return properties

    def _infer_data_type(self, value):
        if isinstance(value, str):
            return 'string'
        elif isinstance(value, int):
            return 'integer'
        elif isinstance(value, list):
            return self._infer_array_type(value)
        else:
            return 'unknown'

    def _infer_array_type(self, array):
        if all(isinstance(item, (str, int))  for item in array):
            return 'enum'
        elif all(isinstance(item, dict) for item in array):
            return 'array'
        else:
            return 'unknown'
