import string
import random
from colorama import Fore,Back,Style
import os
os.system("clear")
class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m'
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

print(f"{bcolors.OK}This Tool Created By Janiue")
print(f"{bcolors.OK}Github  : https://github.com/janiue ")
print(f"{bcolors.OK}Discord : Jan20#6757")

uzunluq = int(input("[NIVOS]Enter password length: "))

random.shuffle(characters)

password = []
for i in range(uzunluq):
    password.append(random.choice(characters))


random.shuffle(password)


print("".join(password))