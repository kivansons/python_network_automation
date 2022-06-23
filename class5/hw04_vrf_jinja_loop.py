"""Expand on exercise3 except use a for-loop to configure five VRFs.
Each VRF should have a unique name and a unique route distinguisher.
Each VRF should once again have the IPv4 and the IPv6 address families 
controlled by a conditional-variable passed into the template.

Note, you will want to pass in a list or dictionary of VRFs
that you loop over in your Jinja2 template.
"""
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set strict undefined var checking
env = Environment(undefined=StrictUndefined)
# Look for jinja2 templates in local dir
env.loader = FileSystemLoader(".")

vrf_list = [
    {
        "vrf_name": "red",
        "ipv4_enabled": True,
        "ipv6_enabled": False,
        "rd_number": "100:1",
    },
    {
        "vrf_name": "green",
        "ipv4_enabled": False,
        "ipv6_enabled": True,
        "rd_number": "101:1",
    },
    {
        "vrf_name": "blue",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
        "rd_number": "102:1",
    },
    {
        "vrf_name": "cyan",
        "ipv4_enabled": True,
        "ipv6_enabled": False,
        "rd_number": "103:1",
    },
    {
        "vrf_name": "yellow",
        "ipv4_enabled": False,
        "ipv6_enabled": True,
        "rd_number": "104:1",
    },
    {
        "vrf_name": "magenta",
        "ipv4_enabled": True,
        "ipv6_enabled": True,
        "rd_number": "105:1",
    },
]
jinja_vars = {"vrf_list": vrf_list}
template_file = "hw04_vrf_jinja_loop.j2"
template = env.get_template(template_file)
vrf_output = template.render(**jinja_vars)

print(vrf_output)