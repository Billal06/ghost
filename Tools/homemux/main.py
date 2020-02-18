import time, os, sys
def run(c):
	os.system(c)

print ("\033[32;1m[!] Remove Old")
time.sleep(2)
print ("[√] Success")
time.sleep(1)
print ("[!] Copying New Home")
run("cp Tools/homemux/bash.bashrc $HOME/../usr/etc")
print ("[√] Success")
time.sleep(2)
i = input("[?] Exit? (Y/n): ")
if i in ["Y","y"]:
	run("killall -9 com.termux")
else:
	sys.exit("Thanks To Using\033[0m")
