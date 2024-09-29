import requests, sys
from bs4 import BeautifulSoup
from one_book import scrap_one_book
from category import send_list_books


def create_csv_1_book():
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

# Creating a file for writing all the books of the category
def create_csv_books_category():
    with open('books_category.csv', 'w') as category_file:
        category_file.write("Url"+','+'UPC'+','+'Title'+','+'Price including tax'+','
            +'Price excluding tax'+','+'Category'+','+'Review rating'+','+'Image Url \n')
        # Using loop to select all the books
        for book_obj in send_list_books():
            category_file.write(
            f"{book_obj['url']}" + ','+
            book_obj['upc']+','+
            book_obj['title']+','+
            book_obj['price_including_tax']+','+
            book_obj['price_excluding_tax']+','+
            book_obj['category']+','+
            book_obj['review_rating']+','+
            book_obj['image_url']+'\n'
        )