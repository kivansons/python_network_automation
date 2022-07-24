#!/usr/bin/env python
"""
1a. Create a PyEZ Device object from the jnpr.junos Device class. 
This device object should connect to "srx2.lasthop.io". 
Use getpass() to enter the device's password. Pretty print all of the device's facts. 
Additionally, retrieve and print only the "hostname" fact.
"""
from jnpr.junos import Device
from getpass import getpass
from pprint import pprint

srx2 = Device(host="srx2.lasthop.io", user="pyclass", password=getpass())
srx2.open()

print("Getting and printing device facts...")
print("-" * 80)
facts = srx2.facts
pprint(facts)
print("\n\n")
print(f"The device hostname is: {facts['hostname']}")

