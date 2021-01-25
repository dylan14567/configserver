import os
import sys
import time
from colorama import init, Fore

init(autoreset=True)

class server:

     def __init__(self):
            print (Fore.CYAN + "Welcome")
   
     def ip (self, ip):
            self.ip = ip
            print (Fore.CYAN + "The ip is", ip)

     def port (self, port):
            self.port = port
            print (Fore.CYAN + "The port is", port)

server = server ()
server.__init__()

os.system ("clear")
              
def consola ():
      
      while True:
          
          try:
             global user

             print (Fore.CYAN + "1- Add IP")
             print (Fore.CYAN + "2- Add port")
             print (Fore.CYAN + "3- ??")
             print (Fore.CYAN + "4- Exit")

             user = input (">>> ")
     
             if user == 1:
                     ip1 = input ()
                     server.ip (ip1)
             elif user == 2:
                     port1 = input ()
                     server.port (port1)
             elif user == 3:
                     print (server)
             elif user == 4:
                     print ("Exiting")
                     os.system ("clear")
                     break
             else:
                     print ("Error")
          except:
                  print ("Error")

if True:
   consola ()
