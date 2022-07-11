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

"""
example output data structure
[{'command': 'show ip route',
  'encoding': 'json',
  'result': {'vrfs': {'default': {'allRoutesProgrammedHardware': True,
                                  'allRoutesProgrammedKernel': True,
                                  'defaultRouteState': 'reachable',
                                  'routes': {'0.0.0.0/0': {'directlyConnected': False,
                                                           'hardwareProgrammed': True,
                                                           'kernelProgrammed': True,
                                                           'metric': 0,
                                                           'preference': 1,
                                                           'routeAction': 'forward',
                                                           'routeType': 'static',
                                                           'vias': [{'interface': 'Vlan1',
                                                                     'nexthopAddr': '10.220.88.1'}]},
                                             '10.220.88.0/24': {'directlyConnected': True,
                                                                'hardwareProgrammed': True,
                                                                'kernelProgrammed': True,
                                                                'routeAction': 'forward',
                                                                'routeType': 'connected',
                                                                'vias': [{'interface': 'Vlan1'}]}},
                                  'routingDisabled': False}}}}]

"""
# Unpack default vrf routes dictionary from api output
routes = output[0]["result"]["vrfs"]["default"]["routes"]

# Pull route prefix,type, and nexthop(if applicable) from route
for key,values in routes.items():
    route_prefix = key
    route_type = values["routeType"]
    if route_type.lower() == "static":
        route_nexthop_addr = values["vias"][0]["nexthopAddr"]
    else:
        route_nexthop_addr = None
    print(f"{route_prefix:20} {route_type:20} {route_nexthop_addr:20}")