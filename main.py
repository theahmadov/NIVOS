import os
import time
from colorama import Fore,Back,Style

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

os.system("figlet Error | lolcat")
print(f"{bcolors.FAIL}This Tool Created By Error")
print(f"{bcolors.FAIL}Github  : ")
print(f"{bcolors.FAIL}Discord : err0r#4018")
print(" ")
print(f"{bcolors.OK}[NIVOS] Welcome To NIVO IP Scanner -NIVOS-")
print(" ")
print(f"{bcolors.OK}[INFO] You Must Run This Tool By Super User Power.")
print(" ")
print(f"{bcolors.WARNING}[1]     Scan Devices In Your Network")
print(f"{bcolors.WARNING}[2]     Scan Networks")
print(f"{bcolors.WARNING}[3]     Try Crack Network With Mac Adress")
print(f"{bcolors.WARNING}[4]     Scan Website")
print(f"{bcolors.WARNING}[5]     DOS-DDOS")
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

else:
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
