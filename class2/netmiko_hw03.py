#!/usr/bin/env python
"""On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index).
Look at some of the commands available for cisco_ios
(you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this).
Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors'
against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors'
(dictionary, list, string, something else)?
The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to).
From this LLDP data, print out the remote device's interface.
In other words, print out the port number on the HPE switch that Cisco4 connects into.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass

cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": getpass(prompt="Cisco4 Password: "),
    "device_type": "cisco_ios",
}

# Connect to Cisco4 and show prompt
net_connect = ConnectHandler(**cisco4)
print(net_connect.find_prompt())

# Send show version command to cisco4
show_version_output = net_connect.send_command("show version", use_textfsm=True)
print("Show Version Command")
print("-" * 80)
pprint(show_version_output)

# Send show LLDP neighbor to cisco4
show_lldp_output = net_connect.send_command("show lldp neighbors", use_textfsm=True)
print("Show LLDP neighbor command")
print("-" * 80)
pprint(show_lldp_output)
print(f"hello {cisco4.get("host")} is connected to port {show_lldp_output[0]["neighbor_interface"]} of {show_lldp_output[0]["neighbor"]}")