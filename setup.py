import os
from colorama import Fore,Back,Style

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

print(f"{bcolors.FAIL}[1]      Debian Based (Kali,Parrot,KDE...)")
print(f"{bcolors.FAIL}[2]      Arch Based (Arch,Manjora,GARUDA...)")
n = int(input(f"{bcolors.FAIL}[OS] Select Your Os : "))

if n==1:
    os.system("sudo bash ./nivo/debian.sh")
elif n==2:
    os.system("sudo bash ./nivo/arch.sh")
else:
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")