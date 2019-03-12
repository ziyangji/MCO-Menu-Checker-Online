
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
