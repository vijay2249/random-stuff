MAC address and how to change it…
why do we need to change the MAC address???
	MAC address is unique for a product, which means that there are no two products having the same MAC address.
	Which brings to the next point, giving access to some of the software or information to only certain systems or computers.
	How to we decide that this computer has access to that particular data, well the unique thing about this computer is its MAC address, so if along with the request for reading or writing the data, it also send the MAC address of the computer,
	So if we are able to change the MAC address to our target host machine, we can actually see some of the important files without much of the hard work.
	it means that we are doing all our necessary tasks in the name of the target or the host machine.
Hence till they find our machine we can do our stuff as quickly and remove our system connection with it and be secure again from re-attack.

Ok for now let's start changing our MAC address…………….

Command  “ifconfig”
	This is used to display all the network interfaces connected to the computer either by virtual network or by the wireless adapter.

(don't worry about the black paint people, have to be secure[our target] so covered my IPv6 and some part of MAC address)
In this pic
	inet <number> => this number represents the IP address of that network
	ether <number> => this number represents the mac address of that system or computer.
one important thing is that 

Command: 
	ifconfig <connection_name (like above pics eth0)> down
	this command disables the mentioned network interface

remember that the options of the network interface can be changed only if that particular interface is down or currently not working.

Changing the mac address of the system:
	ifconfig <connectionName> hw ether <newMACAddress>

	conditions:
New mac address must contain 12 characters
Each two characters should be separated by colon(:)
Example MAC address: 1d:3d:fc:af:d6:78
Also note that the characters in the MAC address can be either numbers from 0-9 and letters from a-f
https://en.wikipedia.org/wiki/MAC_address
Now after changing the mac address we have to enable the network configuration to show up with the changed mac address
Command:
	ifconfig <connectionName> up
	this commands enables the network interface that we actually disabled during the starting of this process with the command “ifconfig <connectionName> down”



Changing MAC address using Python
NOTE: anywhere if i say to compile the python i mean to run the python script, python is a interpreter language which is different from cpp, c, c# which are need to be compiled before running the script
more about the difference in here
Python modules used in this program are 
	1.subprocess
	2.optparse
in this python code our target is to execute the terminal or command shell commands via python
for this python has an inbuilt module named subprocess
https://docs.python.org/3/library/subprocess.html
in this module we use call (or) run method
How it works:
	subprocess.call(“<command>”, shell=True)
Breaking the line of code:
	subprocess is a python module, this module contains call method,
	this call method takes two arguments:
command (that we execute in command prompt or terminal) as string
shell (boolean value either True (or) False)
This shell argument is to say to python that the command that i typed in string is the command that you need to execute in the terminal (if given the argument shell=True) and it automatically takes care of it.

Updates about call method:
	this call method is in Python version 2 and the link that i attached above is the latest one (Python version 3)
	the latest version of Python uses run method instead of call(we can use call also as our wish)
Example of the call method:
	suppose that i need to list out all the wireless interfaces that are connected to my computer using python, then i write and compile the code

import subprocess
subprocess.call(“iwconfig”, shell=True)
thats it these two of code in python does the job for you,
Now all you have to do is to run this python file in the terminal or whatever you are using to run the python file.

now the code in python to change the mac address goes like this
  
import subprocess
interface = input(“interface: “)
newMACaddress = input(“new mac address: “)
subprocess.call("ifconfig {} down".format(interface), shell=True)
subprocess.call("ifconfig {} hw ether {}".format(interface,new_mac_address), shell=True)
subprocess.call("ifconfig {} up".format(interface), shell=True)
subprocess.call(“ifconfig”, shell=True)

run the python script which is just these colored text and give the input of interface and new mac address and 💥💥BOOM💥💥
our MAC address has been changed successfully..


Catch about this process:
	works very well, we have changed the MAC address successfully, what's the catch about this??
well, here it is,
	in linux or ubuntu, we can run multiple commands in a single line, with the commands being separated by semicolon(;)
	Eg: ifconfig; ls; cd Desktop;
	this command lists out the network interfaces, lists the folders or files in the current working directory, and finally changes you working directory to Desktop(inorder)
this means that the person who is trying to change the MAC address along with that he can also perform other tasks (security issue while trying to increasing security strength.😭😭)

So to control this activity here comes the second type of call method..

How it works:
	subprocess.call([“<command>”, “<options>”, “<arguments>”])
Breaking the lines of code:
	we know how call methods works, so let's dive into this wired syntax,
	the whole command that we need to run is enclosed in a square brackets and the command is divided in all the short strings whenever there is space in the command like
	Eg:	subprocess.call([“ls”, “-l”])
		this commands lists all the folders and files in the current working directory along with the hidden files.
So, how exactly it works
in the string that appears inside square brackets, the first string is the actual command name (like ls, ifconfig, aircrack-ng, etc..)
and the rest of the strings are the options that are available for that particular command their values
So if anyone tries to insert other commands in this syntax
	obviously a particular command cannot have another command as an option, so if we try to execute some other commands in between it gives us the error.
	try this command for experience:	
	we have to list all the folders and files in the working directory along with the network interfaces,
		import subprocess
		subprocess.call([“ifconfig”, “;”, “ls”])
	this gives you an error


now let's code in python to do the same task as above
	import subprocess
	interface = input(“interface: “)
	newMAC = input(“new MAC address: “)
subprocess.call([“ifconfig”, interface, “down”])
	subprocess.call([“ifconfig”, interface, “hw”, “ether”, newMAC])
	subprocess.call([“ifconfig”, interface, “up”])
now after running the program in terminal run the command ifconfig to see the changes..

Ahh.. finally in a secure way we are finally able to change our MAC address.

But would it be nice to run our program with arguments too like the inbuilt command and their commands,
	like.
	python mac.py --interface eth0 --mac 00:11:22:33:44:55

Yeah possible fellows, and we are gonna see that in our next example………

so in here all we need to do is that enable options feature to the user as like he/she can use options while using the commands
For that we have to use an inbuilt method in python called optparse package. More information about it in here
How it works:
	parser = optparse.OptionParser()
	parser.add_option(“-i”,”--interface”, dest=”Interface”, help=”Interface to change the MAC address”)
	(options, arguments) = parser.parse_args()
	interface = options.Interface
	let's say that the user in the terminal runs the program like this
		python <filename>.py --interface eth0
Time to break down the code:
	First we are creating a method from the optparse module and assigning it to the variable parser.
	Now we are adding options to the program by adding the line of code in the blue color.
	all the string before the dest property are the options can be used(Eg: for interface we can use either -i or --interface)
	and the dest value is like the identification of that option to use in our program
	Finally, the value is to give information about that particular option to the user about how to use it and what is the option ,  if the user doesn't know about it.
we can add multiple options in the same process.
	now this parser variable contains the arguments, options, help message, destination of that argument.
	time to grab these information separately and use them in our code, how do we do that..??
	by using the parse_args() function in that optparse method.
This function returns the options and arguments which are then used later in our code.
	now the question arises , how to catch the particular argument and use it in our code, well here it is
	options.<dest_value>   -> this gives the particular argument value.

now lets run our python code:
	import subprocess
	import optparse
	parse = optparse.OptionParser()
	parse.add_option(“-i”, “--interface”, dest=”Interface”, help=”Interface to change the MAC address”)
	parse.add_option(“-m”, “--mac”, dest=”new_MAC”, help=”new MAC address”)
	(options, arguments) = parse.parse_args()
	interface = options.Interface
	mac = options.new_MAC
	print(“[+] Changing MAC address for “+interface+” to “+mac)
	subprocess.call([“ifconfig”, interface, “down”])
	subprocess.call([“ifconfig”, interface, “hw”, “ether”, mac])
	subprocess.call(“ifconfig”, interface, “up”])

finally yeah we did it, 
	now this python code can accept arguments from the terminal and then assigns the values to the variables that we declared and then our code runs -> MAC address changes…….

What if the user forgets to give values at the terminal thinking that the code prompts for the value???
GO WORK ON IT BY YOUR OWN
you are trying to learn different techniques to exploit the system
means that you have to think out of the box.
take this as the assignment work or something else to be done.


