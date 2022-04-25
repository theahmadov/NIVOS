################################################################
#           This Repo Writed By Error                          #
################################################################
import sys
import argparse
from validate_email import validate_email
import os
import time
from colorama import Fore,Back,Style
import socket
class bcolors:
    OK = '\033[92m' 
    a = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

os.system("clear")
print(f"{bcolors.OK}[NIVOS] Welcome To Email Verifier. Enter Your Email For Verify IT! ")
results = []
parser = argparse.ArgumentParser(description="email verification utility")
parser.add_argument('--email', help='email(s) to scan', metavar='EMAIL')
parser.add_argument('-f', '--file', help='file with email(s) to check')

args = parser.parse_args()


BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;32m', '\033[0m'

def search():
    if args.file:
        inputfile = args.file
    else:
        inputfile = input('Path to file with email addresses to scan: ')
		
    with open(inputfile) as infile:
        for line in infile:
            results.append(line.strip())
    count = 0
    for i in results:
        is_valid = validate_email(i,verify=True)
        count += 1
        if is_valid == True:
            sys.stdout.write(GREEN + "[*] FOUND - [" + i + "] "+ BLUE + "{line " + str(count) + "}\n" + END)
        else:
            sys.stdout.write(RED + "[!] NOTFOUND - [" + i + "]" + BLUE + " {line " + str(count) + "}\n" + END)

def single():
    if args.email:
        ema = str(args.email)
    else:
        ema = input('Email address to verify : ')
    is_valid = validate_email(ema,verify=True)
    if is_valid == True:
        sys.stdout.write(GREEN + "[*] FOUND - [" + ema + "]\n" + END)
    else:
        sys.stdout.write(RED + "[!] NOTFOUND - [" + ema + "]\n" + END)


def menu():
    print("[NIVOS] Select an option :")
    print(f"{bcolors.FAIL}[1]    Perform a search of emails from specified file")
    print(f"{bcolors.FAIL}[2]    Single search for specified email")
    print(f"{bcolors.FAIL}[E]    Exit")
    while True:
        try:
            ask = input("[NIVOS] > ").format(RED, END)
            if ask.upper() == "1":
                search()
            if ask.upper() == "2":
                single()
            if ask.upper() == "E":
                sys.exit(0) 
        except:
            print("\n[NIVOS] BB :>")
            sys.exit(0)

def main():
    if args.email:
        single()
    elif args.file:
        search()
    else:
        menu()

if __name__ == '__main__':
    main()
