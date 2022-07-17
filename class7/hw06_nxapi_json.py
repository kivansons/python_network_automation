#!/usr/bin/env python
"""
6a. Create an nxapi_plumbing "Device" object for nxos1.
The api_format should be "jsonrpc" and the transport should be "https" (port 8443).
Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device,
parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
"""
import requests
from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password=getpass(),
    transport="https",
    port=8443,
    verify=False,
)

output = device.show("show interface Ethernet1/1")
pprint(output)
