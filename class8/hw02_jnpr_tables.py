#!/usr/bin/env python
"""
2b. Create a Python program that creates a PyEZ Device connection to "srx2" (using the previously created Python module).
Using this PyEZ connection and the RouteTable and ArpTable views retrieve the routing table and the arp table for srx2.

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working.
    You can use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object, the routing table,
     and the ARP table and then prints out the: hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that all of the four functions could be reused in other class8 exercises.
"""
from jnpr_devices import srx2
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable
from pprint import pprint

def check_connected(jnpr_device: Device) -> None:
    print("\n\n")
    if jnpr_device.connected:
        print(f"Device {jnpr_device.hostname} is connected!")
    else:
        print(f"Device {jnpr_device.hostname} failed to connect: Quitting script")
        quit()
    return

def gather_routes(jnpr_device: Device) -> RouteTable:
    routes = RouteTable(jnpr_device)
    routes.get()
    return routes

if __name__ == "__main__":
    srx2_device = Device(**srx2)
    srx2_device.open()
    check_connected(srx2_device)

    srx2_routes = gather_routes(srx2_device)
    pprint(srx2_routes)