from one_book import scrap_one_book
from category import send_list_books
from all_books import send_all_books_scraped

# Function that will create the csv based on the case           
def create_csv(name_csv,list_books):
    with open(f'{name_csv}.csv', 'w') as category_file:
        category_file.write("Url"+','+'UPC'+','+'Title'+','+'Price including tax'+','
            +'Price excluding tax'+','+'Category'+','+'Review rating'+','+'Image Url \n')
        # Using loop to select all the books
        for book_obj in list_books:
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

# Creating csv for one book
# create_csv('book', [scrap_one_book()])

# Creating csv file for one category
create_csv('books_category', send_list_books())

# Creating csv file for all books
# create_csv('all_books', send_all_books_scraped())
