#!/usr/bin/env python
"""
Expand your Jinja2 template such that both the following interface and BGP configurations are generated for nxos1 and nxos2.
The interface name, IP address, netmask, local_as, and peer_ip should all be variables in the template.
This is iBGP so the remote_as will be the same as the local_as.

nxos1

interface Ethernet1/1
  ip address 10.1.100.1/24

router bgp 22
  neighbor 10.1.100.2 remote-as 22
    address-family ipv4 unicast

nxos2

interface Ethernet1/1
  ip address 10.1.100.2/24

router bgp 22
  neighbor 10.1.100.1 remote-as 22
    address-family ipv4 unicast

"""
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set strict undefined var checking
env = Environment(undefined=StrictUndefined)
# Load jinja2 templates from local dir
env.loader = FileSystemLoader(".")

nxos1_conf = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.1",
    "cidr": "24",
    "local_as":"22",
    "peer_ip": "10.1.100.2"
}
nxos2_conf = {
    "interface": "Ethernet1/1",
    "ip_address": "10.1.100.2",
    "cidr": "24",
    "local_as":'22',
    "peer_ip": "10.1.100.1"
}

template_file = "hw02c_nxos_bgp_conf.j2"
template = env.get_template(template_file)
nxos1_output = template.render(**nxos1_conf)
nxos2_output = template.render(**nxos2_conf)

print(f"nxos1\n{nxos1_output}\n\nnxos2\n{nxos2_output}")
