# _*_coding=UTF-8_*_
import sys,time
from module import *

def menu():
	print ("\033[35;1m[1]. START")
	print ("\033[35;1m[2]. ABOUT")
	print ("\033[35;1m[3]. EXIT\n")
	p = input("\033[37;1m [?] SELECT: \033[32;1m")
	if p == "1" or p == "01":
		start_menu()
	elif p == "2" or p == "02":
		about()
	elif p == "3" or p == "03":
		print ("\033[32;1m[!] Thank you for using our tool\033[0m")
		sys.exit()
	else:
		print ("\033[31;1m [×] Wrong Input")
		time.sleep(2)
		ulang()
banner()
menu()
