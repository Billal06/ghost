import requests, os, sys, json
ip = sys.argv[1]
class Scan:
	def __init__(self):
		self.url = "https://billal.herokuapp.com/api/track?ip="+ip
		self.j = ""

	def track(self):
		r = requests.get(self.url)
		self.j = json.loads(r.text)

	def tampil(self):
		print (self.j)
		if self.j["status"] == "success":
			type = self.j["result"]["type"]
			country = self.j["result"]["country"]
			code = self.j["result"]["code"]
			cal = self.j["result"]["calling_code"]
			print ("\033[33;1m[√] TYPE: \033[32;1m"+str(type))
			print ("\033[33;1m[√] COUNTRY: \033[32;1m"+str(country))
			print ("\033[33;1m[√] COUNTRY CODE: \033[32;1m"+str(code))
			print ("\033[33;1m[√] CALLING CODE: \033[32;1m"+str(cal))
		else:
			print ("\033[31;1m[×] IP error");sys.exit()

s = Scan()
s.track()
s.tampil()
