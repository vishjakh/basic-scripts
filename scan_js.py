import os,requests,re,uuid
from bs4 import BeautifulSoup

def get_links_js_files():

	for script in soup.find_all('script',{'src':True}):
		if '.js' in script['src']:
			linksArray.append(script['src'])


def download_js_files():
	js_path=''
	os.system('mkdir downloaded_js_files')
	for link in linksArray:
		try:
			r=requests.get('https:'+link,headers=headers)
			with open('downloaded_js_files/'+str(uuid.uuid4()),'w',encoding = 'utf-8') as f:
				f.write(r.text)
				f.close()
		except:
			try:
				print('https:'+url+link)
				r=requests.get(url+link,headers=headers)
				with open('downloaded_js_files/'+str(uuid.uuid4()),'w',encoding = 'utf-8') as f:
					f.write(r.text)
					f.close()
					pass
			except:
				print("error")

def search_files_for_links():
	print("Searching Files")
	urls=[]
	all_files=os.listdir('downloaded_js_files/')
	for file in all_files:
		
		with open('downloaded_js_files/'+file,'r',encoding = 'utf-8') as f:
			data=f.read()
			url=(re.findall(r'http?s:\/\/[\S]{1,15}\.'+domain+'\.[\w]{1,6}',data))
			urls.append(url)
			f.close()
	return urls

def filter_urls(urls):
	merge=[]
	for url in urls:
		merge+=url
	return list(dict.fromkeys(merge))


if __name__ == "__main__":
	
	url=input("Enter the url to scan(Eg. https://paytm.com): ")
	dom_reg=re.findall(r'://[\w]{1,12}.',url)
	domain=' '.join(dom_reg)[3:-1]
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	r= requests.get(url,headers=headers)
	resp=r.text
	soup=BeautifulSoup(resp,"html.parser")
	linksArray=[]
	get_links_js_files()
	print("Got Links")
	download_js_files()
	unfiltered_lists=search_files_for_links()
	print(filter_urls(unfiltered_lists))