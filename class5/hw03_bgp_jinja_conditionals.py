"""
Generate the following configuration output from an external Jinja2 template:

​vrf definition blue
 rd 100:1
 !
 address-family ipv4
  route-target export 100:1
  route-target import 100:1
 exit-address-family
 !
 address-family ipv6
  route-target export 100:1
  route-target import 100:1
 exit-address-family


Both the IPv4 and the IPv6 address families should be controlled by Jinja2 conditionals
(in other words, the entire 'address-family ipv4' section and the entire 'address-family ipv6' sections
can be dropped from the generated output depending on the value of two variables that you pass into your template
for example, the 'ipv4_enabled' and the 'ipv6_enabled' variables).
Additionally, both the vrf_name and the rd_number should be variables in the template.
Make sure that you control the whitespace in your output such that the configuration looks visually correct.
"""
from pprint import pprint
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

# Set strict undefined var checking
env = Environment(undefined=StrictUndefined)
# Load jinja2 templates from local dir
env.loader = FileSystemLoader(".")

vrf_ipv4 = {
    "vrf_name": "blue",
    "ipv4_enabled": True,
    "ipv6_enabled": False,
    "rd_number": "100:1"
}
vrf_ipv6 = {
    "vrf_name": "blue",
    "ipv4_enabled": False,
    "ipv6_enabled": True,
    "rd_number": "100:1"
}
vrf_ipv4_ipv6 = {
    "vrf_name": "blue",
    "ipv4_enabled": True,
    "ipv6_enabled": True,
    "rd_number": "100:1"
}

template_file = "hw03_bgp_jinja_conditionals.j2"
template = env.get_template(template_file)
vrf_ipv4_output = template.render(**vrf_ipv4)
vrf_ipv6_output = template.render(**vrf_ipv6)
vrf_ipv4_ipv6_output = template.render(**vrf_ipv4_ipv6)

print("IPv4 VRF config:")
print(vrf_ipv4_output)

print("\nIPv6 VRF config:")
print(vrf_ipv6_output)

print("\nIPv4 & IPv6 VRF config:")
print(vrf_ipv4_ipv6_output)