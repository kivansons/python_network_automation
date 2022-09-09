#!/usr/bin/env python
"""
Using a context manager and a 'ProcessPoolExecutor', complete the same task as Exercise 4.

"""
from time import time
from my_devices import network_devices
from my_functions import ssh_command2
from concurrent.futures import ProcessPoolExecutor, as_completed

def main():
    time_start = time()
    MAX_PROCESSES = 8
    
    
    
    # Create a Process for each "show version" netmiko ssh connection and add to process list
    with ProcessPoolExecutor(MAX_PROCESSES) as pool:
        for device in network_devices:
            process = pool.submit(ssh_command2, device, "show version")

            # Print process results as they finish 
        for process in as_completed(pool):
            print("Show version result:")
            print(process.result())

    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()