"""
Create a Python module named 'my_funcs.py'.
In this file create two functions: function1 should read the YAML file you created in exercise 2a 
and return the corresponding data structure; 
function2 should handle the output printing of the ARP entries (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data).
Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.
"""
from my_functs import load_devices_from_yaml,print_arp
from getpass import getpass
import pyeapi

# Load devices from YAML file
device_file = "eapi_devices.yaml"
device_dict = load_devices_from_yaml(device_file)

# get password from user
password = getpass()

# loop through device_dict and add password
for device in device_dict.keys():
    device_dict[device]["password"] = password

# buld connections and then nodes from all devices in device_dict
connections = [pyeapi.client.connect(**device) for device in device_dict.values()]
nodes = [pyeapi.client.Node(connection) for connection in connections]

# Get node hostname and arptable
hostname_output = []
arp_output = []
for node in nodes:
    hostname_output.append(node.enable("show hostname"))
    arp_output.append(node.enable("show ip arp"))

# Loop through "show ip arp" output for each device
for arp_json_data,hostname_json_data in zip(arp_output,hostname_output):
    print_arp(arp_json_data)