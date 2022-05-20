"""
1. In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices. 
You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email
 or alternatively in the ~/.netmiko.yml file.
  Simply print the router prompt back from this device to verify you are connecting to the device properly.
"""
from netmiko import ConnectHandler
from getpass import getpass

nx_password = getpass()
nx01 = {
  "host": "nxos01.lasthop.io",
  "username": "pyclass",
  "password": nx_password,
  "devicetype": "cisco_nxos",
}

net_connect = ConnectHandler(**nx01)
print(net_connect.find_prompt())

