This Password-Gen folder is written with one specific problem that I had while importing and installing required modules
  for now I considered that all required modules are present in requirements.txt file

So I want to write a simple python script that automatically does the job of verifying the modules and installing them if necessary without user necessarily running the pip install command

This is because i am lazy sometimes to run the pip install command and also i dont want to install same modules again and again..


### Usage
The default length of password generated is 12

You can change that by providing "-l" or "--length" argument

`python main.py -l <lengthOfPassword>`
