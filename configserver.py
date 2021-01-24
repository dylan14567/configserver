import os
import sys
import time
from colorama import init, Fore
from configserver.main import server

init(autoreset=True)

server = server ()
server._init_()

os.system ("clear")
              
def consola ():
      
      while True:
          
          try:
             user = input ("root@configserver ~# ")
     
             if user == 'set ip':
                     ip1 = input ()
                     server.ip (ip1)
             elif user == 'set port':
                     port1 = input ()
                     server.port (port1)
             elif user == 'server':
                     print (server)
             elif user == 'exit':
                     print ("Exiting")
                     os.system ("clear")
                     break
             else:
                     print ("Error")
          except:
                  print ("Error")

if True:
   consola ()
