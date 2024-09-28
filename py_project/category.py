import requests
from bs4 import BeautifulSoup
from  list_of_categories import send_category_list

books_categ = send_category_list()

print("Welcome to the category page. here you have the list of the categories that you can choose")
print(f"You have the numbe of the category that you want to scrap")
for i, book_categ in enumerate(books_categ):
    print(f"{i+1} -- {book_categ['Name Category']}")

print("Chouse the number of your category!")
cat_number = input()

type_cat = books_categ[int(cat_number)-1]['Name Category'].lower().replace(' ','-')+ f"_{int(cat_number)+1}"

# geting all the books urls
url_category = f"http://books.toscrape.com/catalogue/category/books/{type_cat}/"
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
