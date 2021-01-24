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

os.system ("clear")
              
def consola ():
      
      while True:
          
          try:
             user = input ("root@configserver ~# ")
     
             if user == 'set ip':
                     ip1 = input ()
                     server.ip (ip1)
             elif user == 'exit':
                     print ("Exiting")
                     os.system ("clear")
                     break
             else:
                     print ("Error")
          except:
                  print ("Error")

consola ()
