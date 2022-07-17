#!/usr/bin/env python
"""
6a. Create an nxapi_plumbing "Device" object for nxos1.
The api_format should be "jsonrpc" and the transport should be "https" (port 8443).
Use getpass() to capture the device's password. Send the "show interface Ethernet1/1" command to the device,
parse the output, and print out the following information:

Interface: Ethernet1/1; State: up; MTU: 1500
"""
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

# Send show interface command and print raw data
output = device.show("show interface Ethernet1/1")
print('raw output of "show interface Ethernet1/1"')
print("-" * 80)
pprint(output)

# Unpack data and get desired values then print
output = output["TABLE_interface"]["ROW_interface"]
interface = output["interface"]
state = output["state"]
mtu = output["eth_mtu"]
print("\n\n")
print(f"Formatted interface information")
print("-" * 80)
print(f"Interface: {interface}; State: {state}; MTU: {mtu}")