"""
Using the pyeapi library, connect to arista3.lasthop.io and execute 'show ip arp'. 
From this ARP table data, print out a mapping of all of the IP addresses and their corresponding MAC addresses.
"""
import pyeapi
from getpass import getpass
from pprint import pprint

# Create connetion to arista3
connection = pyeapi.client.connect(
    transport="https",
    host="arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)

# Create node from connection
device = pyeapi.client.Node(connection)

# Run show ip arp and store output
arp_output = device.enable("show ip arp")

"""
[{'command': 'show ip arp',
  'encoding': 'json',
  'result': {'dynamicEntries': 7,
             'ipV4Neighbors': [{'address': '10.220.88.1',
                                'age': 0,
                                'hwAddress': '0024.c4e9.48ae',
                                'interface': 'Vlan1, Ethernet1'},
                               {'address': '10.220.88.23',
                                'age': 0,
                                'hwAddress': '502f.a8b1.6900',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.28',
                                'age': 0,
                                'hwAddress': '00aa.fc05.b513',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.29',
                                'age': 0,
                                'hwAddress': '00af.fc9a.e49e',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.31',
                                'age': 0,
                                'hwAddress': '00ac.fc59.97f2',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.37',
                                'age': 0,
                                'hwAddress': '0001.00ff.0001',
                                'interface': 'Vlan1, not learned'},
                               {'address': '10.220.88.38',
                                'age': 0,
                                'hwAddress': '0002.00ff.0001',
                                'interface': 'Vlan1, not learned'}],
             'notLearnedEntries': 6,
             'staticEntries': 0,
             'totalEntries': 7}}]

"""
# Unpack arp table from json data
arp_table = arp_output[0]["result"]["ipV4Neighbors"]

# Print ARP entries
for arp_entry in arp_table:
    ip = arp_entry.get("address")
    mac = arp_entry.get("hwAddress")
    print(f"{ip} is bound to {mac}")