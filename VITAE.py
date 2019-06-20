from json import dumps,loads
from requests import get
from subprocess import call
from os.path import abspath
from sys import platform,exit
class main:
    def __init__(self,ip,key):
	    self.ip = ip
		self.key = key
		self.plat = platform
	def load_API_KEY(self):
	    with open(self.key,"r") as out:
		    return out.read()
	def ejecute(self):
	    data = get("http://free.ipwhois.io/json/{}".format(self.ip))
		data.raise_for_status()
		ddata = loads(data)
        who = get("https://maps.googleapis.com/maps/api/geocode/json?",payload={"adress":ddata["city"],"bounds":"{a}|{b}".format(a=ddata["latitute"],b=ddata["longitute"]),"key":load_API_key()})
		who.raise_for_status()
		with open("data.tmp","w" as wr:
		    wr.write(who.text)
		if "win" in self.plat:
		    from webbrowser import open as op
			op(abspath("data.tmp"))
			exit()
		elif "linux" in self.plat:
		    call(["termux-open","--view",abspath("data.tmp")])
			exit()
def ecx
    with open("banner.txt","r") as ptf:
	    print(ptf.read())#API_GOOGLE
	ip = input("ip [publica]: ")
	key = input("ingrese la fila de la API_KEY")
	mks = main(ip,key)
exc()