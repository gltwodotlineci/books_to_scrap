import requests
from bs4 import BeautifulSoup
from one_book import scrap_one_book

def send_all_books_scraped():
    url = "https://books.toscrape.com/catalogue/category/books_1/page-"
    base_url = "https://books.toscrape.com/catalogue"
    all_books_list = []
    # BeautifullSoup for all pages
    for i in range(1,51):
        response =requests.get(url+f"{i}.html")
        bs = BeautifulSoup(response.text, 'html.parser')

        # chooseng every book for each page
        for href in bs.find_all('h3'):
            url = base_url+href.select('a')[0].get('href')[5:]
            all_books_list.append(scrap_one_book(url))

    return all_books_list

