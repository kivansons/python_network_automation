#!/usr/bin/env python
"""
Create a Python program that uses Jinja2 to generate the below BGP configuration.
Your template should be directly embedded inside of your program as a string and should use for the following variables:
local_as, peer1_ip, peer1_as, peer2_ip, peer2_as.
cisco1(conf):
router bgp 10
  neighbor 10.1.20.2 remote-as 20
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor 10.1.30.2 remote-as 30
    address-family ipv4 unicast
"""
from jinja2 import Template

# jinja2 template
template = """
router bgp {{ local_as }}
  neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{ peer2_ip }} remote-as {{ peer2_as }}
    address-family ipv4 unicast
"""
# Config Params
config = {
    "local_as": "10",
    "peer1_ip": "10.1.20.2",
    "peer1_as": "20",
    "peer2_ip": "10.1.30.2",
    "peer2_as": "30",
}

# Load jinja 2 template and render config text
j2_template = Template(template)
conf_render = j2_template.render(**config)
print(conf_render)
