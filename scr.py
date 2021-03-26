import os
import sys
import subprocess as sp


dist1 = "centos"
dist2 = "ubuntu"


user = sp.getoutput("whoami")
os.system("egrep -i -h 'centos|ubuntu' /etc/*-release > /home/"+str(user)+"/info")
with open("info", "r") as file:
	distOS = file.read().replace('\n','')
distOS = distOS.lower()


if dist1 in distOS:
	print ("Your system is CentOS")
	os.system("sudo yum check-update")
	ask = input("Do you want to install Docker? y/n \n")
	if ask == "y":
		os.system("sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
		os.system("sudo dnf list docker-ce")
		os.system("sudo dnf install docker-ce --allowerasing")
		os.system("sudo systemctl enable --now docker")
		os.system("sudo yum check-update")
		os.system("sudo systemctl status docker")
		ask = input("Do you want start check container and check working of Docker? y/n\n")
		if ask == "y":
			newDockFile = open("/home/cent/Dockerfile", "w") 
			newDockFile.write("from helloworld\n")	
			newDockFile.close()
			os.system("sudo docker build .")
			os.system("sudo docker run --it helloworld")
		else:
			print("Check it yourself")
			sys.exit(0)
	else:
		print("Docker will not be installed")
		sys.exit(0)
else:
	if dist2 in distOS:
		print("your system is ubuntu")
	else:
		print("There is not installed system, which supported by the script!")
		sys.exit(1)


os.system("rm info")
sys.exit(0)
