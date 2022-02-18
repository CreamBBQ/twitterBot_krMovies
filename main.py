import requests
import lxml.html as html
import os
from googletrans import Translator
translator = Translator()


#I'm going to ignore movies that have a summary that's too long because tweets have a character limit 
TITLE_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/../h3[@class="lister-item-header"]/a/text()'
ABSTRACT_PATH  = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/text()'
YEAR_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/../h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]/text()'
STARS_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/../div[@class="ipl-rating-widget"]/div[@class="ipl-rating-star small"]/span[@class="ipl-rating-star__rating"]/text()'
page1 = 'https://www.imdb.com/list/ls052519910/?sort=list_order,asc&st_dt=&mode=detail&page=1'
#'https://www.imdb.com/list/ls052519910/?sort=list_order,asc&st_dt=&mode=detail&page=n'
#This link takes you to the n list of movies. Every list had 100 movies. There are 1833 list. 


def translation(some_list): 
    result = translator.translate(some_list, src='en', dest='es')
    spanish_list = []
    for trans in result: 
        spanish_list.append(trans.text)
    return spanish_list

def get_list_info(some_link):
    try :
        response = requests.get(some_link)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)  
            title_list = parsed.xpath(TITLE_PATH)
            abstract_list = parsed.xpath(ABSTRACT_PATH)
            year_list = parsed.xpath(YEAR_PATH)
            stars_list = parsed.xpath(STARS_PATH)
            for iteration, element in enumerate(title_list):
                print(title_list[iteration])
                print(year_list[iteration])
                print(stars_list[iteration])
                print(abstract_list[iteration])
                print("\n")
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    coso = translation(["hellow", "apple"])
    print(coso)


if __name__ == "__main__":
    run()