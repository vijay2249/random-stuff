# import GlobalFeatures.check_modules as pkg
import mod.check_modules_install as pkg
pkg.install_modules('requirements.txt')

import string
import pyperclip
import secrets
import logging
import argparse


WARN = "[=]"
INFO = "[+]"
ERROR = "[-]"

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", dest="Length", help="Length of password", type=int)
    options = parser.parse_args()
    if not options.Length:
        logging.warning(f"{WARN} length of password argument not provided, considering default value of 12")
        options.Length = 12
    return options

def run():
    user_input = get_arguments()
    letters, digits, special_chars = string.ascii_letters, string.digits, string.punctuation
    chars = letters + digits + special_chars

    gen_password = "".join(secrets.choice(chars) for i in range(user_input.Length))
    print(f"[+] Generated password - {gen_password}")
    pyperclip.copy(gen_password)
    print(f"[+] Password copied to clipboard")


if __name__ == "__main__":
    # check_modules_install()
    run()