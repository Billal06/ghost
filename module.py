import sys,os,socket, time
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
	print ("\033[35;1m[5]. Bypass DUIT CC \033[33;1m(BYPASS)")
	print ("\033[35;1m[6]. Termux Key")
	print ("\033[35;1m[6]. Home Termux ")
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
	elif p == "5" or p == "05":
		url = input("\033[37;1m [?] URL: \033[32;1m")
		if url:
			run("python Tools/duitcc/duit.py "+url)
		else:
			print ("\033[31;1m[×] Please input URL");sys.exit()
	elif p == "6" or p == "06":
		print ("\033[32;1m[!] Remove Old")
		time.sleep(3)
		run("rm -rf $HOME/.termux/termux.properties")
		print ("[√] Success")
		time.sleep(1)
		print ("[!] Add new key")
		time.sleep(3)
		try:
			os.mkdir("$HOME/.termux")
		except OSError: pass
		data = """
extra-keys = [['F6','{}','[]','<>','()','""',"''"],['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]
"""
		o = open("/data/data/com.termux/files/home/.termux/termux.properties","w")
		o.write(data)
		o.close()
		print ("[√] Success")
		time.sleep(3)
		y = input("[?] Exit? (Y/n): ")
		if y in ["Y","y"]:
			run("killall -9 com.termux")
		else:
			sys.exit("Thanks This Tool\033[0m")
	elif p == "7" or p == "07":
		run("python Tools/homemux/main.py")
