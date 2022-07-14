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
# [x] write function to load jinja template file, render configs and store in device_dict as conf_payload
# [x] write function to send configs via eapi
# [X] write function to send and display "show ip interface brief"
# [X] build main loop
#       [X] get device_dict with load_devices_from_yaml()
#       [X] get password from user and add to all devices in device_dict
#       [X] establish eapi connections to all devices with eapi_build_connections()
#       [X] Render configs with render_jinja2_config()
#       [X] Send configs with eapi_send_config()
#       [X] Show output of "show ip interface brief" with eapi_show_ip_inter_brief()
import yaml
import pyeapi
from getpass import getpass
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

def load_devices_from_yaml(device_filepath: str) -> dict:
    """Loads devices from YAML file at device_filepath. Returns a python dictionary object"""
    with open(device_filepath, "r") as f:
        device_dict = yaml.safe_load(f)
    return device_dict.copy()

def render_jinja2_config(device_dict: dict, template_filepath: str) -> None:
    """function to load jinja template file, render configs and store in device_dict as config_payload"""
    # Set strict undefined var checking
    env = Environment(undefined=StrictUndefined)
    # Look for jinja2 templates in local dir
    env.loader = FileSystemLoader(".")
    template = env.get_template(template_filepath)
    
    for key,config in device_dict.items():
        config = template.render(**config["data"])
        config_payload = [line.strip() for line in config.splitlines()]
        device_dict[key]["config_payload"] = config_payload
    return

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
    """Accepts a dict of devices with "eapi_node" and "config_payload" keys and sends the config payload to each device in list"""
    
    for device in device_dict.values():
        hostname = device.get("host")
        node = device.get("eapi_node")
        config = device.get("config_payload")

        print(f"Sending the following config to {hostname}:")
        print(config)
        node.config(config)
    
    return

def eapi_show_ip_inter_brief(device_dict: dict) -> None:
    """Accepts a dict of devices with 'eapi_node' and prints the output of 'show ip interface brief'"""
    for device in device_dict.values():
        
        # Send command to device
        hostname = device["host"]
        node = device["eapi_node"]
        command = "show ip interface brief"
        output = node.enable(command)
        output = output[0]["result"]["interfaces"]

        # Print header
        print(f'\n{hostname}: output of "{command}"')
        print("-" * 80)
        print(f"{'Interface':15}{'IP Address':15}{'Status':15}{'Protocol':15}")
        
        #Parse results of "show ip interface brief" and print line by line
        for interface_data in output.values():
            
            interface = interface_data["name"]

            ip_address = interface_data["interfaceAddress"]
            ip_address = ip_address["ipAddr"]
            ip_address = ip_address["address"] + "/" + str(ip_address["maskLen"])

            status = interface_data["interfaceStatus"]
            
            protocol = interface_data["lineProtocolStatus"]

            print(f"{interface:15}{ip_address:15}{status:15}{protocol:15}")
        

if __name__ == "__main__":
    device_file = "hw04_devices.yaml"
    jinja2_template_file = "hw04_loopback_intf_conf.j2"
    device_dict = load_devices_from_yaml(device_file)

    # Get password from user and store in device_dict
    password = getpass()
    for device in device_dict.keys():
        device_dict[device]["password"] = password

    render_jinja2_config(device_dict, jinja2_template_file)
    eapi_build_connnections(device_dict)
    eapi_send_config(device_dict)
    eapi_show_ip_inter_brief(device_dict)