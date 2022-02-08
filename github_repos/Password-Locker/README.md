# Password-Locker

## About
This is a local passwordLocker that I created based on the learnings from Automate Boring Stuff with Python book.

You can find the resources [here](https://github.com/DUMMY-the-BOT/ebooks-1) for the book pdf

This basically creates a binary file called locker in your directory where this file is downloaded.

Based on your OS this creates different files,
    
    in Windows it created three files with .dat .dir and .bak extensions
    in mac os and linux systems it creates just .db extension file

This is the created using shelve module

The user password is then encrypted by using the Fernet methods in cryptography module and then stored into the binary file created

When user requests for the particular password to be copied to the clipboard then the program decrypts the password stored and the final value is copied to clipboard

User can also ask for new password generation in the program using the arguments
    
    python passwordLocker.py new <site> <length_of_password>

This then creates new password of given length by using password_generator module

Also the password strength is checked for each password, if it is not a strong password then error pops up giving some suggestions to make a good strong password

# usage

    python passwordLocker.py passwordsuggestions -> gives suggestions to create strong password

    python passwordLocker.py delete -> deletes all the stored passwords

    python passwordLocker.py list -> to list all the sites stored in the list

    python passwordLocker.py copy <site> -> to copy the site password to the clipboard

    python passwordLocker.py delete <site> -> removes the site and password from the list

    python passwordLocker.py update <site> <password> -> updates the already present password

    python passwordLocker.py save <site> <password> -> to save a password corresponding to site

    python passwordLocker.py new <site> <length> -> generated strong password of given length for site mentioned and stores it

# Disclaimer:
## ALL THE SITE NAMES AND PASSWORDS ARE CASE SENSITIVE

# Modules used:
[re](https://docs.python.org/3/library/re.html)

[sys](https://docs.python.org/3/library/sys.html)

[shelve](https://docs.python.org/3/library/shelve.html)

[pyperclip](https://pypi.org/project/pyperclip/)

[cryptography](https://pypi.org/project/cryptography/)

[password_generator.password](https://password-generator-module.readthedocs.io/en/latest/index.html)
