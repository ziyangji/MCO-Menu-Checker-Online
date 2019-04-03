import sys
import json
import requests
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
        self.dining_hall = {}
        self.currentwindow = ""
        self.currentitem = ""
        self.itemindicator = ""
        self.unknownstring = ""
        self.haveagreatday = 0
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
        # elif target.lower() == 'blm':
        #     self.url = ''  # blitman commons is currently not on RPI's official menu
        else:
            raise ValueError('Target dinning hall ({target}) is not valid')
        self.target = target
        self.driver = webdriver.Chrome()

    def getMeal(self, meal, text):
        self.unknownstring = ""
        # window or item
        if self.itemindicator == 0:
            #Skip the HAVE A GREAT DAY window
            if text == "HAVE A GREAT DAY!":
                self.haveagreatday = 1
                return
            elif self.haveagreatday == 1:
                self.haveagreatday = 0
                return

            #Normal windows
            if self.unknownstring == "":
                self.unknownstring = text
                return
            else:
                if text[0].isdigit():
                    self.currentitem = self.unknownstring
                    cal = text
                    self.dining_hall[self.currentwindow].append((self.currentitem, cal))
                else:
                    self.currentwindow = self.unknownstring
                    self.currentitem = text
                    self.itemindicator = 1

        # itemcal
        elif self.itemindicator == 1:
            currentcal = text
            self.dining_hall[self.currentitem] = [meal, self.currentwindow, currentcal]
            self.itemindicator = 0


    def crawl(self):
        r = requests.get(self.url)
        html = r.text.encode(r.encoding).decode()
        soup = BeautifulSoup(html, 'html.parser')

        # Raises:
        #   raise RuntimeError if there is no data for the target dinning hall
        # Returns:
        #   Packed json file with information from the target dinning hall
        mealindicator = -1

        for element in soup.find_all("div"):
            text = element.get_text().strip()

            if text == "BREAKFAST":
                if mealindicator == 2:
                    return
                mealindicator = 0
                continue

            if text == "LUNCH":
                mealindicator = 1
                continue

            if text == "DINNER":
                mealindicator = 2
                continue

            if mealindicator == 0:
                self.getMeal("BREAKFAST", text)
            elif mealindicator == 1:
                self.getMeal("LUNCH", text)
            elif mealindicator == 2:
                self.getMeal("DINNER", text)

if __name__ == '__main__':
    cms = Fetcher("cms")
    cms.crawl()
    sage = Fetcher("cms")
    sage.crawl()
    barh = Fetcher("cms")
    barh.crawl()


        # Load the data that PHP sent us
        # try:
        #   data = json.loads(sys.argv[1])
        # except:
        #   print("ERROR")
        #   sys.exit(1)
        #
        # Generate some data to send to PHP
        # result = {'res': '', 'menu': '', 'img': ''}
        #
        # Send it to stdout (to PHP)
        # print(json.dumps(result))


