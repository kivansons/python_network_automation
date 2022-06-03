#!/usr/bin/env python
"""
You have the following JSON ARP data from an Arista switch:

# See ./hw04_json_arp_data.json
From a file, read this JSON data into your Python program.
Process this ARP data and return a dictionary,
where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses. 
Print this dictionary to standard output.

"""
import json
from pprint import pprint
with open("hw04_json_arp_data.json", "r") as f:
    arista_arp = json.load(f)

arp_entries = {}

arp_list = arista_arp["ipV4Neighbors"]
for item in arp_list:
    arp_entries.update({item["address"]: item["hwAddress"]})

pprint(arp_entries)