################################################################
#           This Repo Writed By Error                          #
################################################################
import platform
from colorama import Fore,Back,Style
import os
import socket
class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
my_system = platform.uname()

print(f"{bcolors.OK}[INFO] System      : {my_system.system}")
print(f"{bcolors.OK}[INFO] Node Name   : {my_system.node}")
print(f"{bcolors.OK}[INFO] Release     : {my_system.release}")
print(f"{bcolors.OK}[INFO] Version     : {my_system.version}")
print(f"{bcolors.OK}[INFO] Machine     : {my_system.machine}")
print(f"{bcolors.OK}[INFO] Processor   : {my_system.processor}")
