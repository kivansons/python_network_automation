#!/usr/bin/env python
"""
2a. Create a list where each of the list elements is a dictionary representing one of the network devices in the lab.
Do this for at least four of the lab devices.
The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password.
Use a fictional username/password to avoid checking the lab password into GitHub.

2b. Write the data structure you created in part 2a out to a YAML file. Use expanded YAML format. 
How could you re-use this YAML file later when creating Netmiko connections to devices?
"""
import yaml
hosts = {
    "cisco3": {
        "host": "cisco3.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "cisco_ios",
    },
    "cisco4": {
        "host": "cisco4.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "cisco_ios",
    },
    "arista1": {
        "host": "arista1.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "arista_eos",
    },
    "arista2": {
        "host": "arista2.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "arista_eos",
    },
    "arista3": {
        "host": "arista3.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "arista_eos",
    },
    "arista4": {
        "host": "arista4.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "arista_eos",
    },
    "srx2": {
        "host": "srx2.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "juniper",
    },
    "nxos1": {
        "host": "nxos1.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "cisco_nxos",
    },
    "nxos2": {
        "host": "nxos2.lasthop.io",
        "username": "admin",
        "password": "FakePassword",
        "device_type": "cisco_nxos",
    },
}

with open("./hw02_device_list.yaml", "w") as f:
    yaml.dump(hosts, f, default_flow_style=False)