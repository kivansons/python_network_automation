"""
Define an Arista device in an external YAML file (use arista4.lasthop.io for the device).
In your YAML file, make sure the key names exactly match the names required for use with pyeapi and the connect() method.
In other words, you should be able to execute 'connect(**device_dict)' where device_dict was retrieved from your YAML file.
Do not store the lab password in this YAML file, instead set the password using getpass() in your Python program.
Using this Arista device information stored in a YAML file, repeat the 'show ip arp' retrieval using pyeapi. 
Once again, from this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
"""
import yaml
import pyeapi
from getpass import getpass

# Load devices from YAML file
device_file = "eapi_devices.yaml"
with open(device_file, "r") as f:
    device_dict = yaml.safe_load(f)

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
for hostname_json_data,arp_json_data in zip(hostname_output,arp_output):
    # unpack hostname from hostname data
    hostname = hostname_json_data[0]["result"]["hostname"]
    # Unpack arp table from json data
    arp_table = arp_json_data[0]["result"]["ipV4Neighbors"]

    # Print Header
    print(f"{hostname} arp bindings")
    print("-" * 80)
    # Print ARP entries
    for arp_entry in arp_table:
        ip = arp_entry.get("address")
        mac = arp_entry.get("hwAddress")
        print(f"{ip} is bound to {mac}")
