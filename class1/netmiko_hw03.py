#!/usr/bin/env python
"""For one of the Cisco IOS devices,
use Netmiko and the send_command() method to retrieve 'show version'. 
Save this output to a file in the current working directory."""
from netmiko import ConnectHandler
from getpass import getpass


password_input = getpass()
cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password_input,
    "device_type": "cisco_ios",
}

connection = ConnectHandler(**cisco3)
cisco3_show_version = connection.send_command("show version")
print(cisco3_show_version)

with open("./cisco3_show_version.txt", "w") as output_file:
    output_file.write(cisco3_show_version)
