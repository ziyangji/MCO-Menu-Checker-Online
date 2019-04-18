import sys
import json

from lxml import html
from datetime import datetime
import requests
from Public.assets.Python.to_json import to_dict


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

        # current date
        date = int(str(datetime.today()).split()[0].split('-')[-1])

        breakfast = get_dish_and_cal('breakfast', tree, date)
        lunch = get_dish_and_cal('lunch', tree, date)
        dinner = get_dish_and_cal('dinner', tree, date)

        return breakfast, lunch, dinner


def get_dish_and_cal(time, e_tree, date):
    dishes = clean_up(e_tree.xpath('./body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{0:d}-day"]/div[@class="accordion"]/div[contains(@class, "{1}")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[@class="col-xs-9"]/a[contains(@class, "get-nutritioncalculator")]/text()'.format(date, time)))
    cals = clean_up(e_tree.xpath('./body/div[@class="my-app"]/div/div[@class="bottom-half"]/div[@class="main-content"]/div[@id="bite-menu"]/div[@id="menuid-{0:d}-day"]/div[@class="accordion"]/div[contains(@class, "{1}")]/div[contains(@class, "accordion-panel")]/div[@class="bite-menu-item"]/div[contains(@class, "text-right")]/a/text()'.format(date, time))[1:])
    return dishes, cals


def to_html(name, cal, tp, src="http://placehold.it/700x400", description=""):
	html = \
	"""
	<div class="block {0}-block">
			<div class="row">
	          <div class="col-lg-4 col-md-6 mb-4">
	            <div class="card h-100">
	              <a href="#"><img class="card-img-top" src="{1}" alt=""></a>
	              <div class="card-body">
	                <h4 class="card-title">
	                  <a href="#">{2}</a>
	                </h4>
	                <h5>{3}</h5>
	                <p class="card-text">{4}</p>
	              </div>
	              <div class="card-footer">
	                <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small>
	              </div>
	            </div>
	          </div>
	        </div>
    	</div>
	"""
	return html.format(tp, src, name, cal, description)


def clean_up(vals):
    # if type(vals) != type(list()):
    #     raise RuntimeError(f'clean up: Expected list, but was {type(vals)}')

    result = list()
    for item in vals:
        # if type(vals) != type(str()):
        #     raise RuntimeError(f'clean up: entries inside vals are not string. Was {type(item)}')
        result.append(str(item).replace('\r', '').strip())

    return result


# driver function
def fetch_all(name):
    result = Crawler(name).crawl()
    return to_dict(result[0][0], result[0][1]), to_dict(result[1][0], result[1][1]), to_dict(result[2][0], result[2][1])


if __name__ == '__main__':
    pass
