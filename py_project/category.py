import requests
from bs4 import BeautifulSoup

# geting all the books urls
url_category = "http://books.toscrape.com/catalogue/category/books/romance_8/index.html"
request_url_main = requests.get(url_category)

bs_category = BeautifulSoup(request_url_main.text, 'html.parser')
check_next = bs_category.find_all('li', class_='next')
print("check next 1 if OK§ ", len(check_next))
hrefs = bs_category.find_all('h3')
all_urls = []
base_url = "http://books.toscrape.com/catalogue"
for href in hrefs:
    all_urls.append(base_url + href.select('a')[0].get('href')[8:])

# for url in all_urls:
#     resp = requests.get(url)
#     bs = BeautifulSoup(resp.text, 'html.parser').find('body')
#     title = bs.find('h1').text
#     print("Title: ", title)

resp = requests.get(all_urls[5])
bs = BeautifulSoup(resp.text, 'html.parser').find('body')
title = bs.find('h1').text
print("Title: ", title)
