import os, sys, time, urllib.request, requests
from colorama import init, Fore

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

            echo " Enter the username: "
            read name
            adduser $name

             """)

     def verifylogin (self):
            os.system ("w")

     def verifylastlogin (self):
            os.system ("last")

     def checkcpuprocesses (self):
            os.system ("top")

     def checkcpuprocessesstrace (self):
            os.system ("""

            echo " Write the <PID Number>: "
            read numero
            strace -d -p $numero
            
             """)

     def checksystemprocesses (self):
            os.system ("ps auxf")

     def destroyprocess (self):
            os.system ("""

            echo " WRITE THE PIP: "
            read numero1
            kill -9 $numero1


             """)

     def checknetworktraffic (self):
            os.system ("iftop")

     def checklistenerports (self):
            os.system ("netstat -plunt")

     def checklistenerportslsof (self):
            os.system ("lsof -p")

     def checkrootkit (self):
            os.system ("chkrootkit")

     def header (self):
            try:
                 print (Fore.CYAN + "Do not use a website that is not yours because it is not legal, use your website because it is legal.")
                 link = input ("Write the link: ")
                 target = requests.get(url=link)
                 header = dict(target.headers)
                 for x in header:
                     print (x+ " : "+header[x])
            except:
                 print ("Error, could not connect to server")
