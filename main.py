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
os.system("figlet Error | lolcat")
print(f"{bcolors.FAIL}This Tool Created By Error")
print(f"{bcolors.FAIL}Github  : https://github.com/TheSadError ")
print(f"{bcolors.FAIL}Discord : err0r#4018")
print(" ")
print(f"{bcolors.OK}[NIVOS] Welcome To NIVOS -NIVOS-")
print(" ")
print(f"{bcolors.OK}[INFO] You Must Run This Tool By Super User Power.")
print(" ")
print(f"{bcolors.FAIL}[1]     Scan Devices In Your Network")
print(f"{bcolors.FAIL}[2]     Scan Networks")
print(f"{bcolors.FAIL}[3]     Try Crack Network With Mac [Adress Aircrack-ng]")
print(f"{bcolors.FAIL}[4]     Scan Website [NMAP, WHOIS]")
print(f"{bcolors.FAIL}[5]     DOS-DDOS")
print(f"{bcolors.FAIL}[6]     Phone [Information Gathering , SMS Sender]")
print(f"{bcolors.FAIL}[7]     Get Your Information [System INFO]")
print(f"{bcolors.FAIL}[8]     Sniffing , Spoofing [Bettercap]")
print(f"{bcolors.FAIL}[9]     IP [Information Gathering]")
print(" ")
i = int(input(f"{bcolors.OK}[MENU] Please Select Operation Number : "))
if i==1:
    os.system("sudo python3 ./nivo/NIVO_IP.py")
elif i==2:
    os.system("sudo python3 ./nivo/NIVO_NET.py")
elif i == 3:
    os.system("sudo python3 ./nivo/NIVO_CRACK.py")
elif i == 4:
    os.system("sudo python3 ./nivo/NIVO_WEB.py")
elif i == 5:
    os.system("sudo python3 ./nivo/NIVO_DOS.py")
elif i == 6:
    os.system("sudo python3 ./nivo/NIVO_PH.py")
elif i == 7:
    os.system("sudo python3 ./nivo/NIVO_INF.py")
elif i == 8:
    os.system("sudo python3 ./nivo/NIVO_BET.py")
elif i == 9:
    os.system("sudo python3 ./nivo/NIVO_IPF.py")

else:
    print(f"{bcolors.FAIL}[FAIL] Invalid Command Dedected. Please Input Valid Commands.")
