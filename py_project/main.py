import sys, csv
from one_book import scrap_one_book
from category import create_category_data


# Function that will be used to create a csv doc in order of the
def create_csv(name_csv,list_books):
    # creating field names from keys
    field_names = [x for x in list_books[0]]

    with open(f'{name_csv}.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for book_obj in list_books:
            writer.writerow(book_obj)


# downloading images of one book or different categories
# faire deux fonctions séparé (download livre & download image)
def download_image_book(category_or_one_book):
    one = 0 if len(category_or_one_book) == 1 else 1
    for i, book_img in enumerate(category_or_one_book):
        with open(f"img_book_{i+one}.jpg",'wb') as img:
            img.write(book_img.content)



# Creating csv file data of one book or download
# the image of one book
def csv_or_img_1_book(url,image=None):
    if not image:
        create_csv('book', [scrap_one_book(url)])
    else:
        download_image_book([scrap_one_book(url, True)])
        

# Creating csv file or images for one choosed category
def category_csv_or_images(image=None):
    print("If you want to select all the books press a")
    all = input("if not press anything else: ")
    if all == 'a' or all == 'A':
        all_books, name = True, 'all_books'
    else:
        all_books, name = False, "books_category"

    if not image:
        create_csv(name, create_category_data(False))
    else:
        download_image_book(create_category_data(True))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        func_name = sys.argv[1]
        globals()[func_name]()
    elif len(sys.argv) == 3:
        func_name = sys.argv[1]
        param1 = sys.argv[2]
        globals()[func_name](param1)
    elif len(sys.argv) == 4:
        func_name = sys.argv[1]
        param1 = sys.argv[2]
        param2 = sys.argv[3]
        globals()[func_name](param1,param2)
    else:
        sys.exit("Error, please start over!")
