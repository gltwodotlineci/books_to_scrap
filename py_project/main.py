import sys, csv, click
from one_book import scrap_one_book
from category import create_category_data
from list_of_categories import send_category_list



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


# Creaing a click regroupment decorator for all the methods
@click.group()
def cli():
    pass


@cli.command()
@click.argument('url',nargs=1)
def onebook(url):
    '''
    Creating csv file data of one book or download
    the image of one book
    '''
    name_csv = url[37:-11]
    create_csv(name_csv, [scrap_one_book(url)])

@cli.command()
def createcategory():
    '''
    Choosing one category and create csv file data
    from the choosen category
    '''
    create_category_data()


@cli.command()
def allcategories():
    for i, categ in enumerate(send_category_list()):
        create_category_data((i+1,categ),False)



if __name__ == "__main__":
    cli()
