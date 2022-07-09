"""
Using your external YAML file and your function located in my_funcs.py,
use pyeapi to connect to arista4.lasthop.io and retrieve "show ip route". 
From this routing table data, extract all of the static and connected routes from the default VRF. 
Print these routes to the screen and indicate whether the route is a connected route or a static route.
In the case of a static route, print the next hop address.
"""
from my_functs import load_devices_from_yaml
from getpass import getpass
from pprint import pprint
import pyeapi

# Load devices from YAML file
device_file = "eapi_devices.yaml"
device_dict = load_devices_from_yaml(device_file)

# get password from user
password = getpass()

# loop through device_dict and add password
for device in device_dict.keys():
    device_dict[device]["password"] = password

# buld connection and then node from arista4 in device_dict
connection = pyeapi.client.connect(**device_dict["arista4"])
node = pyeapi.client.Node(connection)

output = node.enable("show ip route")

pprint(output)