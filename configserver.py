import os
import sys
import time
import urllib.request
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
     
     def systeminfo (self):
            print (Fore.CYAN + "Machine architecture:")
            os.system ("uname -m")
            print (Fore.CYAN + "Kernel version used:")
            os.system ("uname -r")
            print (Fore.CYAN + "Ubuntu system specifications:")
            os.system ("lshw")
            print (Fore.CYAN + "Private IP Address:")
            os.system ("ifconfig wlan0")
            print (Fore.CYAN + "Public IP Address:")
            print(public_ip())
            print (Fore.CYAN + "More system information:")
            os.system ("inxi")
            print (Fore.CYAN + "Username:")
            os.system ("whoami")

     def listusers (self):
            os.system ("awk -F: '{ print $1}' /etc/passwd")
            

server = server ()

def public_ip():
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	return ip
              
def consola ():
      
      while True:
          
          try:
             global user

             print (Fore.CYAN + "1- Add IP")
             print (Fore.CYAN + "2- Add port")
             print (Fore.CYAN + "3- System information")
             print (Fore.CYAN + "4- Listing all users")
             print (Fore.CYAN + "5- Exit")

             user = input (">>> ")
     
             if user == 1:
                     ip1 = input ()
                     server.ip (ip1)
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
             elif user == 2:
                     port1 = input ()
                     server.port (port1)
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
             elif user == 3:
                     server.systeminfo ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
             elif user == 4:
                     server.listusers ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
             elif user == 5:
                     print ("Exiting")
                     os.system ("clear")
                     break
             else:
                     print ("Error")
          except ValueError:
                  print (Fore.GREEN + "Error, there is a type of error.")
                  sys.exit ()
          except KeyboardInterrupt:
                  print (Fore.GREEN + "Exiting...")
                  sys.exit ()
          except NameError:
                  print (Fore.GREEN + "Error, the command I use is not available in the program code.")
                  sys.exit ()
          except SyntaxError:
                  print (Fore.GREEN + "Error, the code has a syntax error.")
                  sys.exit ()
          except TypeError:
                  print (Fore.GREEN + "Error, the code is misspelled.")
                  sys.exit ()

if True:
   consola ()
