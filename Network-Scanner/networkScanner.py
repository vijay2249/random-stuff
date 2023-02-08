# !/usr/bin/env python3

import re
import argparse
import subprocess
import scapy.all as scapy


def get_gateway():
    result = subprocess.check_output(["ip", "r"])
    gateway_result = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", str(result))
    subnet = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}", str(result))
    return (gateway_result.group(0),subnet.group(0))

# argparse is the module that is new from python 3 and the only difference from optparse is that it returns only options
def get_argumentsby_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--scan", dest="IP", help="IP address of local network to scan")
    options = parser.parse_args()
    if not options.IP:
        ip = get_gateway()[1]
        print(f"[-] No target IP mentioned, using default gateway network {get_gateway()[0]}")
        print(f"[-] Scanning the whole subnet of {ip}")
        options.IP = ip + ".1/24"
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_packet = broadcast/arp_request
    answeredList = scapy.srp(arp_request_packet, timeout=1, verbose=False)[0]
    client_list = []
    for element in answeredList:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def displayClients(clients):
    print("IP\t\t\tMAC Address\n----------------------------------------------")
    for client in clients:
        print(client["ip"] + "\t\t" + client["mac"])

option = get_argumentsby_argparse()
clients_list = scan(option.IP)
displayClients(clients_list)
