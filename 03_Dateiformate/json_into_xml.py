import json
from dicttoxml import dicttoxml


with open("base.json", "r") as file:
    source_data = json.load(file)

xml_data = dicttoxml(source_data, custom_root = "root", attr_type = False)


with open("/root/einarbeitung/03_Dateiformate/data.xml", "wb") as xml_file:
    xml_file.write(xml_data)
