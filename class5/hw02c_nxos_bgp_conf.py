#!/usr/bin/env python
"""
Use Netmiko to push the configurations generated in exercise 2b to the nxos1 device and to the nxos2 device, respectively.
Verify you are able to ping between the devices and also verify that the BGP session reaches the established state.
Note, you might need to use an alternate interface besides Ethernet 1/1 (you can use either Ethernet 1/1, 1/2, 1/3, or 1/4).
Additionally, you might need to use a different IP network (to avoid conflicts with other students).
Your autonomous system should remain 22, however.

For this exercise you should store your Netmiko connection dictionaries in an external file named my_devices.py
and should import nxos1, and nxos2 from that external file.
Make sure that you use getpass() to enter the password in for these devices (as opposed to storing the definitions in the file).

Mermaid flow chart
graph TD
    A[Show IP int brief] --> B{Is IP Configured?}
    B --> |Yes| C[Remove address]
    B --> |No| D[Send IP Address config]
    C --> D
    D --> E[Show IP BGP summary]
    E --> F{Is Peer Established?
"""
import re
import os
import yaml
from netmiko import ConnectHandler
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

def splitlines_strip(commands: str) -> list:
    """Accepts a multi line string of config commands,
    returns a list of config lines with leading and trailing whitespace striped"""
    commands_list = [command.strip() for command in commands.splitlines()]
    return commands_list.copy()

# Set strict jinja2 undefined var checking and look for templates in current dir
env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader(".")
# Load lab hosts file from home dir
home_dir = os.path.expanduser("~")
with open(f"{home_dir}/.netmiko.yml", "r") as f:
    netmiko_hosts = yaml.safe_load(f)

# Device BGP config params
bgp_conf = {
    "nxos1": {
        "interface": "Ethernet1/1",
        "ip_address": "10.1.100.1",
        "cidr": "24",
        "local_as": "22",
        "peer_ip": "10.1.100.2",
    },
    "nxos2": {
        "interface": "Ethernet1/1",
        "ip_address": "10.1.100.2",
        "cidr": "24",
        "local_as": "22",
        "peer_ip": "10.1.100.1",
    },
}


# load jinja template file and render config commands
template_file = "hw02c_nxos_bgp_conf.j2"
template = env.get_template(template_file)
nxos1_conf_commands = template.render(**bgp_conf["nxos1"])
nxos2_conf_commands = template.render(**bgp_conf["nxos2"])

# build netmiko connections to nxos1,nxos2
nxos1_net_connect = ConnectHandler(**netmiko_hosts["nxos1"])
nxos2_net_connect = ConnectHandler(**netmiko_hosts["nxos2"])
print(nxos1_net_connect.find_prompt())
print(nxos2_net_connect.find_prompt())

# Send config to both nxos devices
output = nxos1_net_connect.send_config_set(splitlines_strip(nxos1_conf_commands))
print("Nxos1 config output\n" + ("#" * 80))
print(output)
output = nxos2_net_connect.send_config_set(splitlines_strip(nxos2_conf_commands))
print("Nxos2 config output\n" + ("#" * 80))
print(output)
# Todo: Verify that desired config state has been reached
#  - ping neighbor
ping_peer = f"ping {bgp_conf['nxos1']['peer_ip']}"
ping_output = nxos1_net_connect.send_command(ping_peer)
print("Pinging nxos1 from nxos2")
print(ping_output)
if "64 bytes from" in ping_output:
    print("Ping was successful!")
elif "64 bytes from" not in ping_output:
    print("Ping failed!")
#  - show ip bgp summary
#  - show ip interface brief
