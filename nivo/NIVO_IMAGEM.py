from PIL import Image
from PIL.ExifTags import TAGS
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
imagename = input(f"{bcolors.OK}[NIVOS] Please Input Image Path : ")
image = Image.open(imagename)
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label,value in info_dict.items():
    print(f"{label:25}: {value}")
exifdata = image.getexif()
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
