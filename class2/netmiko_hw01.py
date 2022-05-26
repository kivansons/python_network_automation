#!/usr/bin/env python
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
from ast import Str
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

# ping command and directives
ping_command = [
    "ping",
    "ip",
    "8.8.8.8",
    "5",
    "100",
    "2",
    "n",
    "n",
]
# expected string response for ping_command of same index
ping_expected_string = [
    "Protocol",
    "Target IP address",
    "Repeat count",
    "Datagram size",
    "Timeout in seconds",
    "Extended Commands",
    "Sweep range",
    "#",
]

# Establish connection to cisco4 and print prompt
net_connect = ConnectHandler(**hosts["cisco4"])
print(net_connect.find_prompt())

# Send ping command to cisco4 via send_command_timing method
output = ""
for command in ping_command:
    output += net_connect.send_command_timing(
        command, strip_prompt=False, strip_command=False
    )
print("\nOutput using send_command_timing method is: ")
print(output)

# Send ping command to cisco4 via send_command and use "expect_string" arg to detect prompt
output = ""
for i, command in enumerate(ping_command):
    output += net_connect.send_command(
        command,
        expect_string=ping_expected_string[i],
        strip_prompt=False,
        strip_command=False,
    )
print("\nOutput using send_command method is: ")
print(output)
