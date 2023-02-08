# File_Interceptor
<p align='center'>
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/DUMMY-the-BOT/File-Interceptor?style=flat-square">
    <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/DUMMY-the-BOT/File-Interceptor">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/DUMMY-the-BOT/File-Interceptor?style=flat-square">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/DUMMY-the-BOT/File-Interceptor">
</p>
  
## About

A simple python script to replace the downloads made by user

Before using this script be sure that you run the [arp spoof](https://github.com/DUMMY-the-BOT/ARP-Spoof) attack on the user

## ___Description___

### usage

    clone the repository
    cd into repository
    pip install -r requirements.txt
    python file_interceptor.py --local false -p \<filePath> -qn \<number> -f \<fileExtension>

  Arguemnts     | Description
:-------------: | -------------
local(l)        | Whether you are running this program on your system or other system
path(-p)        | Path of replaced file you need to place in packet
queue-num(qn)   | to capture and store the packets by iptables, this requires the queue-number to capture and store these packets (default value is zero)
file(-f)        | the type of file extension that you are trying to replace with in the packets


If these required areguments are not mentioned then the backup class that contains the functions to ask for the required input from user to use the tool

## _Modules Used_

- [os](https://docs.python.org/3/library/os.html)
- [sys](https://docs.python.org/3/library/sys.html)
- [scapy](https://scapy.readthedocs.io/en/latest/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- [netfilterqueue](https://pypi.org/project/NetfilterQueue/)


Script only works with linux systems and do not accept with windows operating..


More information about the concepts used in the script

- [iptables](https://netfilter.org/documentation/)
- To know the operating system use sys module (sys.platform)

## By default linux do not allow packets flow through your system as a security feature, to accept the packets flow we modify the settings in the system(taken care in the script at the line 84)

If you need to do this manually the open the terminal and run the command

    echo 1 > /proc/sys/net/ipv4/ip_forward

By default script flushes any iptables that are created before that are not deleted, and once the program is stopped from executing then it clears all the iptables that are used in the script

# _Happy Learning_
