# Code-Injector

## About and Description
As the name says using this script we are going to inject some extra code while capturing and sending the modified packets to the user

First things first, all the data inside the packets are generally encrypted by default due to the parameter in the request packet called accept encoding along with the encoding type it can decode the file data

So while sending the requests to the server we delete the encoding part in the packet header and send it to the server

now after receiving the packet, we check for the content length mentioned in the packet header this is attached by the server itself, and if we inject our code then this value changes

and ones this values changes and but still we send the non modified value then browser stops loading the packet information once the loaded length is more than the sent value

So we modify the content length value too and the inject our code and then send the response packet to the user


# Usage

1.  Clone the repository or download the files
2.  cd into folder
3.  run the command _pip install -r requirements.txt_
4.  python arp_spoof_detector.py -p \<path of the js file> -l \<true/false>


-p(--path) argument is to capture the path of the file that has code that need to be injected in the packet

-l(--local) argument is to know whether you want to run this script on local machine or any remote computer

## Modules used in this program and links to documentation
- [os](https://docs.python.org/3/library/os.html)
- [re](https://docs.python.org/3/library/re.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [scapy](https://scapy.readthedocs.io/en/latest/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [NetfilterQueue](https://pypi.org/project/NetfilterQueue/)
