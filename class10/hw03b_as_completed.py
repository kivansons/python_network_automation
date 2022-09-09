#!/usr/bin/env python
"""
Instead of waiting for all of the futures to complete, use "as_completed" to print the future results as they come available.
Reuse your "ssh_command2" function to accomplish this.
Once again use the concurrent futures "ThreadPoolExecutor" and print the "show version" results to standard output. 
Additionally, print the total execution time to standard output.
"""
from time import time
from my_devices import network_devices
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, as_completed

def main():
    time_start = time()
    MAX_THREADS = 8
    
    pool = ThreadPoolExecutor(MAX_THREADS)
    
    # Create a thread for each "show version" netmiko ssh connection and add to thread list
    thread_list = []
    for device in network_devices:
        thread = pool.submit(ssh_command2,device, "show version")
        thread_list.append(thread)

    # Print thread results as they finish 
    for thread in as_completed(thread_list):
        print("Show version result:")
        print(thread.result())

    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()