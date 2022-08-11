#!/usr/bin/env python
"""

5a. Connect to the srx2 device. Using an RPC call, gather and pretty-print the "show version" information.
Recall that you can retrieve RPC method name by running "show version | display xml rpc" argument.
Also don't forget to convert the hyphens to underscores. Your output should match the following:

<software-information>
<host-name>srx2</host-name>
<product-model>srx110h2-va</product-model>
<product-name>srx110h2-va</product-name>
<jsr/>
<package-information>
<name>junos</name>
<comment>JUNOS Software Release [12.1X46-D35.1]</comment>
</package-information>
</software-information>


5b. Using a direct RPC call, gather the output of "show interfaces terse". Print the output to standard out.

5c. Modify the previous task to capture "show interface terse", but this time only for "fe-0/0/7".
Print the output to standard out. Use normalize=True in the RPC method call to make the output more readable.
You will also need to add pretty_print=True to the etree.tostring() call.
Consequently, your code should be similar to the following:

xml_out = dev.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
"""
from jnpr.junos import Device
from lxml import etree
from getpass import getpass
from pprint import pprint
from jnpr_devices import srx2

srx2_device = Device(**srx2)
srx2_device.open()

# show version | display xml rpc
# <get-software-information>
xml_show_version = srx2_device.rpc.get_software_information()
xml_show_version = etree.tostring(xml_show_version, encoding="unicode")
pprint(xml_show_version)



# show interfaces terse | display xml rpc
# <get-interface-information>
xml_interface_info = srx2_device.rpc.get_interface_information(terse=True)
xml_interface_info = etree.tostring(xml_interface_info, encoding="unicode")
pprint(xml_interface_info)