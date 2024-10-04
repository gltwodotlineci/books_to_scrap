import sys, csv
from one_book import scrap_one_book
from category import send_list_books
from all_books import send_all_books_scraped


# Function that will be used to create a csv doc in order of the
def create_csv(name_csv,list_books):
    # creating field names from keys
    field_names = [x for x in list_books[0].keys()]

    with open(f'{name_csv}.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for book_obj in list_books:
            writer.writerow(book_obj)


def validate_choice():
    print("Here are three cases of parsing the books and saving their data to a csv file:")
    print("  A --- Parsing one book")
    print("  B --- Parsing all the books of one category ")
    print("  C --- Parsing all the books of every category")
    print(" Please choose one of the cases A, B or C")
    abc = input()
    i = 1
    while not abc in ['A','B','C']:
        print(f"You choosed {abc}. Make sure your choice is A, B or C")
        i +=1
        abc = input()
        if i > 2:
            sys.exit("Too many errors please restart over again.")
    return abc

# downloading images of one book or different categories
def download_image_book(category_or_one_book):
    one = 0 if len(category_or_one_book) == 1 else 1
    for i, book_img in enumerate(category_or_one_book):
        with open(f"img_book_{i+one}.jpg",'wb') as img:
            img.write(book_img.content)

# download_image_book([scrap_one_book(None,True)])
# download_image_book(send_list_books(True))


def choosing_type_download():
    match validate_choice():
        case 'A':
            # Creating csv for one book
            create_csv('book', [scrap_one_book()])
        case 'B':
            # Creating csv file for one category
            create_csv('books_category', send_list_books())
        case 'C':
            # Creating csv file for all books
            create_csv('all_books', send_all_books_scraped())


choosing_type_download()
