from netmiko import ConnectHandler

def ssh_command(device: dict, command: str) -> None:
    """Create an SSH connection then execute show command. Prints results of command"""
    conn = ConnectHandler(**device)
    output = conn.send_command(command)
    conn.disconnect()
    print("\n")
    print(f'Output of {device["host"]} "show version" command')
    print("\/" * 40)
    print(output)
    print("/\\" * 40)
    return None

def ssh_command2(device: dict, command: str) -> str:
    """Create an SSH connection then execute show command. Returns results of command"""
    conn = ConnectHandler(**device)
    output = conn.send_command(command)
    conn.disconnect()
    return output

def generate_show_arp_cmd(device: dict) -> str:
    """Accepts a Netmiko device dict and returns the show ip arp commmand for device type"""
    if device["device_type"] == "juniper_junos":
        arp_cmd = "show arp"
    elif device["device_type"] == "arista_eos":
        arp_cmd = "show ip arp"
    elif device["device_type"] == "cisco_ios":
        arp_cmd = "show ip arp"
    else:
        raise Exception
    return arp_cmd