import requests
from bs4 import BeautifulSoup
from  list_of_categories import send_category_list
from one_book import scrap_one_book

books_categ = send_category_list()


print("Welcome to the category page. here you have the list of the categories that you can choose")
print(f"You have the numbe of the category that you want to scrap")
for i, book_categ in enumerate(books_categ):
    print(f"{i+1} -- {book_categ['Name Category']}")

print("Chouse the number of your category!")
cat_number = input()

def send_categories():
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

    return category_url_list


# parsing from the categories page of the category
def send_list_books():
    all_urls = []
    base_url = "http://books.toscrape.com/catalogue"
    for categ_url in send_categories():
        # first we will create a list with the pages of each category    
        url_c = requests.get(categ_url)
        # we will sellect all the books url for each category page
        bs = BeautifulSoup(url_c.text, 'html.parser')

        # we will create a list of each book from each page of each category
        for href in bs.find_all('h3'):
            all_urls.append(base_url + href.select('a')[0].get('href')[8:])

    list_books_category = []
    for url in all_urls:
        list_books_category.append(scrap_one_book(url))

    return list_books_category
