import requests
from jsonschema import validate, ValidationError
import json
import xmlschema

class TestJsonSchemaValiation:
    def test_json_schema_validation(self):
        url = "http://mocktarget.apigee.net/json"
        res =  requests.get(url)
        assert res.status_code == 200 , "Wrong status"

        data =  res.json()
        print(data)

        with open("./jsonschema.json") as f:
            schema = json.load(f)
        try:
            validate(instance=data, schema=schema)
            print("JSON data is valid against the schema.")
        except ValidationError as e:
            print("JSON data is not valid against the schema. error is : " ,e)
            assert False

    
    def test_xml_schema_validation(self):
        url = "http://mocktarget.apigee.net/xml"
        res  = requests.get(url)
        assert res.status_code == 200 , "Wrong status"

        #load xml schema
        schema = xmlschema.XMLSchema("./xmlschema.xsd")
        try:
            schema.validate(res.text)
            print("xml schema validation got passed")
        except:
            print("xml schema validation failed")
            assert False

        
