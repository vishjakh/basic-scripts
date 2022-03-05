import requests
import string



inputs=list(string.printable)
url=input("Enter complete url( Eg. http://abc.com?s= ) :  ")
id_to_check=input("Input '#Element ID' to check in response : ")

with open(url+":::fuzz.txt",'w',encoding = 'utf-8') as f:
	for inp in inputs:
		req=requests.get(url+inp)
		soup=BeautifulSoup(req.text)
		#print(inp+"    =>    "+soup.find(id=id_to_check).string)
		f.write(inp+"    =>    "+soup.find(id=id_to_check).string)
	f.close()