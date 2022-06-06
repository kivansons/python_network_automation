#!/usr/bin/env python
"""
6. Use Netmiko to retrieve 'show run' from the Cisco4 device. Feed this configuration into CiscoConfParse.

Use CiscoConfParse to find all of the interfaces on Cisco4 that have an IP address.
Print out the interface name and IP address for each interface.
Your solution should work if there is more than one IP address configured on Cisco4.
For example, if you configure a loopback interface on Cisco4 with an IP address, then your solution should continue to work.
The output from this program should look similar to the following:

$ python confparse_ex6.py

Interface Line: interface GigabitEthernet0/0/0
IP Address Line:  ip address 10.220.88.23 255.255.255.0
"""
import yaml
import os
from pprint import pprint
from netmiko import ConnectHandler
from ciscoconfparse import CiscoConfParse

# Import list of lab devices from netmiko.yml
home_dir = os.path.expanduser("~")
with open(f"{home_dir}/.netmiko.yml", "r") as f:
    netmiko_hosts = yaml.safe_load(f)


test_loopback_commands = [
    "interface Loopback100",
    "description test loopback for for class3 exercise 6",
    "ip address 192.0.2.1 255.255.255.255",
    "interface Loopback101",
    "description test loopback for for class3 exercise 6",
    "ip address 198.51.100.2 255.255.255.255 secondary",
    "ip address 198.51.100.3 255.255.255.255 secondary",
    "ip address 198.51.100.1 255.255.255.255",
]
# Connect to Cisco4, configure loopback IPs and get running config
net_connect = ConnectHandler(**netmiko_hosts["cisco4"])
net_connect.send_config_set(test_loopback_commands)
running_config = net_connect.send_command("show run")
pprint(running_config)

# Pass cisco4 running_config to CiscoConfParse as list of lines
cisco4_conf = CiscoConfParse(running_config.splitlines())

# Find and save interface objects that have an ip assigned then pprint
# childspec= regex breakdown: (^) char looks for begining of line, (\s+) a whitespace char one or more times,
# (ip address) the literal string "ip address".
# Put togeather... find lines that start with one or more whitespaces then the string "ip address"
interfaces = cisco4_conf.find_objects_w_child(
    parentspec=r"^interface", childspec=r"^\s+ip address"
)
pprint(interfaces)

# For each interface in interfaces list, print the interface name then all ip address configuration lines
for interface in interfaces:
    print(f"\nInterface line: {interface.text}")
    for address in interface.re_search_children(r"^\s+ip address"):
        print(f"Address line: {address.text}")