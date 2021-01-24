import os
import sys
import time

class server:

     def _init_(self):
            print ("Welcome")
   
     def ip (self, ip):
            self.ip = ip
            print ("The ip is", ip)

server = server ()
server._init_()
              
def menu ():
      
      while True:
            
            user = input ("root@configserver ~# ")
