import requests, sys
from bs4 import BeautifulSoup as bs

data = []
url = sys.argv[1]
r = requests.get(url)
b = bs(r.text, "html.parser")
for a in b.findAll("input"):
	if "geturl" == a.get("name"):
		data.append(a.get("value"))

if len(data) > 0:
	print ("[RESULT]: "+data[0])
else:
	print ("[ERROR]: not found")
