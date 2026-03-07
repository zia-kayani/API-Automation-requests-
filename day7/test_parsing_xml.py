import requests
import json
import xmltodict
from xml.dom.minidom import parseString

class TestXMLParsing:
    #Basic xml elements validation
    def test_xml_response_1(slef):
        """
        Validates:
        - HTTP Status code
        - Content Type
        - Specific XML elements
        """
        url = "http://mocktarget.apigee.net/xml"
        res = requests.get(url)

        assert res.status_code == 200 , "Wrong status"
        assert res.headers["Content-Type"] == "application/xml; charset=utf-8", "wrong header"

        print(parseString(res.text).toprettyxml())
        #converting xml to json for easier access to elements and asserting values
        xml_to_json_data = xmltodict.parse(res.text)

        print(json.dumps(xml_to_json_data, indent=4))

        root = xml_to_json_data["root"]
        assert root["city"] == "San Jose", "Wrong city"
        assert root["firstName"] == "John", "Wrong first name"
        assert root["lastName"] == "Doe", "Wrong last name"
        assert root["state"] == "CA", "Wrong state"
    
    def test_xml_response_2(slef):
        """
        Validates:
        - HTTP Status code
        - Content Type
        - Specific XML elements
        """
        url = "http://httpbin.org/xml"
        res = requests.get(url)

        assert res.status_code == 200 , "Wrong status"
        assert res.headers["Content-Type"] == "application/xml", "wrong header"

        print(parseString(res.text).toprettyxml())

        xml_to_json_data = xmltodict.parse(res.text)
        print(json.dumps(xml_to_json_data, indent=4))

        slideshow =  xml_to_json_data["slideshow"]
        assert slideshow["@title"] == "Sample Slide Show", "Wrong title"
        assert slideshow["@date"] == "Date of publication", "Wrong date"
        assert slideshow["@author"] == "Yours Truly", "Wrong author"

    #Parse and valide more content from above api
    def test_xml_response_2(slef):
            """
            Validates:
            - HTTP Status code
            - Content Type
            - Specific XML elements
            """
            url = "http://httpbin.org/xml"
            res = requests.get(url)

            assert res.status_code == 200 , "Wrong status"
            assert res.headers["Content-Type"] == "application/xml", "wrong header"

            print(parseString(res.text).toprettyxml())

            xml_to_json_data = xmltodict.parse(res.text)
            print(json.dumps(xml_to_json_data, indent=4))

            slides =  xml_to_json_data["slideshow"]["slide"]
            #validations ------------------------
            assert len(slides) == 2, "Wrong number of slides"
            titles  = [slide["title"] for slide in slides]
            print(titles)
            assert len(titles) == 2, "Wrong number of titles"
            assert titles[0] == "Wake up to WonderWidgets!", "Wrong title for slide 1"
            assert titles[1] == "Overview", "Wrong title for slide 2"

            # validate items
            items = []

            for slide in slides:
                item = slide.get("item", [])
                if isinstance(item, str):
                    items.append(item)
                else:
                    items.extend(item)

            print(items)

            assert len(items) == 3, "There shoud be 3 items"
            assert items[0]['em'] == "WonderWidgets"
            assert items[2]['em'] == "buys"



       