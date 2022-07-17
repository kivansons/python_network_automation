#!/usr/bin/env python
"""
3a. Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml. 
Use a generic function that accepts an argument "filename" to open and read a file.
Inside this function, use xmltodict to parse the contents of the file.
Your function should return the xmltodict data structure.
Using this function, create two variables to store the xmltodict data structure from the two files.
"""
from pprint import pprint
from typing import OrderedDict
import xmltodict

def parse_xml_file(filename: str, force_list: tuple = None) -> OrderedDict:
    """Accepts an xml file and returnes an xmltodict OrderedDict
       Optional parameter: 'force_list' accepts a touple of strings containing the XML element keys to be forced into lists
       by the xmltodict parser.
    """
    with open(filename, "r") as f:
        if force_list is None:
            xml_dict = xmltodict.parse(f.read())
        else:
            xml_dict = xmltodict.parse(f.read(), force_list=force_list)
    return xml_dict.copy()

if __name__ == "__main__":
    show_security_zones_filename = "show_security_zones.xml"
    show_security_zones_trust_filename = "show_security_zones_trust.xml"
    
    security_zones = parse_xml_file(show_security_zones_filename)
    security_zones_trust = parse_xml_file(show_security_zones_trust_filename,force_list=("zones-security",))

    """
    3b. Compare the Python "type" of the elements at ['zones-information']['zones-security']. 
    What is the difference between the two data types? Why?
    """
    security_zones_branch = security_zones['zones-information']['zones-security']
    security_zones_trust_branch = security_zones_trust['zones-information']['zones-security']

    print(f"Type of security_zones_trust at ['zones-information']['zones-security'] is {type(security_zones_trust_branch)}")
    print(f"Type of security_zones at ['zones-information']['zones-security'] is {type(security_zones_branch)}")
    
    print("\nThe type of the two branches differ because security_zones_trust has a single element")
    print("in the ['zones-information']['zones-security'] branch")
    
    print("\nConversely security_zones has multiple elements in the ['zones-information']['zones-security'] branch")
    print("and xmltodict must use a list to contain the additional elements")
