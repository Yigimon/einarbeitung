from lxml import etree

# Lade das XML und das XSD
xml_file = "Hero.xml"
xsd_file = "schema.xsd"

# Lade das XSD-Schema
with open(xsd_file, "r") as schema_file:
    schema_root = etree.XML(schema_file.read())
    xmlschema = etree.XMLSchema(schema_root)

# Lade das XML
with open(xml_file, "r") as xml_file:
    xml_root = etree.XML(xml_file.read())

# Validierung des XMLs gegen das XSD
is_valid = xmlschema.validate(xml_root)

if is_valid:
    print("Das XML ist gültig.")
else:
    print("Das XML ist ungültig.")
    # Ausgabe von Validierungsfehlern
    for error in xmlschema.error_log:
        print(error.message)
