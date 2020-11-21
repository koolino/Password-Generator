import string
import random
from termcolor import colored
import os

cmd = "clear"
os.system(cmd)
print(colored("""

     _____                                    _          
    |  __ \                                  | |         
    | |__) |_ _ ___ _____      _____  _ __ __| |         
    |  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |         
    | |  | (_| \__ \_  \ \V  V / (_) | | | (_| |         
    |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|         
           _____                           _             
          / ____|                         | |            
         | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
         | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
         | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
          \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                         
                                                         
 
""",'green'),colored("By Adem TCL ","red"))
input(colored("Press Enter to continue...","green"))


print(colored("1","yellow"),colored(".","red"),colored("Simple Password","green"))
print(colored("2","yellow"),colored(".","red"),colored("Advanced Password","green"))
print(colored("3","yellow"),colored(".","red"),colored("Calculate Password","green"))
choice = int(input(colored("Enter A Number : ","yellow")))
test = ""
if choice == 1 or choice == 2 :
	num=int(input(colored("Please Enter Your Password Length : ","yellow")))
	if choice == 1 :
		input(colored("Please Enter Informations That you will Remember ! ","red"))
		nums = int(input(colored("How Much Information You Would Enter ? : ","yellow")))
		for i in range(0,nums):
			print(colored("Enter Here Info : ","yellow"))
			i = input()
			test += i
		password = ''.join(random.sample(test,len(test)))
		npass = list(password)
		password = npass[0:num]
		pas = ""
		for i in range(0,num):
			pas += password[i]
	if choice == 2 :
		lis = string.ascii_uppercase+string. ascii_lowercase+string.punctuation+string.digits
		pas =  ""
		while len(pas) < num :
		     h=random.choice(lis)
		     pas += str(h)
	print(colored("The Password Is : ","cyan"),pas)
if choice == 3 :
	passworded = input("Enter A Password Please : ")
	if len(passworded) >= 8:
		print(colored("GOOD","green"))
	else:
		print(colored("WEAK","red"))
