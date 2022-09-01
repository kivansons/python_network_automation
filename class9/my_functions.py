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
import time

def build_napalm_connection(device: dict):
    """Opens a napalm connection from passed device and returns connection object"""

    # Copy passed mutable object so orginal is not modified
    device = device.copy()

    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device_connection = driver(**device)
    device_connection.open()
    return device_connection

def create_backup(napalm_connection):
    """Accepts an open napalm connection and creates a backup file of the running config"""
    # Get device hostname for filename
    filename = napalm_connection.get_facts()
    filename = filename["hostname"]
    timestr = time.strftime("%Y%m%d_%H%M%S")
    filename = f"{filename}_{timestr}"

    # Get device running configuration
    backup = napalm_connection.get_config()
    backup = backup["running"]

    # Write config to file
    with open(f"{filename}.backup", "w") as backup_file:
        backup_file.write(backup)

    return None

def create_checkpoint(napalm_connection):
    """Create a config checkpoint and write to disk"""
    filename = f"{napalm_connection.hostname}-checkpoint.txt"
    checkpoint_conf = napalm_connection._get_checkpoint_file()

    with open(filename, "w") as f:
        f.write(checkpoint_conf)
    
    return None