#!/usr/bin/env python
"""
 Create a new function that is a duplicate of your "ssh_command" function.
 Name this function "ssh_command2". This function should eliminate all printing to standard output and
 should instead return the show command output.
 Note, in general, it is problematic to print in the child thread as you can get into race conditions between the threads.
 Using the "ThreadPoolExecutor" in Concurrent Futures execute "show version" on each of the devices defined in my_devices.py.
 Use the 'wait' method to ensure all of the futures have completed. 
 Concurrent futures should be executing the ssh_command2 function in the child threads. 
 Print the total execution time required to accomplish this task.
"""
from time import time
from my_devices import network_devices
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor, wait

def main():
    time_start = time()
    MAX_THREADS = 10
    
    pool = ThreadPoolExecutor(MAX_THREADS)
    
    # Create a thread for each "show version" netmiko ssh connection and add to thread list
    thread_list = []
    for device in network_devices:
        thread = pool.submit(ssh_command2, (device, "show version"))
        thread_list.append(thread)

    # wait for all threads to finish 
    wait(thread_list)

    for thread in thread_list:
        print("Show version result:")
        print(thread.result())

    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()