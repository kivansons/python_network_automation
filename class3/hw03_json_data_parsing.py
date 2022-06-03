#!/usr/bin/env python
"""
NAPALM using nxos_ssh has the following data structure in one of its unit tests (the below data is in JSON format).

### Data in hw03_json_data.json

Read this JSON data in from a file.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device.
From this data create two lists: 'ipv4_list' and 'ipv6_list'.
The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes;
the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.
"""
import json
import ipaddress

# Read in data from JSON file
with open("./hw03_json_data.json", "r") as f:
    json_data = json.load(f)

ipv4_list = []
ipv6_list = []

# Parse json data and create two lists containing all ipv4, and ipv6 addresses
for interface in json_data.values():
    # Try to get ipv4 dict from interface
    ipv4 = interface.get("ipv4")
    # If interface has an ipv4 key continue parsing ipv4
    if ipv4 is not None:
        # unpack each ipv4 tuple and append values to ipv4_list
        for address, prefix_dict in ipv4.items():
            prefix = prefix_dict["prefix_length"]
            ipv4_string = f"{address}/{prefix}"
            interface_address = ipaddress.ip_interface(ipv4_string)
            ipv4_list.append(interface_address)

    # Try to get ipv6 dict fom interface
    ipv6 = interface.get("ipv6")
    # If interface has an ipv6 key continue parsing ipv6
    if ipv6 is not None:
        # Unpack each ipv6 tuple and append values to ipv6_list
        for address, prefix_dict in ipv6.items():
            prefix = prefix_dict["prefix_length"]
            ipv6_string = f"{address}/{prefix}"
            interface_address = ipaddress.ip_interface(ipv6_string)
            ipv6_list.append(interface_address)

print("IPv4 addresses")
print("-" * 80)
for interface_address in ipv4_list:
    print(interface_address.with_prefixlen)

print("\nIPv6 addresses")
print("-" * 80)
for interface_address in ipv6_list:
    print(interface_address.with_prefixlen)
