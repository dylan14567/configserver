import os
import sys
import time

class server:

     def _init_(self):
            print ("\033[;36m"+"Welcome")
   
     def ip (self, ip):
            self.ip = ip
            print ("The ip is", ip)

     def port (self, port):
            self.port = port
            print ("The port is", port)

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
