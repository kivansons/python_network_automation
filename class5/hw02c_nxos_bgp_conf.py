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
"""
import re
import os
import yaml
from time import sleep
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
print("\nNxos1 config output\n" + ("-" * 80))
print(output)
output = nxos2_net_connect.send_config_set(splitlines_strip(nxos2_conf_commands))
print("\nNxos2 config output\n" + ("-" * 80))
print(output)

# Verify that desired config state has been reached
# ping neighbor
ping_peer = f"ping {bgp_conf['nxos1']['peer_ip']}"
ping_output = nxos1_net_connect.send_command(ping_peer)
print("\nPinging nxos1 from nxos2\n" + "-" * 80)
print(ping_output)
if "64 bytes from" in ping_output:
    print("Ping was successful!")
    ping_success = True
elif "64 bytes from" not in ping_output:
    print("Ping failed!")
    ping_success = False

# Sleep while waiting for BGP session to establish
sleep_time = 15
print(f"\nWaiting for {sleep_time} seconds to allow BGP session to establish\n")
sleep(sleep_time)

# Check if BGP peering worked
print("Sending show command to nxos1")
bgp_check = f"show ip bgp summary | include {bgp_conf['nxos1']['peer_ip']}"
print(f"Command sent:\n{bgp_check}\n")
bgp_output = nxos1_net_connect.send_command(bgp_check)
print(f"Response received:\n{bgp_output}")
# Search from end of string looking for first nonwhitespace block of chars
bgp_re_search = re.search(r"\s+(\S+)\s*$", bgp_output)
bgp_state = bgp_re_search.group(1)

try:
    # If bgp session is established cisco will show an integer value of prefixes
    int(bgp_state)
    print(f"BGP peering established. {bgp_state} prefixes received")
    bgp_success = True
except ValueError:
    # If BGP session is not established bgp_state will be a non-int string
    print("BGP peering failed")
    bgp_success = False

# Close connections to devices
nxos1_net_connect.disconnect()
nxos2_net_connect.disconnect()

# Print outcome of configuration
print("\n")
if (ping_success is True) and (bgp_success is True):
    print("Configuration was successful!")
if ping_success is False:
    print(f"Configuration was unsuccessful\nPing check to {bgp_conf['nxos1']['peer_ip']} failed")
if bgp_success is False:
    print(f"Configuration was unsuccessful\nBGP peering not established")