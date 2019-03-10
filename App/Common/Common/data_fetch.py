import sys
import json
import urllib.request

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

    def __init__(self, target,breakfast,lunch,dinner):
        breakfast = {}
        lunch = {}
        dinner = {}
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

    def crawl(self,breakfast,lunch,dinner):

        # Raises:
        # 	raise RuntimeError if there is no data for the target dinning hall
        # Returns:
        # 	Packed json file with information from the target dinning hall

        currentitem = ""
        currentwindow = ""
        currentcal = ""
        temp = ""
        mealindicator = -1
        itemindicator = 0
        for element in soup.find_all("div"):
            text = element.get_text().strip()
            if text == "BREAKFAST":
                if mealindicator == 2:
                    return
                mealindicator = 0

            if text == "LUNCH":
                mealindicator = 1

            if text == "DINNER":
                mealindicator = 2

             #Breakfast
            if mealindicator == 0:
                #window or item
                if itemindicator == 0:
                    if temp == "":
                        temp = text
                    else:
                        if text[0].isdigit():
                            currentitem = temp
                            currentcal = text
                            breakfast[currentwindow].append((currentitem,currentcal))
                        else:
                            currentwindow = temp
                            currentitem = text
                            breakfast[currentwindow] = []
                            itemindicator = 1
                #itemcal
                elif itemindicator == 1:
                    currentcal = text
                    breakfast[currentwindow].append((currentitem, currentcal))
                    itemindicator = 0

            #Lunch
            elif mealindicator == 1:
                # window or item
                if itemindicator == 0:
                    if temp == "":
                        temp = text
                    else:
                        if text[0].isdigit():
                            currentitem = temp
                            currentcal = text
                            lunch[currentwindow].append((currentitem, currentcal))
                        else:
                            currentwindow = temp
                            currentitem = text
                            lunch[currentwindow] = []
                            itemindicator = 1
                # itemcal
                elif itemindicator == 1:
                    currentcal = text
                    lunch[currentwindow].append((currentitem, currentcal))
                    itemindicator = 0
            #Dinner
            elif mealindicator == 2:
                # window or item
                if itemindicator == 0:
                    if temp == "":
                        temp = text
                    else:
                        if text[0].isdigit():
                            currentitem = temp
                            currentcal = text
                            dinner[currentwindow].append((currentitem, currentcal))
                        else:
                            currentwindow = temp
                            currentitem = text
                            dinner[currentwindow] = []
                            itemindicator = 1
                # itemcal
                elif itemindicator == 1:
                    currentcal = text
                    dinner[currentwindow].append((currentitem, currentcal))
                    itemindicator = 0



if __name__ == '__main__':
    html = urllib.request.urlopen('https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http://rensselaerdining.com/dining-near-me/commons-dining-hall').read()
    soup = BeautifulSoup(html, 'html.parser')




        # Load the data that PHP sent us
        # try:
        # 	data = json.loads(sys.argv[1])
        # except:
        # 	print("ERROR")
        # 	sys.exit(1)

        # Generate some data to send to PHP
        # result = {'res': '', 'menu': '', 'img': ''}

        # Send it to stdout (to PHP)
        # print(json.dumps(result))


