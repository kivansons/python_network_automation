#!/usr/bin/env python
"""
4a. Using the previously created jnpr_devices.py file, open a connection to srx2 and gather the current routing table information.

4b. Using PyEZ stage a configuration from a file. The file should be "conf" notation.
This configuration should add two static host routes (routed to discard).
These routes should be from the RFC documentation range of 203.0.113.0/24 (picking any /32 in that range should be fine).
Use "merge=True" for this configuration. For example:

routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}


4c. Reusing your gather_routes() function from exercise2, retrieve the routing table before and after you configuration change. Print out the differences in the routing table (before and after the change). 
o simplify the problem, you can assume that the only change will be *additional* routes added by your script.

4d. Using PyEZ delete the static routes that you just added. You can use either load() and set operations or load() plus a configuration file to accomplish this.

"""
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2
from pprint import pprint
from hw02_jnpr_tables import gather_routes


def load_conf_from_file(filepath: str, device: Device, merge: bool = True) -> None:
    """Load config from passed filepath and commit to passed device"""
    config = Config(device)
    config.lock()
    config.load(path=filepath, format="text", merge=merge)
    if config.diff() is not None:
        config.commit()
    config.unlock()
    
    return None


def remove_routes(device: Device) -> None:
    """Remove routes added for exercise from passed device"""
    config = Config(device)
    config.lock()
    config.load(
        "delete routing-options static route 203.0.113.42/32", format="set", merge=True
    )
    config.load(
        "delete routing-options static route 203.0.113.223/32", format="set", merge=True
    )
    print("\n")
    print("Removing example routes")
    if config.diff() is not None:
        config.commit
    config.unlock()
    
    return None
    
    # Build connection to device
srx2_device = Device(**srx2)
srx2_device.open()

# Print out routes
srx2_initial_routes = gather_routes(srx2_device)
print(f"Printing routes from {srx2_device.hostname}")
print("-" * 80)
pprint(srx2_initial_routes.items())

# Send new routes
ROUTES_CONFIG_PATH = "hw04_routes.txt"
print(f"Sending routes config to {srx2_device.hostname}")
load_conf_from_file(ROUTES_CONFIG_PATH, srx2_device)

# Print out routes
srx2_new_routes = gather_routes(srx2_device)
print(f"Printing routes from {srx2_device.hostname}")
print("-" * 80)
pprint(srx2_new_routes.items())

# Clean up routes
remove_routes(srx2_device)