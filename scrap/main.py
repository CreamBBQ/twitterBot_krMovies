import requests
import lxml.html as html
import os

#I'm going to ignore movies that have a summary that's too long because tweets have a character limit 
TITLE_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/../h3[@class="lister-item-header"]/a/text()'
ABSTRACT_PATH  = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/text()'
YEAR_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/../h3[@class="lister-item-header"]/span[@class="lister-item-year text-muted unbold"]/text()'
STARS_PATH = '//div[@class="lister-item-content"]/p[@class="" and not(contains(.,"...                "))]/../div[@class="ipl-rating-widget"]/div[@class="ipl-rating-star small"]/span[@class="ipl-rating-star__rating"]/text()'

#'https://www.imdb.com/list/ls052519910/?sort=list_order,asc&st_dt=&mode=detail&page=n'
#This link takes you to the n list of movies. Every list had 100 movies. There are 1833 list. 


#$x('//div[@class="ipl-rating-star small"]/span[@class="ipl-rating-star__rating"]/text()').map(x => x.wholeText)