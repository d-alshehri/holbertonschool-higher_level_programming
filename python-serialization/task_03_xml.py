#!/usr/bin/env python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Destination XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)  # Ensure all values are strings

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes an XML file to a Python dictionary.

    Args:
        filename (str): XML filename to read.

    Returns:
        dict: Deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}

        for element in root:
            data[element.tag] = element.text

        return data
    except Exception:
        return None
