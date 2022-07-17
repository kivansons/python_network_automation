#!/usr/bin/env python
"""
7a. Create an nxapi_plumbing "Device" object for nxos1.
The api_format should be "xml" and the transport should be "https" (port 8443). Use getpass() to capture the device's password.
Send the "show interface Ethernet1/1" command to the device, parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands: "show system uptime" and "show system resources". Print the XML output from these two commands.


7c. Using the nxapi_plumbing config_list() method, configure two loopbacks on nxos1 including interface descriptions. Pick random loopback interface numbers between 100 and 199.

"""
from doctest import OutputChecker
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

# Send "show interface Ethernet1/1" and store XML result
output = device.show("show interface Ethernet1/1")

# Unpack XML data and get desired values then print
output = output.find("body").find("TABLE_interface").find("ROW_interface")
interface = output.find("interface")
state = output.find("state")
mtu = output.find("eth_mtu")
print("\n\n")
print(f"Formatted Interface Information")
print("-" * 80)
print(f"Interface: {interface.text}; State: {state.text}; MTU: {mtu.text}")
"""
7b. Run the following two show commands on the nxos1 device using a single method and passing in a list of commands:
"show system uptime" and "show system resources".
Print the XML output from these two commands.
"""
commands = [
    "show system uptime",
    "show system resources"
]

output_list = device.show_list(commands)

for command,result in zip(commands,output_list):
    print("\n\n")
    print(f'XML result from "{command}')
    print("-" * 80)
    pprint(etree.tostring(result).decode())

"""
7c. Using the nxapi_plumbing config_list() method,
configure two loopbacks on nxos1 including interface descriptions.
Pick random loopback interface numbers between 100 and 199.
"""