################################################################
#           This Repo Writed By Error                          #
################################################################
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import os
class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
os.system("clear")
def info():
    mobileNo=input(f"{bcolors.WARNING}[NIVOS] Please Enter Number Via + : ")
    mobileNo=phonenumbers.parse(mobileNo)
    print(timezone.time_zones_for_number(mobileNo))
    print(carrier.name_for_number(mobileNo,"en"))
    print(geocoder.description_for_number(mobileNo,"en"))
    print("Valid Mobile Number:",phonenumbers.is_valid_number(mobileNo))
    print("Checking possibility of Number:",phonenumbers.is_possible_number(mobileNo))
def sms():
    text = input(f"{bcolors.WARNING}[NIVOS] Please Entter Message : ")
    for match in phonenumbers.PhoneNumberMatcher(text, "US"):
        print(match)
    y = input(f"{bcolors.WARNING}[NIVOS] Please Enter Number To Send : ")
    x = phonenumbers.parse(y, None)
    phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
print(f"{bcolors.OK}[NIVOS] You Are Welcome To Phone Tool ")
print(f"{bcolors.WARNING}[1]    Phone Info")
print(f"{bcolors.WARNING}[2]    Send Sms")
n = int(input(f"{bcolors.WARNING}[NIVOS] Please Select : "))
if n==1:
    info()
elif n==2:
    sms()
else:
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
