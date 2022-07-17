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
commands = [
    "show interface Ethernet1/1"
]
output = device.show_list(commands)
pprint(etree.tostring(output).decode())
