import os
import time
from colorama import Fore,Back,Style
import socket
import requests
from bs4 import BeautifulSoup
class bcolors:
    OK = '\033[92m' 
    a = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
    #TheSadError Repo
os.system("clear")
os.system("figlet NIVOS | lolcat")
print(f"{bcolors.FAIL}This Tool Created By Error")
print(f"{bcolors.FAIL}Github  : https://github.com/TheSadError ")
print(f"{bcolors.FAIL}Discord : err0r#4018")
print(" ")
print(f"{bcolors.OK}[NIVOS] Welcome To NIVOS -NIVOS-")
print(" ")
print(f"{bcolors.OK}[INFO] You Must Run This Tool By Super User Power.")
print(" ")
print(f"{bcolors.FAIL}[1]     Scan Devices In Your Network") # Error
print(f"{bcolors.FAIL}[2]     Scan Networks") # Error
print(f"{bcolors.FAIL}[3]     Try Crack Network With Mac [Adress Aircrack-ng]") # Error
print(f"{bcolors.FAIL}[4]     Scan Website [NMAP, WHOIS]") # Error
print(f"{bcolors.FAIL}[5]     DOS-DDOS") # Error
print(f"{bcolors.FAIL}[6]     Phone [Information Gathering , SMS Sender]") # Error
print(f"{bcolors.FAIL}[7]     Get Your Information [System INFO]") # Error
print(f"{bcolors.FAIL}[8]     Sniffing , Spoofing [Bettercap]") # Error
print(f"{bcolors.FAIL}[9]     IP [Information Gathering]") # Error
print(f"{bcolors.FAIL}[10]    Verify Gmail") # Error
print(f"{bcolors.FAIL}[11]    Port Scanner") # Error
print(f"{bcolors.FAIL}[12]    SQL Scan (WEBSITE)") # Error
print(f"{bcolors.FAIL}[13]    Discord Spammer") # Error
print(f"{bcolors.FAIL}[14]    Wordlist Generator") # Error
print(f"{bcolors.FAIL}[15]    Find Social Media Account With Username") # Error
print(f"{bcolors.FAIL}[16]    See index.html Source Of Website") # Error
print(f"{bcolors.FAIL}[17]    Creating Fake Wifi Acces Point For Phishing") # Error
print(f"{bcolors.FAIL}[18]    XSS Vulnerebility Scan") # Error
print(f"{bcolors.FAIL}[19]    Dedect ARP Spoof") # Error
print(f"{bcolors.FAIL}[20]    Image Meta Data") # Error
print(f"{bcolors.FAIL}[21]    Brute Force ZIP") # Error
print(f"{bcolors.FAIL}[22]    Instagram Bot") # Januie
print(f"{bcolors.FAIL}[23]    Email Extractor") # Error
print(f"{bcolors.FAIL}[24]    Password Generator") # Janiue
print(f"{bcolors.FAIL}[C]     Credits") # Error
print(f"{bcolors.FAIL}[Q]     Quit") # Error
print(" ")
i = input(f"{bcolors.OK}[MENU] Please Select Operation Number : ") # Error
if i=="1":
    os.system("sudo python3 ./nivo/NIVO_IP.py") # Error
elif i=="2":
    os.system("sudo python3 ./nivo/NIVO_NET.py") # Error
elif i == "3":
    os.system("sudo python3 ./nivo/NIVO_CRACK.py") # Error
elif i == "4":
    os.system("sudo python3 ./nivo/NIVO_WEB.py") # Error
elif i == "5":
    os.system("sudo python3 ./nivo/NIVO_DOS.py") # Error
elif i == "6":
    os.system("sudo python3 ./nivo/NIVO_PH.py") # Error
elif i == "7":
    os.system("sudo python3 ./nivo/NIVO_INF.py") # Error
elif i == "8":
    os.system("sudo python3 ./nivo/NIVO_BET.py") # Error
elif i == "9":
    os.system("sudo python3 ./nivo/NIVO_IPF.py") # Error
elif i == "10":
    os.system("sudo python3 ./nivo/NIVO_EM.py") # Error
elif i == "11":
    os.system("sudo python3 ./nivo/NIVO_PRT.py") # Error
elif i == "12":
    os.system("sudo python3 ./nivo/NIVO_SQL.py") # Error
elif i == "13":
    os.system("sudo python3 ./nivo/NIVO_DC.py") # Error
elif i == "14":
    os.system("sudo python3 ./nivo/NIVO_WRD.py") # Error
elif i == "15":
    os.system("sudo bash nivo/NIVO_FUSR.sh") # Error
elif i == "16":
    os.system("clear")
    os.system("figlet Error | lolcat")
    print(f"{bcolors.FAIL}This Tool Created By Error")
    print(f"{bcolors.FAIL}Github  : https://github.com/TheSadError ")
    print(f"{bcolors.FAIL}Discord : err0r#4018")
    url = input(f"{bcolors.OK}[NIVOS] Please Input URL : ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"{bcolors.FAIL}{soup}")
elif i == "17":
    os.system("sudo bash nivo/NIVO_FAKEP.sh") # Error
elif i == "18":
    os.system("sudo python3 ./nivo/NIVO_XSS.py") # Error
elif i == "19":
    os.system("sudo python3 ./nivo/NIVO_DARP.py") # Error
elif i == "20":
    os.system("sudo python3 ./nivo/NIVO_IMAGEM.py") # Error
elif i == "21":
    os.system("sudo python3 ./nivo/NIVO_ZIP.py") # Error
elif i == "22":
    os.system("sudo python3 ./nivo/NIVO_IG.py") # Error
elif i == "23":
    os.system("sudo python3 ./nivo/NIVO_EMX.py") # Error
elif i == "24":
    os.system("sudo python3 ./nivo/NIVO_PG.py")
elif i == "C" or i == "c":
    os.system("sudo python3 ./NH/NH_CR.py") # Error
elif i == "Q" or i == "q" :
    print("[INFO] Exitting...")

else:
    print(f"{bcolors.FAIL}[FAIL] Invalid Command Dedected. Please Input Valid Commands.") # Error
