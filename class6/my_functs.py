"""
Create a Python module named 'my_funcs.py'.
In this file create two functions: function1 should read the YAML file you created in exercise 2a 
and return the corresponding data structure; 
function2 should handle the output printing of the ARP entries (in other words, create a separate function that handles all printing to standard out of the 'show ip arp' data).
Create a new Python program based on exercise2a except the YAML file loading and the output printing is accomplished using the functions defined in my_funcs.py.
"""
import yaml

def load_devices_from_yaml(device_filepath: str) -> dict:
    """Loads devices from YAML at device_filepath. Returns a dictionary python object"""
    device_filepath = "eapi_devices.yaml"
    with open(device_filepath, "r") as f:
        device_dict = yaml.safe_load(f)
    return device_dict.copy()

def print_arp(arp_json_data: list, hostname_json_data = None) -> None:
    """Prints the output from a 'show ip arp' eapi json dict
    if the output of a 'show hostname' eapi command the host name will be included in output"""
    if hostname_json_data is not None:
        hostname = hostname_json_data[0]["result"]["hostname"]
        # Print Header
        print(f"{hostname} arp bindings")

    # Print line
    print("-" * 80)
    # Unpack arp table from json data
    arp_table = arp_json_data[0]["result"]["ipV4Neighbors"]
    # Print ARP entries
    for arp_entry in arp_table:
        ip = arp_entry.get("address")
        mac = arp_entry.get("hwAddress")
        print(f"{ip} is bound to {mac}")
