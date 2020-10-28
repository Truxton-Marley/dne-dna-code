#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
import pprint


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_text = file.read()

    # print("JSON text is a", type(json_text))
    # print(json_text)

    json_data = json.loads(json_text)
    # print("JSON data is a", type(json_data))
    print("\nJSON file as a python dict:\n")
    pprint.pprint(json_data)

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

    print("The following IPv4 interfaces are configured:\n")

    for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
        print(interface["name"] + ":")
        print("  IP:", interface["ietf-ip:ipv4"]["address"][0]["ip"])
        print("  SM:", interface["ietf-ip:ipv4"]["address"][0]["netmask"], "\n")