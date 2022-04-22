import os
import time
from colorama import Fore,Back,Style
import socket
class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
os.system("clear")
os.system("figlet Error | lolcat")
print(f"{bcolors.WARNING}This Tool Created By Error")
print(f"{bcolors.WARNING}Github  : ")
print(f"{bcolors.WARNING}Discord : err0r#4018")
print(" ")
print(f"{bcolors.OK}[NIVOS] Welcome To NIVO IP Scanner -NIVOS-")
print(" ")
print(f"{bcolors.OK}[INFO] You Must Run This Tool By Super User Power.")
print(" ")
print(f"{bcolors.WARNING}[1]     Scan Devices In Your Network")
print(f"{bcolors.WARNING}[2]     Scan Networks")
print(f"{bcolors.WARNING}[3]     Try Crack Network With Mac [Adress Aircrack-ng]")
print(f"{bcolors.WARNING}[4]     Scan Website [NMAP, WHOIS]")
print(f"{bcolors.WARNING}[5]     DOS-DDOS")
print(f"{bcolors.WARNING}[6]     Phone [Information Gathering , SMS Sender]")
print(f"{bcolors.WARNING}[7]     Get Your Information [System INFO]")
print(f"{bcolors.WARNING}[8]     Sniffing , Spoofing [Bettercap]")
print(f"{bcolors.WARNING}[9]     IP [Information Gathering]")
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
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
