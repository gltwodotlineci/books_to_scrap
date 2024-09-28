import requests
from bs4 import BeautifulSoup

# geting all the books urls
url_category = "http://books.toscrape.com/catalogue/category/books/mystery_3/"
category_url_list = [url_category + "index.html"]
request_url_main = requests.get(category_url_list[0])

bs_category = BeautifulSoup(request_url_main.text, 'html.parser')

def checking_next_pages(bs):
    try:
        return bs.find_all('li', class_='next')[0].a['href']
    except:
        return ''

next_pages = checking_next_pages(bs_category)
i = 1
while next_pages != '':
    # adding pages on the category
    category_url_list.append(url_category + next_pages)

    request_url_main = requests.get(category_url_list[i])
    next_pages = checking_next_pages(BeautifulSoup(request_url_main.text, 'html.parser'))

    i = i+1
    
print("Next page is: ", category_url_list)
print("Number of category pages: ", i)


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

resp = requests.get(all_urls[2])
bs = BeautifulSoup(resp.text, 'html.parser').find('body')
title = bs.find('h1').text
print("Title: ", title)
