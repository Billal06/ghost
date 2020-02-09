import sys,os,socket
def banner():
        clear()
        print ("""\033[32;1m
 _____ _     ____  ____  _____    _____  ____  ____  _
/  __// \ /|/  _ \/ ___\/__ __\  /__ __\/  _ \/  _ \/ \\
| |  _| |_||| / \||    \  / \      / \  | / \|| / \|| |
| |_//| | ||| \_/|\___ |  | |      | |  | \_/|| \_/|| |_/\\
\____\\\_/ \|\____/\____/  \_/      \_/  \____/\____/\____/\033[33;1m
   CYBER GHOST INDONESIAN             \033[37;1mBILLAL FAUZAN\033[33;1m
     BLACK CODER CRUSH           \033[37;1mhttps://github.com/billal06
""")

def about():
	print ("""
Author: BILLAL FAUZAN
Version: 0.1
Thanks To: Allah SWT, And You

API: https://billal.herokuapp.com
""")
def ulang():
	file = sys.argv[0]
	os.system("python "+file)

def clear():
	os.system("clear")

def run(command):
	os.system(command)

def start_menu():
	banner()
	print ("\033[35;1m[1]. IP Tracker \033[33;1m(INFOGA)")
	print ("\033[35;1m[2]. HAMMER \033[33;1m(DDOS TOOL)")
	print ("\033[35;1m[3]. HULK \033[33;1m(DDOS TOOL)")
	print ("\033[35;1m[4]. Scan IP \033[33;1m(INFOGA)")
	p = input("\033[37;1m [?] SELECT: \033[32;1m")
	if p == "1" or p == "01":
		ip = input("\033[37;1m [?] IP: \033[32;1m")
		if ip:
			run("python Tools/track/scan.py "+ip)
		else:
			print ("\033[31;1m[×] Please input IP");sys.exit()
	elif p == "2" or p == "02":
		ip = input("\033[37;1m [?] IP: \033[32;1m")
		if ip:
			run("python Tools/hammer/hammer.py -s "+ip+" -p 80 -t 135")
		else:
			print ("\033[31;1m[×] Please input IP");sys.exit()
	elif p == "3" or p == "03":
		web = input("\033[37;1m [?] WEB: \033[32;1m")
		if web:
			run("python2 Tools/hulk/hulk.py "+web)
		else:
			print ("\033[31;1m[×] Please input WEB");sys.exit()
	elif p == "4" or p == "04":
		web = input("\033[37;1m [?] WEB: \033[32;1m")
		if web:
			try:
				ip = socket.gethostbyname(web)
				print ("\033[33;1m[√] IP: \033[32;1m"+ip);sys.exit()
			except socket.gaierror:
				print ("\033[31;1m[×] No Address with hostname");sys.exit()
		else:
			print ("\033[31;1m[×] Please input WEB");sys.exit()
