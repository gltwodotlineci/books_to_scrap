import requests, sys
from bs4 import BeautifulSoup
from one_book import scrap_one_book

dt_1_book = scrap_one_book()


with open('book.csv', 'w') as file:
    file.write(
        "Url"+','+'UPC'+','+'Title'+','+'Price including tax'+','
        +'Price excluding tax'+','+'Category'+','+'Review rating'+','+'Image Url \n'
        f"{dt_1_book['url']}" + ','+
        dt_1_book['upc']+','+
        dt_1_book['title']+','+
        dt_1_book['price_including_tax']+','+
        dt_1_book['price_excluding_tax']+','+
        dt_1_book['category']+','+
        dt_1_book['review_rating']+','+
        dt_1_book['image_url']
    )
