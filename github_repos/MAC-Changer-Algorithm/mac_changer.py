# !/usr/bin/env python

import subprocess
import re
import argparse

#first we need the arguments that represent the interface for which we have to change mac address and new mac address

def get_arguments():
    p = argparse.ArgumentParser()
    #new argument -i or --interface for taking the interface as the input for this argument
    p.add_argument("-i", "--interface", dest="Interface", help="Interface for which need to change mac address")
    #new argument -m or --mac for taking new mac address as the input
    p.add_argument("-m", "--mac", dest="new_MAC_address", help="enter new mac address")
    options_entered = p.parse_args()
    #we also need to check weather user actually inputted all the required inputs
    #error handling
    if not options_entered.Interface:
        p.error("[-] please specify an interface with argument -i or --interface")
    if not options_entered.new_MAC_address:
        p.error("[-] Please specify the correct mac address by the argument -m or --mac")
    #if everything is fine then we return the options that user entered
    return options_entered


#defining a new function that changes the mac address for us
def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address, for the {interface} to {new_mac}")
    #now its time to run actual kali linux commands using python script
    #this is done by using the subprocess module
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    #and now we are done


#new function to get the current mac address of the given interface
#this takes interface as parameter
def get_current_mac(interface):
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
    mac_results = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_results:
        return mac_results.group(0)
    else:
        print(f"[-] Cannot read MAC address for the {interface}")


#capturing these values user entered
option = get_arguments()
current_mac = str(get_current_mac(option.Interface))
print(f"[+] Current MAC address for {option.Interface} is {current_mac}")
#time to change mac address
change_mac(option.Interface, option.new_MAC_address)
current_mac = str(get_current_mac(option.Interface))

#now lets check weather the program actually got executed correct or not
if current_mac == option.new_MAC_address:
    print(f"[+] MAC address for {option.Interface} have been changed successfully..")
else:
    print(f"[-] Mac address did not get changed for {option.Interface}")

#end of our program now lets try to execute this and see the result
