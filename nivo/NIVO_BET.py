import os# Error

class bcolors:# Error
    OK = '\033[92m' # Error
    WARNING = '\033[93m' # Error
    FAIL = '\033[91m' # Error
    RESET = '\033[0m' # Error

print(f"{bcolors.OK}[NIVOS] Sniffing Spoofing")# Error
print(f"{bcolors.OK}[NIVOS] Starting...")# Error

os.system("sudo bettercap")
