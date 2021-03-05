import os, sys, time, urllib.request, requests
from colorama import init, Fore

init(autoreset=True)

# Here is the function to know the public ip, do not modify this function unless you find an error.

def public_ip():
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	return ip

# The server class contains the components of the system menu, if you edit or add some function in the class you would be adding new content for the system.

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

     def header (self, link):
            try:
                 self.link = link
                 target = requests.get(url=link)
                 header = dict(target.headers)
                 for x in header:
                     print (x+ " : "+header[x])
            except:
                 print ("Error, could not connect to server")

     def installpackages (self):
            os.system ("""

            sudo apt update -y && sudo apt upgrade -y
            sudo apt install curl -y
            sudo apt install wget -y
            sudo apt install net-tools -y
            sudo apt install strace -y
            sudo apt install iftop -y
            sudo apt install lsof -y
            sudo apt install chkrootkit -y
            sudo apt install inxi -y
            sudo apt install lshw -y
            sudo apt install git -y
            sudo apt install python3 -y
            sudo apt install python3-pip -y
            sudo apt install build-essential libssl-dev libffi-dev python3-dev -y


             """)
