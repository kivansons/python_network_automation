#!/usr/bin/env python
"""
Note, this exercise might be fairly challenging.
Construct a new YAML file that contains the four Arista switches.
This YAML file should contain all of the connection information need to create a pyeapi connection using the connect method.
Using this inventory information and pyeapi, create a Python script that configures the following on the four Arista switches:

interface {{ intf_name }}
   ip address {{ intf_ip }}/{{ intf_mask }}

The {{ intf_name }} should be a Loopback interface between 1 and 99 (for example Loopback99).

The {{ intf_ip }} should be an address from the 172.31.X.X address space.
The {{ intf_mask }} should be either a /24 or a /30.

Each Arista switch should have a unique loopback number, and a unique interface IP address.

You should use Jinja2 templating to generate the configuration for each Arista switch.

The data for {{ intf_name }} and for {{ intf_ip }} should be stored in your YAML file
and should be associated with each individual Arista device. 
For example, here is what 'arista4' might look like in the YAML file:

​arista4:
  transport: https
  host: arista4.lasthop.io
  username: pyclass
  port: 443
  data:
    intf_name: Loopback99
    intf_ip: 172.31.1.13
    intf_mask: 30


Use pyeapi to push this configuration to the four Arista switches.
Use pyeapi and "show ip interface brief" to display the IP address table after the configuration changes have been made.
"""
# Todo:
# [x] import python dependencies [jinja, yaml, eapi, getpass]
# [x] build yaml device inventory
# [x] write jinja template
# [x] write funct to load yaml file
# [x] write function to build eapi connections and node and add eapi node objects to device_dict as eapi_node
# [] write function to load jinja template file, render configs and store in device_dict as conf_payload
# [X] write function to send configs via eapi
# [] write function to send and display "show ip interface brief"
# [] build main loop
#       [] get device_dict with load_devices_from_yaml()
#       [] get password from user and add to all devices in device_dict
#       [] establish eapi connections to all devices with eapi_build_connections()
#       [] Render configs with render_jinja2_config()
#       [] Send configs with eapi_send_config()
#       [] 
import yaml
import pyeapi
from getpass import getpass
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

def load_devices_from_yaml(device_filepath: str) -> dict:
    """Loads devices from YAML file at device_filepath. Returns a dictionary python object"""
    with open(device_filepath, "r") as f:
        device_dict = yaml.safe_load(f)
    return device_dict.copy()

def render_jinja2_config(device_dict: dict, template_filepath: str) -> None:
    """function to load jinja template file, render configs and store in device_dict as conf_payload"""
    # Set strict undefined var checking
    env = Environment(undefined=StrictUndefined)
    # Look for jinja2 templates in local dir
    env.loader = FileSystemLoader(".")
    template_file = template_filepath
    template = env.get_template(template_filepath)
    
    output = template.render(**cisco3_vars)

def eapi_build_connnections(device_dict: dict) -> None:
    """Accepts a dict containing device credentials and builds pyeapi node objects.
    node objects will be added to supplied dict with 'eapi_node' key.
    
    Expected dict structure:
    device_dict = {
        "arista1": {
            "transport": "https",
            "host": "arista1.lasthop.io",
            "username": "example_user",
            "password": "example_pass"
            "port": "443"
        },
    }
    """
    for device,credentials in device_dict.items():
        connection = pyeapi.client.connect(**credentials)
        device_dict[device]["eapi_node"] = pyeapi.client.Node(connection)
    return



def eapi_send_config(device_dict: dict) -> None:
    """Accepts a dict of devices with "eapi_node" and "conf_payload keys and sends the config payload to each device in list"""
    for device in device_dict.values():
        hostname = device.get("host")
        node = device.get("eapi_node")
        config = device.get("conf_payload")
        if node is not None and config is not None:
            print(f"Sending the following config to {hostname}:")
            print(config)
            node.config(config)
        else:
            if node is None:
                print(f"Missing eapi_node for {hostname}")
            if config is None:
                print(f"Missing config for {hostname}")
            print(f"Skiping {hostname} configuration")

if __name__ == __main__:
    # Start of main loop