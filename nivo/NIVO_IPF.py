################################################################
#           This Repo Writed By Error                          #
################################################################
import requests
import sys
import os
import time
from colorama import Fore,Back,Style,init
import socket
class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m'

os.system("clear")
def locate():
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy")
    resp = data.json()
    print(" ")
    print(f"{bcolors.WARNING}[INFO] Results :\n")
    print(bcolors.WARNING + "Status : " + resp["status"])
    if resp["status"] == "fail":
        print(bcolors.WARNING + "Fail : " + resp["message"])
        sys.exit()
    print(bcolors.WARNING + "Continent: " + resp["continent"])
    print("Country Code     : " + resp["continentCode"])
    print("Pays             : " + resp["country"])
    print("Pays Code        : " + resp["countryCode"])
    print("Region           : " + resp["region"])
    print("Region Number    : " + resp["regionName"])
    print("City             : " + resp["city"])
    print("Districte        : " + resp["district"])
    print("Code Postal      : " + resp["zip"])
    print("Latitude         : " + str(resp["lat"]))
    print("Longitude        : " + str(resp["lon"]))
    print("Timezone         : " + resp["timezone"])
    print("Operator         : " + resp["isp"])
    print("AS               : " + resp["as"])
    print("Mobile           : " + str(resp["mobile"]))
    print("Proxy            : " + str(resp["proxy"]))

print(bcolors.WARNING + "[NIVOS] Welcome To Ip Tracker : ")
ip = input(bcolors.WARNING + "Input IP :\n[>] ")
locate()
