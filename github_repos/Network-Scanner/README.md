# Network-Scanner

Before executing this program you need to install the [scapy](https://scapy.readthedocs.io/en/latest/) module

or

download this folder then cd into the folder and run the command "pip install -r requirements.txt"

# Usage
python3 {fileName.py} -s {source IP address}
source IP address -> the local network router IP address or t can be specific IP address
Lets say IP address be 10.0.2.1 (for the router and you are in this network)
To scan the whole network the IP argument be : python3 {fileName.py} -s 10.0.2.1/24
To scan for a particular IP address like for 50: python3 {fileName.py} -s 10.0.2.50
# This IP address mentioned is just an example


### NOTE: If no target IP mentioned is mentioned then this program takes the default gateway of your local network then scans the whole network
for this you just need to run the code by
"python3 {fileName.py}"


# Modules used and more information about them..
[re](https://docs.python.org/3/library/re.html)

[subprocess](https://docs.python.org/3/library/subprocess.html)

[os](https://docs.python.org/3/library/os.html)

[optparse](https://docs.python.org/3/library/optparse.html)

[argparse](https://docs.python.org/3/library/argparse.html)

[scapy](https://scapy.readthedocs.io/en/latest/)
