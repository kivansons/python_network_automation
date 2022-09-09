#!/usr/bin/env python
"""
Create a new program that completes the same task as Exercise 3b except using multiple processes (i.e. a 'ProcessPoolExecutor').
"""
from time import time
from my_devices import network_devices
from my_functions import ssh_command2
from concurrent.futures import ProcessPoolExecutor, as_completed

def main():
    time_start = time()
    MAX_PROCESSES = 8
    
    pool = ProcessPoolExecutor(MAX_PROCESSES)
    
    # Create a Process for each "show version" netmiko ssh connection and add to process list
    process_list = []
    for device in network_devices:
        process = pool.submit(ssh_command2, device, "show version")
        process_list.append(process)

    # Print process results as they finish 
    for process in as_completed(process_list):
        print("Show version result:")
        print(process.result())

    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()