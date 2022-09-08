#!/usr/bin/env python
"""
1b. Create a Python script that executes "show version" on each of the network devices defined in my_devices.py.
This script should execute serially i.e. one SSH connection after the other.
Record the total execution time for the script.
Print the "show version" output and the total execution time to standard output.
As part of this exercise, you should create a function that both establishes
a Netmiko connection and that executes a single show command that you pass in as argument.
This function's arguments should be the Netmiko device dictionary and the "show-command" argument. 
The function should return the result from the show command.
"""
from netmiko import ConnectHandler
from my_devices import network_devices
from time import time

def ssh_command(device: dict, command: str) -> str:
    """Create an SSH connection then execute show command. Returns results of command"""
    conn = ConnectHandler(**device)
    output = conn.send_command(command)
    conn.disconnect()
    return output

def main():
    time_start = time()
    for device in network_devices:
        output = ssh_command(device, "show version")
        print("\n")
        print("-" * 80)
        print(output)
        print("-" * 80)
    print("\n\n")
    print("*" * 80)
    time_end = time()
    time_taken = time_end - time_start
    print(f"Execution completed in {time_taken} seconds")

if __name__ == "__main__":
    main()