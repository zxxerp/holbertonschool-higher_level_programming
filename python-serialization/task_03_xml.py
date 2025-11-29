#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): The data to save.
        filename (str): The destination file path.
    """
    # Create the Root Element
    # In XML, everything must be wrapped in a single parent tag.
    # We call it "data" here.
    root = ET.Element("data")

    # Iterate through the dictionary items
    for key, value in dictionary.items():
        # Create a child element for each key (e.g., <name>)
        child = ET.SubElement(root, key)

        # Set the content of the tag.
        # XML requires values to be strings, so we cast str(value).
        child.text = str(value)

    # Create the ElementTree object wrapping our root
    tree = ET.ElementTree(root)

    # Write the tree to the file
    tree.write(filename, encoding="utf-8", xml_declaration=False)
    # xml_declaration=False is optional, but often cleaner for simple files.


def deserialize_from_xml(filename):
    """
    Deserializes an XML file back into a dictionary.

    Args:
        filename (str): The file path to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        # Parse the XML file
        # This reads the file and builds the tree in memory.
        tree = ET.parse(filename)

        # Get the root element (<data>) so we can loop through its children
        root = tree.getroot()

        result_dict = {}

        # Iterate through every child element inside <data>
        for child in root:
            # child.tag is the key (e.g., "name")
            # child.text is the value (e.g., "John")
            result_dict[child.tag] = child.text

        return result_dict

    except FileNotFoundError:
        return None
    except ET.ParseError:
        return None
