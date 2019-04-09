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
        self.StringOrLetter = False
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
        #self.driver = webdriver.Chrome()

    def getMeal(self, meal, text, target):
        # 我们当前不知道这是一个window或者一个菜品
        # itemindicator == 0 means window or an item
        if self.StringOrLetter:

            #跳过两句废话
            #Skip the HAVE A GREAT DAY
            #第一句废话
            if text == "HAVE A GREAT DAY!":
                self.haveagreatday = 1
                return
            #第二句废话
            elif self.haveagreatday == 1:
                self.haveagreatday = 0
                return
            #存进一个string
            self.unknownstring = text
            
            #第二次到这里，发现上次的unknownstring是window名字，
            #那么这次的就是菜品了,那么下次一定是卡路里
            #这个操作判断是不是数字
            if text[0].isdigit() != True:
                self.StringOrLetter = False
                self.currentwindow = self.unknownstring
                self.currentitem = text
                return
            
            #第二次到这里，发现上次的是菜品，那么这次就是卡路里了
            else:
                self.currentitem = self.unknownstring
                self.dining_hall[self.currentitem] = [meal, self.currentwindow, text, target]
                return
            
        #如果上次一定是菜品，那么现在一定是卡路里
        else:
            self.currentitem = self.unknownstring
            self.dining_hall[self.currentitem] = [meal, self.currentwindow, text, target]
            self.StringOrLetter = True
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
            text.replace("\n","")

            if text == "\n" or text == "\r" or text == None or text == "":
                continue
                
            #我这里print了一天的所有数据
            
            if mealindicator!=-1:
                print(text)
                
            #他每一个BREAKFAST LUNCH DINNER下面都多了一个250cal，别的没什么
            #如果我们找到了早餐
            if text == "BREAKFAST":
                #如果我们到了第二天的早餐 停止
                if mealindicator == 2:
                    return
                mealindicator = 0
                continue
            #如果我们找到了午餐               
            if text == "LUNCH":
                mealindicator = 1
                continue
            #如果我们找到了晚餐
            if text == "DINNER":
                mealindicator = 2
                continue
            #早餐
            if mealindicator == 0:
                self.getMeal("BREAKFAST", text, target)
            #午餐
            elif mealindicator == 1:
                self.getMeal("LUNCH", text, target)
            #晚餐
            elif mealindicator == 2:
                self.getMeal("DINNER", text, target)
            #print(self.dining_hall)

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


