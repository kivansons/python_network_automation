#!/usr/bin/env python
"""
Using a context manager, the ProcessPoolExecutor, and the map() method,
create a solution that executes "show ip arp" on all of the devices defined in my_devices.py. 
Note, the Juniper device will require "show arp" instead of "show ip arp" so your solution will have to properly account for this.
"""
from time import time
from my_devices import network_devices
from my_functions import ssh_command2,generate_show_arp_cmd
from concurrent.futures import ProcessPoolExecutor, as_completed

def main():
    time_start = time()
    MAX_PROCESSES = 8

    arp_cmds = []
    for device in network_devices:
        arp_cmds.append(generate_show_arp_cmd(device))

    payloads = zip(network_devices,arp_cmds)

    # Create a Process for each "show version" netmiko ssh connection and add to process list
    with ProcessPoolExecutor(MAX_PROCESSES) as pool:
        results = pool.map(ssh_command2, *payloads)
        
        # Print process results as they finish 
        for result in results:
            print("Show arp result:")
            print(result)

    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()