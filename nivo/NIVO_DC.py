import time
import requests
import os
from colorama import Fore,Back,Style
import socket
class bcolors:
    OK = '\033[92m' 
    a = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
    #TheSadError Repo
os.system("clear")
msg = input(f"{bcolors.OK}[NIVOS] Please Enter Message For Spam : ")
webhook = input(f"{bcolors.OK}[NIVOS] Please Enter WebHook URL: ")
time.sleep(1)
def spam(msg, webhook):
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print(f"{bcolors.FAIL}[NIVOS] Bad Webhook : " + webhook)
            time.sleep(5)
            exit()
kingman_top = 1
while kingman_top == 1:
    spam(msg, webhook)
