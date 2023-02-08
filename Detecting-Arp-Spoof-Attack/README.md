# Detecting-Arp-Spoof-Attack
As name says, using this python script we can detect arp spoof attacks on our system

In this script we use whats neglected in "address resolution protocol" that is verifying the packets actual information or the originality of the packet

While attacker is trying to be man in the middle attacker tries to send the packets of information that says that router IP is here at my mac address (attackers mac address)

So now with the packets we are received, we try to get the original mac address of the IP address that is mentioned in the packet

If the return mac address from our function and the mac address that is mentioned in the packet are matched then the packet is not modified and it is legit packet

Else if the return mac address from our function and the mac address that is mentioned in the packet are not matched then the packet is not real one and is a modified packet

So everytime we get any packets from outside, we run this program to compare the mac address of the IP address from which the packets are coming from and original mac address of the IP address mentioned in the packet



## Usage

1.  Clone the repository or download the files
2.  cd into folder
3.  run the command _pip install -r requirements.txt_
4.  python arp_spoof_detector.py -i \<interface>

interface is the network interface that you are connected to like in linux "eth0" or "eth1" etc..

## Modules used in this program and links to documentation
- [sys](https://docs.python.org/3/library/sys.html)
- [scapy](https://scapy.readthedocs.io/en/latest/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [argparse](https://docs.python.org/3/library/argparse.html)



## The only drawback of this login
_As you have privilage to change your systems mac address to someone else's mac address_

So does the attacker can do the same thing to change his/her mac address to routers mac address

In such cases the response from the from findind the mac address using arp broadcasting packets and the mac address mentioned in the receiving packets are same and hence will be no change of finding the error as per logic we used to find the creepy response packets that we get
