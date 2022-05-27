#!/usr/bin/env python
""" Use Netmiko and the send_config_set() method to configure the following on the Cisco3 router.

ip name-server 1.1.1.1
ip name-server 1.0.0.1
ip domain-lookup

Experiment with fast_cli=True to see how long the script takes to execute (with and without this option enabled).

Verify DNS lookups on the router are now working by executing 'ping google.com'.
Verify from this that you receive a ping response back.
"""
from tracemalloc import start
from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(prompt="Cisco3 Password: "),
    "device_type": "cisco_ios",
}
cisco3_fast = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": getpass(prompt="Cisco3 Password: "),
    "device_type": "cisco_ios",
    "fast-cli": True,
}

dns_config = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
]

net_connect = ConnectHandler(**cisco3)
net_connect.find_prompt()

# send_config_set fast-cli=False
output = ""
start_time = datetime.now()
output = net_connect.send_config_set(dns_config)
end_time = datetime.now()
net_connect.disconnect()
elapsed_time = end_time - start_time
print(output)
print(f"send_config_set fast-cli=False took {elapsed_time} to execute")

# send_config_set fast-cli=True
net_connect_fast = ConnectHandler(**cisco3_fast)
output = ""
start_time = datetime.now()
output = net_connect_fast.send_config_set(dns_config)
end_time = datetime.now()
elapsed_time_fast = end_time - start_time
elapsed_time_delta = elapsed_time - elapsed_time_fast
print(output)
print(
    f"send_config_set fast-cli=False took {elapsed_time_fast} to execute {elapsed_time_delta} faster"
)
