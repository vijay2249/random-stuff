# DNS-Spoof

# NOTE: <br>
Before executing this program make sure that you are the man in the middle between your target system and router in your local network
More about it [here](https://github.com/NeverStopLearningNSL/ARP-Spoof)

# Download the required third party python modules from here

download this git repo and cd into the folder and run the command from the terminal **"pip install -r requirements.txt"**

or

[netfilterqueue](https://pypi.org/project/NetfilterQueue/)

[scapy](https://scapy.readthedocs.io/en/latest/installation.html#installing-scapy-v2-x)

## Usage

    python dns_spoofing.py -l <true/false> --site <siteYouAreSpoofing> -i <IP of serving site> -qn <queue_num>

  Arguemnts     | Description
:-------------: | -------------
local(-l)        | Whether you are running this program on your system or other system _required_
queue_num(-qn)   | to capture and store the packets by iptables, this requires the queue-number to capture and store these packets (default value is zero)
site(-s)         | the site you are trying to spoof (ex: google.com or github.com or cowin.gov.in) _required_
ip(-i)           | the ip address of the site you want to serve to the user (ex: 10.0.2.4 or 8.8.8.8 etc..) _required_


# Modules used in this program and links to detailed information about them

- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [netfilterqueue](https://pypi.org/project/NetfilterQueue/)
- [scapy](https://scapy.readthedocs.io/en/latest/index.html)

# little more information about the concepts used in this program
- [DNS Requests](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [iptables](https://linux.die.net/man/8/iptables)


## disclaimer

This script do not support windows systems...
