
import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
 
 version1：
url  = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15288&locationId=76929015&whereami=http://rensselaerdining.com/dining-near-me/blitman-dining-hall'
headers = {'User-Agent': ''}
response = requests.get(url, headers=headers)  # 使用headers避免访问受限
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('img')
folder_path = './photo/'
if os.path.exists(folder_path) == False:  # 判断文件夹是否已经存在
    os.makedirs(folder_path)  # 创建文件夹
 
for index,item in enumerate(items):
	if item:		
		html = requests.get(item.get('src'))   # get函数获取图片链接地址，requests发送访问请求
		img_name = folder_path + str(index + 1) +'.png'
		with open(img_name, 'wb') as file:  # 以byte形式将图片数据写入
			file.write(html.content)
			file.flush()
		file.close()  # 关闭文件
		time.sleep(1)  # 自定义延时

