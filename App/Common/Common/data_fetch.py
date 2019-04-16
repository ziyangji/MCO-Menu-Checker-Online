import sys
import json

from lxml import html
import requests


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
            self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15465&locationId=76929001&whereami=http:' \
                       '//rensselaerdining.com/dining-near-me/commons-dining-hall'
        elif target.lower() == 'sage':
            self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=15285&locationId=76929002&whereami=http:' \
                       '//rensselaerdining.com/dining-near-me/russell-sage'
        elif target.lower() == 'barh':
            self.url = 'https://menus.sodexomyway.com/BiteMenu/Menu?menuId=667&locationId=76929003&whereami=http:' \
                       '//rensselaerdining.com/dining-near-me/barh-dining-hall'
        elif target.lower() == 'blm':
            raise ValueError(f'Blitman Commons is currently not on Sodexo\'s official website')
        else:
            raise ValueError(f'Target dinning hall ({target}) is not valid')

        self.target = target

    def crawl(self):
        '''
        The crawler function that uses request to get html source, and use lxml.html to build element tree
        '''
        tree = html.fromstring(requests.get(self.url).content)
        
        
        
        
        
        
        #这个是当天日期
        #current date
        date = 12
        
        
        
        
        
        
        
        # BREAKFAST:
        # use xpath to retrieve breakfast name
        breakfast_dishes = tree.xpath(
            './body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{:d}-day"]/div[@class="accordion"]/div[contains(@class, "breakfast")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[@class="col-xs-9"]/a[contains(@class, "get-nutritioncalculator")]/text()'.format(date))
        # use xpath to retrieve breakfast calories (the first cal data is invalid -> use slice to get rid of it)
        breakfast_cals = tree.xpath(
            './body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{:d}-day"]/div[@class="accordion"]/div[contains(@class, "breakfast")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[contains(@class, "text-right")]/a/text()'.format(date))[
                         1:]

        # TODO: same logic for lunch and dinner, implement them here
        # LUNCH:
        lunch_dishes = tree.xpath(
            './body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{:d}-day"]/div[@class="accordion"]/div[contains(@class, "lunch")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[@class="col-xs-9"]/a[contains(@class, "get-nutritioncalculator")]/text()'.format(date))
        # use xpath to retrieve breakfast calories (the first cal data is invalid -> use slice to get rid of it)
        lunch_cals = tree.xpath(
            './body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{:d}-day"]/div[@class="accordion"]/div[contains(@class, "lunch")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[contains(@class, "text-right")]/a/text()'.format(date))[
                         1:]

        # DINNER:
        dinner_dishes = tree.xpath(
            './body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{:d}-day"]/div[@class="accordion"]/div[contains(@class, "dinner")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[@class="col-xs-9"]/a[contains(@class, "get-nutritioncalculator")]/text()'.format(date))
        # use xpath to retrieve breakfast calories (the first cal data is invalid -> use slice to get rid of it)
        dinner_cals = tree.xpath(
            './body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{:d}-day"]/div[@class="accordion"]/div[contains(@class, "dinner")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[contains(@class, "text-right")]/a/text()'.format(date))[
                         1:]

        # TODO: pass data to php, print for debug uses

        # for d in breakfast_dishes:
        #   print(d, end='\t')
        # print()
        # for cal in breakfast_cals:
        #   print(cal, end='\t')
        # print()
        print(f'dish len: {len(breakfast_dishes)}')
        print(f'cal len: {len(breakfast_cals)}')
        i = 0
        while i < len(breakfast_dishes):
            print(f"{breakfast_dishes[i].strip()} -> {breakfast_cals[i].strip()}")
            i += 1

        print(f'dish len: {len(lunch_dishes)}')
        print(f'cal len: {len(lunch_cals)}')
        i = 0
        while i < len(lunch_dishes):
            print(f"{lunch_dishes[i].strip()} -> {lunch_cals[i].strip()}")
            i += 1

        print(f'dish len: {len(dinner_dishes)}')
        print(f'cal len: {len(dinner_cals)}')
        i = 0
        while i < len(dinner_dishes):
            print(f"{dinner_dishes[i].strip()} -> {dinner_cals[i].strip()}")
            i += 1



if __name__ == '__main__':
    test_ = Crawler('cms')
    test_.crawl()
# with open('test_cms.json', 'w', encoding='utf-8') as f:
#   f.write(test_.crawl())
