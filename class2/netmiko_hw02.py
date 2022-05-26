#!/usr/bin/env python
"""
Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2.
Execute 'show lldp neighbors detail' and print the returned output to standard output.
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8.
Print the output of this command to standard output.
Use the Python datetime library to record the execution time of both of these commands. 
Print these execution times to standard output.
"""
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

nxos2 = {
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": getpass(prompt="nxos2 Password: "),
    "device_type": "cisco_nxos",
    "global_delay_factor": 2,
}
show_lldp_command = "show lldp neighbors detail"

# Connect to nxos2 and print prompt
net_connect = ConnectHandler(**nxos2)
print(net_connect.find_prompt())

# Run show lldp on nxos2 with global_delay_factor=2 and time execution"
start_time = datetime.now()
output = net_connect.send_command(show_lldp_command)
end_time = datetime.now()
elapsed_time = end_time - start_time
print(output)
print(f"Show lldp command with global_delay_factor=2 took {elapsed_time} to execute")

# Run show lldp on nxos2 with additional delay_factor=8 and time execution"
start_time = datetime.now()
output = net_connect.send_command(show_lldp_command, delay_factor=8)
end_time = datetime.now()
elapsed_time = end_time - start_time
print(output)
print(f"Show lldp command with delay_factor=8 took {elapsed_time} to execute")
