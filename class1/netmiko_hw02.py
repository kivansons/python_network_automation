#!/usr/bin/env python
"""
2. Add a second NX-OS device to your first exercise.
Make sure you are using dictionaries to represent the two NX-OS devices.
Additionally, use a for-loop to accomplish the Netmiko connection creation.
Once again print the prompt back from the devices that you connected to.
"""
from netmiko import ConnectHandler
from getpass import getpass

nx_password = getpass()

nx01 = {
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": nx_password,
    "device_type": "cisco_nxos",
}

nx02 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": nx_password,
    "device_type": "cisco_nxos",
}
devices = [nx01, nx02]
for device in devices:
    connection = ConnectHandler(**device)
    print(connection.find_prompt())
