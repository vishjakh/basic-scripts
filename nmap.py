#!/usr/bin/python

import sys , getopt , os


def main(argv):
	
	url=''
	try:
		opts,args =getopt.getopt(argv,"hu:")
	except getopt.GetoptError:
		print('nmap.py -u <url>')
		sys.exit(2)
	for opt,arg in opts:
		if opt=='-h':
			print('nmap.py -u <url>')
		elif opt in ("-u"):
			url=arg
	os.system('sudo nmap -sCV  -p- -T5 --min-parallelism 100 -sT -sU --min-rate=1000 --max-retries=2 '+url+' -Pn -oN '+url+':::nmapScan.txt')

if __name__ == "__main__":
   main(sys.argv[1:])