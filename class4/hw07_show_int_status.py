#!/usr/bin/env python
""" 
Using your TextFSM template and the 'show interface status' data from exercise2, 
create a Python program that uses TextFSM to parse this data.
In this Python program, read the show interface status data from a file and process it using the TextFSM template.
From this parsed-output, create a list of dictionaries. The program output should look as follows:

$ python ex7_show_int_status.py

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
"""
import textfsm
from pprint import pprint

# Open TextFSM template and read in text data to be parsed
template_file = "./hw02_show_int_status_expanded.fsm"
template = open(template_file)
with open("hw02_show_int_status.txt") as f:
    raw_text_data = f.read()

# Load template file then parse data. Finnaly close template file
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

# Build list of dicts from parsed data and headers
data_list = []
temp_dict = {}
for row in data:
    for key, value in zip(re_table.header, row):
        temp_dict[key] = value
    data_list.append(temp_dict.copy())
    temp_dict.clear()

pprint(data_list)