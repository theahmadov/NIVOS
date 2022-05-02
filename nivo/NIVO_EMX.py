import re
from requests_html import HTMLSession
import os
import time
from colorama import Fore,Back,Style
import socket
from bs4 import BeautifulSoup
class bcolors:
    OK = '\033[92m' 
    WA = '\033[93m' 
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
url = input(f"{bcolors.FAIL}[NIVOS] Please Enter URL To Extract Email : ")
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
session = HTMLSession()
r = session.get(url)
r.html.render()

for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    print(re_match.group())
