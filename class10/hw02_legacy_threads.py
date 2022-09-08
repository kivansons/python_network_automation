#!/usr/bin/env python
"""
Create a new file named my_functions.py.
Move your function from exercise1 to this file.
Name this function "ssh_command". Reuse functions from this file for the rest of the exercises.
Complete the same task as Exercise 1b except this time use "legacy" threads to create a solution.
Launch a separate thread for each device's SSH connection. Print the time required to complete the task for all of the devices. 
Move all of the device specific output printing to the called function (i.e. to the child thread). 
"""
from time import time
from my_devices import network_devices
from my_functions import ssh_command
import threading

def main():
    time_start = time()

    # Construct threads to 'show version' for each device in network_devices
    for device in network_devices:
        show_version_thread = threading.Thread(target=ssh_command, args=(device, "show version"))
        show_version_thread.start()

    main_thread = threading.currentThread()
    for thread in threading.enumerate():
        if thread != main_thread:
            print(thread)
            thread.join()
    
    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()