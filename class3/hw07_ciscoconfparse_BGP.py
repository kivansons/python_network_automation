#!/usr/bin/env python
"""
You have the following BGP configuration from a Cisco IOS-XR router:

# See Router_BGP_Config var

From this BGP configuration, retrieve all of BGP peer IP addresses and their corresponding remote-as.
Return a list of tuples. The tuples should be (neighbor_ip, remote_as). Print your data-structure to standard output.

Your output should look similar to the following. Use ciscoconfparse to accomplish this.

​BGP Peers:
[('10.220.88.20', '42'), ('10.220.88.32', '43')]
"""

from ciscoconfparse import CiscoConfParse
from pprint import pprint
router_BGP_config = """
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
"""
BGP_peers = []

# Parse config with CiscoConfParse
BGP_obj = CiscoConfParse(router_BGP_config.splitlines())

neighbors = BGP_obj.find_objects_w_child(parentspec=r"^\s+neighbor",childspec=r"^\s+remote-as")

for neighbor in neighbors:
    remote_as = neighbor.re_search_children(r"^\s+remote-as")
    remote_as = remote_as[0]
    _, neighbor_str = neighbor.text.split()
    _, remote_as_str = remote_as.text.split()
    BGP_peers.append((neighbor_str, remote_as_str))

pprint(BGP_peers)