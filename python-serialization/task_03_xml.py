#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Create a root element, e.g., <data>."""

    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
        if isinstance(value, bool):
            child.set('type', 'bool')
        elif isinstance(value, int):
            child.set('type', 'int')
        elif isinstance(value, float):
            child.set('type', 'float')
        else:
            child.set('type', 'str')
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """deserialize_from_xml"""
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    for child in root:
        element_type = child.get('type', 'str')
        text = child.text
        if element_type == 'bool':
            dictionary[child.tag] = text.lower() == 'true'
        elif element_type == 'int':
            dictionary[child.tag] = int(text)
        elif element_type == 'float':
            dictionary[child.tag] = float(text)
        else:
            dictionary[child.tag] = text
    return dictionary
