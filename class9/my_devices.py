"""
1a. Create a Python file named "my_devices.py"
that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device.
Use getpass() for the password handling.
This Python module should be used to store the device connection information for all of the exercises in this lesson.
"""
from getpass import getpass

net_devices = {
    "cisco3": {
        "hostname": "cisco3.lasthop.io",
        "device_type": "ios",
        "username": "pyclass",
        "password": getpass(),
        "optional_args": {},
    },
    "arista1": {
        "hostname": "arista1.lasthop.io",
        "device_type": "eos",
        "username": "pyclass",
        "password": getpass(),
        "optional_args": {},
    },
}
