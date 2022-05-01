from instabot import Bot
bot = Bot()
from sys import platform
from os import *
import colorama
class bcolors:
    OK = '\033[92m' 
    a = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
system("cls")
#system("figlet NIVOS | lolcat")
print(f"{bcolors.FAIL}This Tool Created By Janiue")
print(f"{bcolors.FAIL}Github  : https://github.com/janiue ")
print(f"{bcolors.FAIL}Discord : Jan20#6757")

username = str(input("UserName >> "))
passwd = input("Password >> ")
target = str(input("Target User >> "))
ms = int(input("Message Number >> "))
mss = str(input("Message >> "))

bot.login(username=username,
          password=passwd)

for i in range(1,ms):
    bot.send_message("message is being sent", mss,target)
