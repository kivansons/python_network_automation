import json
from getpass import getpass

#Network devices in pynet lab
hosts = {
    "cisco3": {
        "host": "cisco3.lasthop.io",
        "snmp_port": 161,
        "ssh_port": 22,
        "username": "pyclass",
        "password": getpass(prompt="Cisco3 Password: "),
        "device_type": "cisco_ios",
    },
    "cisco4": {
        "host": "cisco4.lasthop.io",
        "snmp_port": 161,
        "ssh_port": 22,
        "username": "pyclass",
        "password": getpass(prompt="Cisco4 Password: "),
        "device_type": "cisco_ios",
    },
    "arista1": {
        "host": "arista1.lasthop.io",
        "ssh_port": 22,
        "eapi_port": 443,
        "username": "pyclass",
        "password": getpass(prompt="Arista1 Password: "),
        "device_type": "arista_eos",
    },
    "arista2": {
        "host": "arista2.lasthop.io",
        "ssh_port": 22,
        "eapi_port": 443,
        "username": "pyclass",
        "password": getpass(prompt="Arista2 Password: "),
        "device_type": "arista_eos",
    },
    "arista3": {
        "host": "arista3.lasthop.io",
        "ssh_port": 22,
        "eapi_port": 443,
        "username": "pyclass",
        "password": getpass(prompt="Arista3 Password: "),
        "device_type": "arista_eos",
    },
    "arista4": {
        "host": "arista4.lasthop.io",
        "ssh_port": 22,
        "eapi_port": 443,
        "username": "pyclass",
        "password": getpass(prompt="Arista4 Password: "),
        "device_type": "arista_eos",
    },
    "srx2": {
        "host": "srx2.lasthop.io",
        "ssh_port": 22,
        "netconf_port": 830,
        "username": "pyclass",
        "password": getpass(prompt="srx2 Password: "),
        "device_type": "juniper",
    },
    "nxos1": {
        "host": "nxos1.lasthop.io",
        "ssh_port": 22,
        "nxapi_port": 8443,
        "username": "pyclass",
        "password": getpass(prompt="nsos1 Password: "),
        "device_type": "cisco_nxos",
    },
    "nxos2": {
        "host": "nxos2.lasthop.io",
        "ssh_port": 22,
        "nxapi_port": 8443,
        "username": "pyclass",
        "password": getpass(prompt="nxos2 Password: "),
        "device_type": "cisco_nxos",
    },
}

#Write Hosts to json
with open("./pynet_hosts.json", "w") as json_output:
    json.dump(hosts, json_output)