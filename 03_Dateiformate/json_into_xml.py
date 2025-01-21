import json
import xmltodict

# Read JSON file
with open("Hero.json", "r") as file:
    python_data = json.load(file)

# Wrap the JSON list under a root element # das hat ChatGpt hinzugefügt, da es ansonsten nicht funktioniert hat und es immer einen Fehlercode angezeigt hatte
root_element = {"root": {"squads": python_data}}

# Convert to XML and save to file
with open("Hero.xml", "w") as xml_file:
    xml_content = xmltodict.unparse(root_element, pretty=True)
    xml_file.write(xml_content)

print("XML file saved successfully.")
