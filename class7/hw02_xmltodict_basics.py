#!/usr/bin/env python
"""
2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary.
Print out this new variable and its type.
Note, the newly created object is an OrderedDict; not a traditional dictionary.
"""
import xmltodict
from pprint import pprint

xml_file = "show_security_zones.xml"
with open(xml_file,"r") as f:
    my_xml = xmltodict.parse(f.read())

print("PPrinting the xmltodict data structure:")
print("-" * 80)
print(f"my_xml has a type of: {type(my_xml)}")
pprint(my_xml)

"""
2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. 
Your output should look similar to the following (tip, enumerate will probably help):

Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host
"""

print("\n\n")
print("Printing all security zones")
print("-" * 80)
# Unpack outer dicts
zones_security = my_xml["zones-information"]["zones-security"]
# Iterate through list of zones
for i,dict in enumerate(zones_security):
    print(f"Security Zone #{i + 1}: {dict['zones-security-zonename']}")