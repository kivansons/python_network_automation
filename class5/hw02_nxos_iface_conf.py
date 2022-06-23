#!/usr/bin/env python
"""
Use Python and Jinja2 to generate the below NX-OS interface configuration. 
You should use an external template file and a Jinja2 environment to accomplish this. 
The interface, ip_address, and netmask should all be variables in the Jinja2 template.

nxos1
interface Ethernet1/1
  ip address 10.1.100.1/24

nxos2
interface Ethernet1/1
  ip address 10.1.100.2/24
"""
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set strict undefined var checking
env = Environment(undefined=StrictUndefined)
# Load jinja2 templates from local dir
env.loader = FileSystemLoader(".")

nxos1_iface_conf = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.1",
    "cidr": "24",
}
nxos2_iface_conf = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.2",
    "cidr": "24",
}

template_file = "hw02_nxos_iface_conf.j2"
template = env.get_template(template_file)
nxos1_output = template.render(**nxos1_iface_conf)
nxos2_output = template.render(**nxos2_iface_conf)

print(f"nxos1\n{nxos1_output}\n\nnxos2\n{nxos2_output}")
