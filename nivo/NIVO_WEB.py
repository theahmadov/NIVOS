################################################################
#           This Repo Writed By Error                          #
################################################################
import scapy.all as scapy
import re
from threading import Thread
import time
import socket
import os
from colorama import Fore,Back,Style
import requests

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 



print(f"{bcolors.OK}[NIVOS] Welcome To Website Scanner...")
print(" ")
url = input(f"{bcolors.WARNING}[NIVOS] Please Input URL : ")
def nmap(options,ip):
    command = "sudo nmap " + options + " " + ip
    process = os.popen(command)
    results = str(process.read())
    return results

def whois(url):
    command = 'sudo whois '+ url
    process = os.popen(command)
    results = str(process.read())
    return results

print(f"{bcolors.WARNING}[1]    NMAP INFO Scan")
print(f"{bcolors.WARNING}[2]    Whois Scan")
print(f"{bcolors.WARNING}[3]    NMAP Vulnerabilities Scan")
n = int(input(f"{bcolors.WARNING}[NIVOS] Please Select Option : "))
#print(f"{bcolors.OK}[NIVOS] ")
print(" ")
if n==1:
    print(nmap("-F",url))
elif n==2:
    print(whois(url))
elif n==3:
    print(f"{bcolors.WARNING}[INFO] 1. Scan")
    os.system("sudo nmap -sV "+url)
    print(f"{bcolors.WARNING}[INFO] 2. Scan")
    pr = int(input("[NIVOS] Please Input Open Port : "))
    os.system("sudo nmap -Pn --script vuln "+" "+url+" -p {pr}")
else:
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
