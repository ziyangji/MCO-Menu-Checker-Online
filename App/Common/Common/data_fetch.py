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
        self.unknownstring = ""
        self.haveagreatday = 0
        self.StringOrLetter = false
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

    def getMeal(self, meal, text, target):
        # itemindicator == 0 means window or an item
        if self.StringOrLetter == true:

            #Skip the HAVE A GREAT DAY
            if text == "HAVE A GREAT DAY!":
                self.haveagreatday = 1
                return
            elif self.haveagreatday == 1:
                self.haveagreatday = 0
                return

            #window or an item
            self.unknownstring = text
            if text[0].isdigit() != true:
                self.StringOrLetter = false
                self.currentwindow = self.unknownstring
                self.currentitem = text
                return

            else:
                self.currentitem = self.unknownstring
                self.dining_hall[self.currentitem] = [meal, self.currentwindow, text, target]
                return
        else:
            self.currentitem = self.unknownstring
            self.dining_hall[self.currentitem] = [meal, self.currentwindow, text, target]
            self.StringOrLetter = true
            return



    def crawl(self, target):
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
                self.getMeal("BREAKFAST", text, target)
            elif mealindicator == 1:
                self.getMeal("LUNCH", text, target)
            elif mealindicator == 2:
                self.getMeal("DINNER", text, target)
            print(self.dining_hall)

if __name__ == '__main__':
    cms = Fetcher("cms")
    cms.crawl("cms")
    #sage = Fetcher("sage")
    #sage.crawl("sage")
    #barh = Fetcher("barh")
    #barh.crawl("barh")


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


