#!/usr/bin/env python
"""
3a. Using your existing functions and the my_devices.py file, create a NAPALM connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and `cisco3.lasthop.io-loopbacks`. 
In each of these files, create two new loopback interfaces with a description. 
Your files should be similar to the following:

interface loopback100
  description loopback100
!
interface loopback101
  description loopback101


For both cisco3 and arista1, use the load_merge_candidate() method to stage the candidate configuration.
In other words, use load_merge_candidate() and your loopback configuration file to stage a configuration change.
Use the NAPALM compare_config() method to print out the pending differences 
(i.e. the differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again (after the commit_config).
"""
from my_devices import net_devices
from my_functions import build_napalm_connection

def main():
    
    # Create napalm connections
    net_connections = []
    for device in net_devices.values():
        net_connect = build_napalm_connection(device)
        net_connections.append(net_connect)

    for connection in net_connections:
        print("\n")
        print("-" * 80)
        print(f"Loading config candidate for {connection.hostname}")
        try:
            connection.load_merge_candidate(filename=f"{connection.hostname}-loopbacks")
        except:
            print(f"Failed to merge config for {connection.hostname} skipping..")
            continue
        diff = connection.compare_config()
        print("Config diff is:")
        print("-" * 80)
        print(diff)



    return None

if __name__ == "__main__":
    main()