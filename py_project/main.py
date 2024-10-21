import csv, click
from one_book import scrap_one_book
from category import create_category_data
from list_of_categories import send_category_list
from pathlib import Path


def create_csv(name_csv,book):
    '''
    Function that will be used to create a csv doc in order of the
    '''
    # creating field names from keys
    field_names = [x for x in book]
    with open(f'data/one_book/{name_csv}.csv', 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(book)


# Creaing a click regroupment decorator for all the methods
@click.group()
def cli():
    pass


@cli.command()
@click.argument('url',nargs=1)
def one_book(url):
    '''
    Creating csv file data of one book or download
    the image of one book
    '''
    name_csv = Path(url).parts[3]
    create_csv(name_csv, scrap_one_book(url))


@cli.command()
def extract_category():
    '''
    Choosing one category and create csv file data
    from the choosen category
    '''
    create_category_data()


@cli.command()
def extract_all_categories():
    for i, categ in enumerate(send_category_list()):
        create_category_data((i+1,categ))


if __name__ == "__main__":
    cli()
