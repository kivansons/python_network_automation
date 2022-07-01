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

pprint(arp_output)
