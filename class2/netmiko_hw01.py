"""Use the extended 'ping' command and Netmiko on the 'cisco4' router.
 This should prompt you for additional information as follows:
 
 ##########################
 cisco4#ping
Protocol [ip]:
Target IP address: 8.8.8.8
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]:
Sweep range of sizes [n]:
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms
##########################

a. Use send_command_timing() to handle the additional prompting from this 'ping' command.
 pecify a target IP address of '8.8.8.8'

b. Use send_command() and the expect_string argument to handle the additional prompting.
Once again specify a target IP address of '8.8.8.8'.

 """
from netmiko import ConnectHandler
from getpass import getpass

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

net_connect = ConnectHandler(**hosts["cisco4"])
print(net_connect.find_prompt())
