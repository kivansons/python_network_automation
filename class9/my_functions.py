#!/usr/bin/env python

"""
2a. Create a new file named "my_functions.py" that will store a set of reusable functions.
Move the "open_napalm_connection" function from exercise1 into this Python file.
Import the network devices once again from my_devices.py and create a list of connection objects
(once again with connections to both cisco3 and arista1).
"""
from napalm import get_network_driver

def build_napalm_connection(device: dict):
    """Opens a napalm connection from passed device and returns connection object"""

    # Copy passed mutable object so orginal is not modified
    device = device.copy()


    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device_connection = driver(**device)
    device_connection.open()
    return device_connection