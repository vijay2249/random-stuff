# ARP-Spoof

Before executing this program make sure that you download the scapy module 
Download scapy module from [here](https://scapy.readthedocs.io/en/latest/installation.html#installing-scapy-v2-x)

or 

run the command pip install -r requirements.txt

# usage

python3 {fileName.py} -t {targetIP} -g {gatewayIP}

or

python3 {filename.py} --target {targetIP} --gateway {gatewayIP}

# Modules used in this program and more information about them

[re](https://docs.python.org/3/library/re.html)

[time](https://docs.python.org/3/library/time.html)

[argparse](https://docs.python.org/3/library/argparse.html)

[subprocess](https://docs.python.org/3/library/subprocess.html)

[SCAPY](https://scapy.readthedocs.io/en/latest)

# Note: If the gateway parameter is not mentioned, then the program tried to get the default gateway of the network you are in..
