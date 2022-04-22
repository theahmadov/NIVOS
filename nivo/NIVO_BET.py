import os

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 

print(f"{bcolors.OK}[NIVOS] Sniffing Spoofing")
print(f"{bcolors.OK}[NIVOS] Starting...")

os.system("sudo bettercap")
