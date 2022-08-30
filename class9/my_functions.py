#!/usr/bin/env python

"""
2a. Create a new file named "my_functions.py" that will store a set of reusable functions.
Move the "open_napalm_connection" function from exercise1 into this Python file.
Import the network devices once again from my_devices.py and create a list of connection objects
(once again with connections to both cisco3 and arista1).

2d. Create another function in "my_functions.py".
This function should be named "create_backup" and should accept a NAPALM connection object as an argument.
Using the NAPALM get_config() method, the function should retrieve and write the current running configuration to a file.
The filename should be unique for each device. 
In other words, "cisco3" and "arista1" should each have a separate file that stores their running configuration. 
Note, get_config() returns a dictionary where the running-config is referenced using the "running" key.
Call this function as part of your main exercise2
and ensure that the configurations from both cisco3 and arista1 are backed up properly.

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

def create_backup(device_connection):
    """Accepts an open napalm connection and creates a backup file"""
    backup = device_connection.get_config()
    print(backup)
    return backup