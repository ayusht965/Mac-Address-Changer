#!/usr/bin/env python

import subprocess
import optparse
import re

def change_mac(Interface, new_mac):

    subprocess.call(["ifconfig", Interface, "down"])
    subprocess.call(["ifconfig", Interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", Interface, "up"])

def get_parsed_value():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for which the MAC is to be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        print("Please enter an interface,for more info type help ")
    elif not options.new_mac:
        print("Please enter a MAC address, for more info type help")
    return options

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Not able to find MAC address")


options = get_parsed_value()
current_mac = get_current_mac(options.interface)
if current_mac:
    print("Current MAC = "+ str(current_mac))

    change_mac(options.interface, options.new_mac)

    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] The MAC address changed to "+ options.new_mac)
    else:
        print("[-]The MAC address did not changed ")




