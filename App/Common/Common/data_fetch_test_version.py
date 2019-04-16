
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
 
 version1：
url  = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15288&locationId=76929015&whereami=http://rensselaerdining.com/dining-near-me/blitman-dining-hall'
headers = {'User-Agent': ''}
response = requests.get(url, headers=headers)  
#use headers to make sure the webpage is still accessible
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('img')
folder_path = './photo/'
if os.path.exists(folder_path) == False:  
	#figure out whether the folder is already there
    os.makedirs(folder_path)  
# create folder
 
for index,item in enumerate(items):
	if item:		
		html = requests.get(item.get('src'))  
		# get the address of the picture
		img_name = folder_path + str(index + 1) +'.png'
		with open(img_name, 'wb') as file:  
			# save in bytes
			file.write(html.content)
			file.flush()
		file.close()  
		# close file
		
//
version 2:
import re
import requests



def dowmloadPic(html,keyword):


    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    for each in pic_url:
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print 'Unable to download'
            continue
        string = 'pictures\\'+keyword+'_'+str(i) + '.jpg'
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    word = raw_input("Input key word: ")
    url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15288&locationId=76929015&whereami=http://rensselaerdining.com/dining-near-me/blitman-dining-hall'
    result = requests.get(url)
    dowmloadPic(result.text,word)//
