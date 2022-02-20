import csv
import requests
import lxml.html as html
from googletrans import Translator
translator = Translator()


#This script save important information about Korean films from a list in IDBM, with this information
#i'm going to have a Twitter bot that tweet a Korean film every day.
#I'm going to ignore movies that have a summary that's too long because tweets have a character limit 
TITLE_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                ")) and not(contains(.,"\n        ")) and not(contains(.," »\n"))]/../..//div[@class="ipl-rating-star small"]/../../h3[@class="lister-item-header"]/a/text()'
ABSTRACT_PATH  = '//div[@class="ipl-rating-star small"]/../..//p[@class="" and not(contains(.,"...                ")) and not(contains(.,"\n        ")) and not(contains(.," »\n"))]/text()'
YEAR_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                ")) and not(contains(.,"\n        ")) and not(contains(.," »\n"))]/../..//div[@class="ipl-rating-star small"]/../../h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]/text()'
STARS_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                ")) and not(contains(.,"\n        ")) and not(contains(.," »\n"))]/../div[@class="ipl-rating-widget"]/div[@class="ipl-rating-star small"]/span[@class="ipl-rating-star__rating"]/text()'
#'https://www.imdb.com/list/ls052519910/?sort=list_order,asc&st_dt=&mode=detail&page=n'
#This link takes you to the n list of movies. Every list had 100 movies. There are 19 list and 1983 movies.   »\n


def translation(some_list): 
    spanish_list = []
    for  element in some_list:
        result = translator.translate(element, src='en', dest='es')
        spanish_list.append(result.text)
    return spanish_list


def get_list_info(some_link):
    try :
        response = requests.get(some_link)
        if response.status_code == 200:
            temportal_list = []
            home = response.content.decode('utf-8')
            parsed = html.fromstring(home)  
            title_list = parsed.xpath(TITLE_PATH)
            year_list = parsed.xpath(YEAR_PATH)
            stars_list = parsed.xpath(STARS_PATH)
            abstract_list = translation(parsed.xpath(ABSTRACT_PATH))
            for iteration, element in enumerate(title_list):
                temporal_dic = {}
                temporal_dic = {
                    "name" : title_list[iteration], 
                    "year" : year_list[iteration],
                    "stars" : stars_list[iteration],
                    "abstract" : abstract_list[iteration]
                }
                temportal_list.append(temporal_dic)
            return temportal_list
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)
        

def get_movie_info(): 
    movies_info = []
    for n in range(1,20): 
        link = f'https://www.imdb.com/list/ls052519910/?sort=list_order,asc&st_dt=&mode=detail&page={n}'
        movies_info = movies_info + get_list_info(link)
    return movies_info


def run():
    movies_info = get_movie_info()
    keys = movies_info[0].keys()
    with open('korean_movies.csv', 'w', newline='', encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(movies_info)
    


if __name__ == "__main__":
    run()