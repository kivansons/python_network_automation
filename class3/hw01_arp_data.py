#!/usr/bin/env python
"""
Using the below ARP data, create a five element list.
 Each list element should be a dictionary with the following keys: "mac_addr", "ip_addr", "interface".
  At the end of this process, you should have five dictionaries contained inside a single list.

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""
from pprint import pprint

arp_data = [
    {
        "mac_addr": "0062.ec29.70fe",
        "ip_addr": "10.220.88.1",
        "interface": "Gi0/0/0",
    },
    {
        "mac_addr": "c89c.1dea.0eb6",
        "ip_addr": "10.220.88.20",
        "interface": "Gi0/0/0",
    },
    {
        "mac_addr": "a093.5141.b780",
        "ip_addr": "10.220.88.22",
        "interface": "Gi0/0/0",
    },
    {
        "mac_addr": "0001.00ff.0001",
        "ip_addr": "10.220.88.37",
        "interface": "Gi0/0/0",
    },
    {
        "mac_addr": "0002.00ff.0001",
        "ip_addr": "10.220.88.38",
        "interface": "Gi0/0/0",
    },
]

pprint(arp_data)
