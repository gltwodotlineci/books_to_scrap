import requests, sys, csv
from bs4 import BeautifulSoup
from  list_of_categories import send_category_list
from one_book import scrap_one_book
from pathlib import Path


def choose_category():
    '''
    choosing the category
    '''
    books_categ = send_category_list()
    print("Welcome to the category page. here you have the list of the categories that you can choose")
    print(f"You have the numbe of the category that you want to scrap")
    for i, book_categ in enumerate(books_categ):
        print(f"{i+1} -- {book_categ['Name Category']}")

    print("Choose the number of your category!")
    categ_nb = input()
    i = 1
    while not int(categ_nb) in range(0,51):
        if i > 2:
            sys.exit("Please start over")

        print("Please make sure your choice is between 1 to 50")
        categ_nb = input()
        i = i+1
    
    return categ_nb, books_categ[int(categ_nb)-1]


def send_category_url(not_choosed_category):

    folder_path = 'category'
    if not not_choosed_category:
        categ_lst = choose_category()
    else:
        categ_lst = not_choosed_category
        folder_path = 'all_categories'

    categ_nb = categ_lst[0]
    category_dictionary = categ_lst[1]

    type_cat = category_dictionary['Name Category'].lower().replace(' ','-')+ f"_{int(categ_nb)+1}"

    # geting all the books of a category urls
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

    return (category_url_list,
            category_dictionary['Name Category'],
            folder_path)


def create_category_data(all_categories=None):
    '''
    parsing from the categories page of the category
    '''
    base_url = "https://books.toscrape.com/catalogue"
    returned_categ = send_category_url(all_categories)

    field_names = []
    folder_path = returned_categ[2]
    name_csv = returned_categ[1] + '.csv'

    with open(Path('data',folder_path,name_csv), 'w', encoding='utf-8') as csv_file:

        for categ_url in returned_categ[0]:
            # first we will create a list with the pages of each category
            url_c = requests.get(categ_url)
            # we will sellect all the books url for each category page
            bs = BeautifulSoup(url_c.text, 'html.parser')

            # we will create a list of each book from each page of each category
            for href in bs.find_all('h3'):
                book_url = base_url + href.select('a')[0].get('href')[8:]
                scraped_book = scrap_one_book(book_url, folder_path)
                # Creating headers only if the field_name is void
                if field_names == []:
                    field_names = [x for x in scraped_book]
                    writer = csv.DictWriter(csv_file, fieldnames=field_names)
                    writer.writeheader()
                writer.writerow(scraped_book)
