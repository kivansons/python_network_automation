#!/usr/bin/env python
"""On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names
(just pick 5 VLAN numbers between 100 - 999). Use Netmiko's send_config_from_file() method to accomplish this.
Also use Netmiko's save_config() method to save the changes to the startup-config."""
from netmiko import ConnectHandler
from getpass import getpass

lab_password = getpass()
hosts = {
    "cisco3": {
        "host": "cisco3.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "cisco_ios",
    },
    "cisco4": {
        "host": "cisco4.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "cisco_ios",
    },
    "arista1": {
        "host": "arista1.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "arista_eos",
    },
    "arista2": {
        "host": "arista2.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "arista_eos",
    },
    "arista3": {
        "host": "arista3.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "arista_eos",
    },
    "arista4": {
        "host": "arista4.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "arista_eos",
    },
    "srx2": {
        "host": "srx2.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "juniper",
    },
    "nxos1": {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "cisco_nxos",
    },
    "nxos2": {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": lab_password,
        "device_type": "cisco_nxos",
    },
}

# Connect and send config to nxos1
net_connect = ConnectHandler(**hosts["nxos1"])
net_connect.find_prompt()
output = net_connect.send_config_from_file(config_file="netmiko_hw05_conf_file.txt")
print(output)
net_connect.disconnect()

# Connect and send config to nxos2
net_connect = ConnectHandler(**hosts["nxos2"])
net_connect.find_prompt()
output = net_connect.send_config_from_file(config_file="netmiko_hw05_conf_file.txt")
print(output)
net_connect.disconnect()
