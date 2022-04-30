
import zipfile
import sys
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
print(f"{bcolors.FAIL}This Tool Created By Error")
print(f"{bcolors.FAIL}Github  : https://github.com/TheSadError ")
print(f"{bcolors.FAIL}Discord : err0r#4018")
print(f"{bcolors.FAIL}[NIVOS] Welcome To ZIP File Brute Forcer")
def crack_password(password_list, obj):
    idx = 0
    with open(password_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    idx += 1
                    obj.extractall(pwd=word)
                    print("Password found at line", idx)
                    print("Password is", word.decode())
                    return True
                except:
                    continue
    return False
  
  
zip_file = input(f"{bcolors.OK}[NIVOS] Please Input ZIP FILE Path : ")
password_list = input(f"{bcolors.OK}[NIVOS] Please Input Wordlist Path : ")
  
obj = zipfile.ZipFile(zip_file)
  
cnt = len(list(open(password_list, "rb")))
  
print("There are total", cnt,
      "number of passwords to test")
  
if crack_password(password_list, obj) == False:
    print("Password not found in this file")
