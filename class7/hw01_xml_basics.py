#!/usr/bin/env python
"""
1a Using the show_security_zones.xml file,
read the file contents and parse the file using etree.fromstring(). 
Print out the newly created XML variable and also print out the variable's type. 
Your output should look similar to the following:

​<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>
"""
from lxml import etree

# Open and read XML file
xml_file = "show_security_zones.xml"
with open(xml_file, "r") as f:
    my_xml = f.read()

security_zones = etree.fromstring(my_xml)

print("Printing XML Variable 'security_zones'")
print(security_zones)
print(f"It's type is: {type(security_zones)}")


"""
1b. Using your XML variable from exercise 1a,
print out the entire XML tree in a readable format (ensure that the output string is a unicode string).
"""
print("\n\nPrinting the XML tree")
print("-" * 80)
print(etree.tostring(security_zones).decode())

"""
1c. Print out the root element tag name (this tag should have a value of "zones-information").
Print the number of child elements of the root element (you can retrieve this using the len() function).
"""
print(f"\n\nThe root element tag name is: {security_zones.tag}")
print(f"It has {len(security_zones)} child elements")

"""
1d. Using both direct indices and the getchildren() method, obtain the first child element and print its tag name. 
"""
print("\n\nUsing direct indices, the first child element's tag name is:")
print("-" * 80)
print(security_zones[0].tag)

print("\nUsing the getchildren() method. The first child element's tag name is:")
print("-" * 80)
print(security_zones.getchildren()[0].tag)

"""
1e. Create a variable named "trust_zone". Assign this variable to be the first "zones-security" element in the XML tree. 
Access this newly created variable and print out the text of the "zones-security-zonename" child.
"""
print("\n\n")
print('Unpacking the first child element into "trust_zone" variable')
print("-" * 80)
trust_zone = security_zones[0]
print(f'The "trust-zone" element variable, child tag "{trust_zone[0].tag}" has a text value of "{trust_zone[0].text}"')

"""
1f. Iterate through all of the child elements of the "trust_zone" variable. Print out the tag name for each child element.
"""
print("\n\n")
print('Iterating through all child elements in "security_zones"')
print("-" * 80)
for child_element in security_zones:
    print(child_element.tag)