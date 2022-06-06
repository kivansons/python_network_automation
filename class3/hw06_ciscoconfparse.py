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

# Connect to Cisco4 and get running config
net_connect = ConnectHandler(**netmiko_hosts["cisco4"])
running_config = net_connect.send_command("show run")
pprint(running_config)

# Pass cisco4 running_config to CiscoConfParse as list of lines
cisco4_conf = CiscoConfParse(running_config.splitlines())

# Find and save interface objects then pprint
interfaces = cisco4_conf.find_objects(r"^interface")
pprint(interfaces)

# Search for "ip address" child commands of interfaces
interface_addresses = [address for address in interfaces.re_search_children(r"^ip address")]
pprint(interface_addresses)