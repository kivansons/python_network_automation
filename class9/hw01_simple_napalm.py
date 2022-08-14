
"""
1a. Create a Python file named "my_devices.py" 
that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device.
Use getpass() for the password handling. 
This Python module should be used to store the device connection information for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information
from the my_devices.py file and creates a NAPALM connection object. 
This function should open the NAPALM connection to the device and should return the NAPALM connection object.

1c. Using your "my_devices.py" file and your NAPALM connection function,
create a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects,
print out the device's connection object itself.
Additionally, pretty print the facts for each device and also print out the device's NAPALM platform type (ios, eos, et cetera).
"""
from napalm import get_network_driver
from pprint import pprint
from my_devices import net_devices

def build_napalm_connection(device: dict):
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device_connection = driver(**device)
    return device_connection.open()

def main():
    napalm_connections = []
    for device in net_devices:
        napalm_connections.append(build_napalm_connection(device))

    for connection in napalm_connections:
        pprint(connection)

if __name__ == "__main__":
    main()
