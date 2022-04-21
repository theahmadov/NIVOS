import os
print("[1]      Debian Based (Kali,Parrot,KDE...)")
print("[2]      Arch Based (Arch,Manjora,GARUDA...)")
n = int(input("[OS] Select Your Os : "))

if n==1:
    os.system("sudo bash ./nivo/debian.sh")
elif n==2:
    os.system("sudo bash ./nivo/arch.sh")
else:
    print("[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
