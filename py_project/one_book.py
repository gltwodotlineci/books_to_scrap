import requests, sys, csv
from bs4 import BeautifulSoup

def fix_encoding(str):
    '''
    Because of the meta charset of html, we might have a problem with accented
    characters. we will change it by using encoede ISO and decode utf
    '''
    return bytes(str, encoding="ISO-8859-1").decode('utf-8')


def valid_response(given_url):
    '''
    Validation of the url
      '''
    try:
        return requests.get(given_url)
    except Exception:
        sys.exit("Be carefull the domain name is wrong! Please restart from the begining.")

def scrap_one_book(given_url=None, category=False, all_categories=False):
    '''
    Scraping the data of the choosen book
    '''
    if given_url is not None:
        url = given_url
    else:
        print("Entrez le lien de la page: ")
        url = input()

    response = valid_response(url)

    while response.status_code != 200:
        print(" Please try again and check if your link has been copied correctly!")
        print(" Enter again your url here: ")
        url = input()
        response = valid_response(url)


    page_dict = {'url': url,
                    'title':'',
                    'upc':'',
                    'price_including_tax':'',
                    'price_excluding_tax':'',
                    'description':'',
                    'category':'',
                    'review_rating':'',
                    'image_url':'',
                    'number_available':'',
                    } 


    # Updating the new data to the dictionary
    bs_body = BeautifulSoup(response.text, 'html.parser').find('body')
    title = bs_body.find('h1').text

    # updating the imge
    img_path = bs_body.find('img', alt=title).get('src')[5:]
    img_name = title.replace(' ','_').replace('/','-').lower()
    folder = "one_book/"
    if category:
        folder ="category/"
    elif all_categories:
        folder = "all_categories/"
    with open(f"data/{folder}images/{img_name}.jpg",'wb') as img:
        book_img = requests.get('https://books.toscrape.com'+img_path)
        img.write(book_img.content)

    table_prices = bs_body.find('table').find_all('tr')
    # Category
    bredcrumb = bs_body.find("ul")

    page_dict.update({  'title':title,
                        'upc':table_prices[0].td.text,
                        'price_including_tax':fix_encoding(table_prices[3].td.text),
                        'price_excluding_tax':fix_encoding(table_prices[2].td.text),
                        'description':fix_encoding(bs_body.find_all('p')[3].text),
                        'category':bredcrumb.find_all('li')[2].text.strip(),
                        'review_rating':table_prices[6].td.text,
                        'image_url':bs_body.find('img', alt=title).get('src'),
                        'number_available':table_prices[5].td.text
                })


    return page_dict
