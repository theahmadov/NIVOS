################################################################
#           This Repo Writed By Error                          #
################################################################
import scapy.all as scapy
import re
from threading import Thread
import time
import os
from colorama import Fore,Back,Style

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

print(f"{bcolors.OK}[NIVOS] Starting...")
time.sleep(1)
os.system("sudo airmon-ng check kill")
print(f"{bcolors.FAIL}[1] wlan0mon")
print(f"{bcolors.FAIL}[2] wlan1mon")
n = int(input(f"{bcolors.OK}[MENU] Please Select Interface : "))
iw = "wlan1"
if n == 1:
    iw="wlan0"
elif n == 2:
    iw="wlan1"
else:
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
print(" ")
print(f"{bcolors.OK}[NIVOS] Selected Interface : "+iw)
print(" ")
os.system("sudo airmon-ng start "+iw)
os.system("sudo airodump-ng "+iw)
