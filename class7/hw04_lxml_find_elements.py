#!/usr/bin/env python
"""
4a. Use the find() method to retrieve the first "zones-security" element.
Print out the tag of this element and of all its children elements.
Your output should be similar to the following:

Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces
"""
from xml.etree.ElementTree import ElementTree
from lxml import etree

def parse_xml_file(filename: str) -> ElementTree:
    with open(filename, "r") as f:
        xml = etree.parse(f)
    return xml

xml_filename = "show_security_zones.xml"
my_xml = parse_xml_file(xml_filename)

print(etree.tostring(my_xml).decode())

child1 = my_xml.find("zones-security")

print("Find tag of the first zones-security element")
print("-" * 80)
print(child1.tag)

print("\n")
print("Find tag of all child elements of the first zones-security element")
print("-" * 80)
for child in child1:
    print(child.tag)

"""
4b. Use the find() method to find the first "zones-security-zonename". 
Print out the zone name for that element (the "text" of that element).
"""
print("\n")
print('Finding the first "zones-security-zonename"')
print("-" * 80)
zonename = my_xml.find("zones-security").find("zones-security-zonename")
print(zonename.text)
"""
4c. Use the findall() method to find all occurrences of "zones-security".
 For each of these security zones, print out the security zone name ("zones-security-zonename", the text of that element).

"""
print("\n")
print('Finding all "zones-security-zonename"')
print("-" * 80)
zones_security = my_xml.findall("zones-security")
for children in zones_security:
    zonename = children.find("zones-security-zonename")
    print(zonename.text)