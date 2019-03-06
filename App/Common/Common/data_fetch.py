import sys
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup


class Fetcher:
	''' The crawler class used for retrieving information from sodexo's menu page
	Note:
		Blitman Commons is not yet included in sodexo's page. The class should throw an error if blm is at request

	Attributes:
		url (str): link to the corresponding menu page of the target dinning hall
	'''

	def __init__(self, target):
		'''
		Args:
			target (str): Shortened name of the dinning hall

		Returns:
			None

		Raises:
			ValueError: If `target` is a not expected dinning hall name
		'''
		if target.lower() == 'cms':
			self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rensselaerdining.com/dining-near-me/commons-dining-hall'
		elif target.lower() == 'sage':
			self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http://rensselaerdining.com/dining-near-me/russell-sage'
		elif target.lower() == 'barh':
			self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=667&locationId=76929003&whereami=http://rensselaerdining.com/dining-near-me/barh-dining-hall'
		elif target.lower() == 'blm':
			self.url = ''  # blitman commons is currently not on RPI's official menu
		else:
			raise ValueError(f'Target dinning hall ({target}) is not valid')
		self.target = target
		self.driver = webdriver.Chrome()

	def crawl(self):
		'''
		Raises:
			raise RuntimeError if there is no data for the target dinning hall
		Returns:
			Packed json file with information from the target dinning hall
		'''
		
		# open url			
		self.driver.get(self.url)
		
		source_code = self.driver.find_element_by_xpath("//*").get_attribute("outerHTML")
		
		soup = BeautifulSoup(source_code, 'html.parser')
		
		self.menu = {
			"breakfast": null,
			"lunch": null,
			"dinner": null
		}		
		
		self.menu["breakfast"] = soup.find_all(class_="breakfast")
		self.menu["lunch"] = soup.find_all(class_="lunch")
		self.menu["dinner"] = soup.find_all(class_="dinner")
		
		# TODO: Structure out the data in self.menu and return
		pass


# Load the data that PHP sent us
try:
	data = json.loads(sys.argv[1])
except:
	print("ERROR")
	sys.exit(1)



# Generate some data to send to PHP
result = {'res': '', 'menu': '', 'img': ''}

# Send it to stdout (to PHP)
print(json.dumps(result))
