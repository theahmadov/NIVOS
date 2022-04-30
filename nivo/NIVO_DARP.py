from scapy.all import Ether, ARP, srp, sniff, conf
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
os.system("figlet Error | lolcat")
print(f"{bcolors.OK}This Tool Created By Error")
print(f"{bcolors.OK}Github  : https://github.com/TheSadError ")
print(f"{bcolors.OK}Discord : err0r#4018")
print(f"{bcolors.OK}[NIVOS] Welcome To ARP Spoof Dedector Tool...")
def get_mac(ip):
    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc

def process(packet):
    if packet.haslayer(ARP):
        if packet[ARP].op == 2:
            try:
                real_mac = get_mac(packet[ARP].psrc)
                response_mac = packet[ARP].hwsrc
                if real_mac != response_mac:
                    print(f"[!] You are under attack, REAL-MAC: {real_mac.upper()}, FAKE-MAC: {response_mac.upper()}")
            except IndexError:
                pass

if __name__ == "__main__":
    import sys
    try:
        iface = sys.argv[1]
    except IndexError:
        iface = conf.iface
    sniff(store=False, prn=process, iface=iface)
