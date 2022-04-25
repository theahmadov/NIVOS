################################################################
#           This Repo Writed By Error                          #
################################################################
from scapy.all import ARP, Ether, srp
import colorama
from colorama import Fore,Back,Style
import os
import time
os.system("clear")

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

os.system("figlet Error | lolcat")
print(f"{bcolors.FAIL}This Tool Created By Error ")
print(f"{bcolors.FAIL}Github  : https://github.com/TheSadError")
print(f"{bcolors.FAIL}Discord : err0r#4018")
print(" ")
print(f"{bcolors.OK}[NIVOS] Starting...")
time.sleep(1)
ip = "192.168.100.1/24"
arp = ARP(pdst=ip)
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
packet = ether/arp
result = srp(packet, timeout=3, verbose=0)[0]
devices = []

for sent, received in result:
    devices.append({'ip': received.psrc, 'mac': received.hwsrc})


print(f"{bcolors.OK}[NIVOS] Searching Devices...")
time.sleep(3)
print(" ")
print(f"{bcolors.FAIL}IP" + " "*18+"MAC")

for i in devices:
    print("{:16}    {}".format(i['ip'], i['mac']))

print(" ")

print(f"{bcolors.OK}[NIVOS] Finished...")
