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

     def addnewuser (self):
            os.system ("""

            read -p " Enter the username: " name
            adduser $name

            export user1=$name

             """)

            user1 = os.environ.get ('user1')
            print ("The new user is", user1)

     def verifylogin (self):
            os.system ("w")

     def verifylastlogin (self):
            os.system ("last")

     def checkcpuprocesses (self):
            os.system ("top")
            

server = server ()

def public_ip():
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	return ip
              
def main ():
      
      while True:
          
          try:
             global user

             os.system ("clear")

             print (Fore.CYAN + "1- Add IP")
             print (Fore.CYAN + "2- Add port")
             print (Fore.CYAN + "3- System information")
             print (Fore.CYAN + "4- Listing all users")
             print (Fore.CYAN + "5- Add a New User")
             print (Fore.CYAN + "6- Verify Current Login")
             print (Fore.CYAN + "7- Verify Last Login")
             print (Fore.CYAN + "8- Check CPU processes")
             print (Fore.CYAN + "9- Exit")

             user = int (input (">>> "))
     
             if user == 1:
                     os.system ("clear")
                     ip1 = input ()
                     server.ip (ip1)
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 2:
                     os.system ("clear")
                     port1 = input ()
                     server.port (port1)
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 3:
                     os.system ("clear")
                     server.systeminfo ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 4:
                     os.system ("clear")
                     server.listusers ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 5:
                     os.system ("clear")
                     server.addnewuser ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 6:
                     os.system ("clear")
                     server.verifylogin ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 7:
                     os.system ("clear")
                     server.verifylastlogin ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 8:
                     os.system ("clear")
                     server.checkcpuprocesses ()
                     print (Fore.CYAN + "Hit enter to get out of here")
                     input ()
                     os.system ("clear")
             elif user == 9:
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

if __name__ == "__main__":
          main ()
