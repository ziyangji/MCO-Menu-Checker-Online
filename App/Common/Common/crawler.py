import sys
import json

from selenium import webdriver
from bs4 import BeautifulSoup


class Crawler:
	''' 
	The crawler class used for retrieving information from sodexo's menu page
	Note:
		Blitman Commons is not yet included in sodexo's page. The class should throw an error if blm is at request

	Attributes:
		url (str): link to the corresponding menu page of the target dinning hall
	'''

	def __init__(self, target):
		if target.lower() == 'cms':
			self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rensselaerdining.com/dining-near-me/commons-dining-hall'
		elif target.lower() == 'sage':
			self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rensselaerdining.com/dining-near-me/russell-sage'
		elif target.lower() == 'barh':
			self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=667&locationId=76929003&whereami=http://rensselaerdining.com/dining-near-me/barh-dining-hall'
		elif target.lower() == 'blm':
			raise ValueError(f'Blitman Commons is currently not on Sodexo\'s official website')
		else:
			raise ValueError(f'Target dinning hall ({target}) is not valid')

		self.target = target
		self.driver = webdriver.Chrome()

	def crawl(self):
		'''
		The crawler function that uses the webdriver to go to the website, and use bs4 to fecth information
		'''

		self.driver.get(self.url)       # Goto the menu page
		html = self.driver.page_source  # get page source
		soup = BeautifulSoup(html)      # parse page source html with bs4
		b = list()  # breakfast dishes
		l = list()  # lunch dishes
		d = list()  # dinner dishes

		# Breakfast
		breakfast = soup.find_all('div', class_="accordion-block breakfast open")  # find the breakfast div
		breakfast_dishes = breakfast.children
		for item in breakfast_dishes:
			temp = item.attrs['class']  # temp is a dict that stores the class names of dish
			if temp.find('accordion-panel') != -1 and temp.find('rtf') != -1 and temp.find('hide') != -1:  # get the actual menu div
				for bite_menu_item in item.children:
					


		pass  # TODO: finish this thing

