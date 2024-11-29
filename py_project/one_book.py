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


def scrap_one_book(given_url, folder_path=None):
    '''
    Scraping the data of the choosen book
    '''
    url = given_url
    response = valid_response(given_url)

    i = 1
    while response.status_code != 200:
        print(" Please try again and check if your link has been copied correctly!")
        print(" Enter again your url here: ")
        url = input()
        response = valid_response(url)
        i += 1
        if i > 3:
            sys.exit("To many errors, please start from the begining")


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
                    'star_rating':''
                }

    # Updating the new data to the dictionary
    bs_body = BeautifulSoup(response.text, 'html.parser').find('body')
    title = bs_body.find('h1').text
    # Geting the raiting stars
    bs_star_rating = bs_body.find('div', class_="col-sm-6 product_main").find_all('p')[2]
    word_numbers ={'One':1,'Two':2,'Three':3, 'Four':4, 'Five':5}
    given_word_number = bs_star_rating.attrs['class'][1]
    star_rating = word_numbers.get(given_word_number)

    # updating the imge
    img_path = bs_body.find('img', alt=title).get('src')[5:]
    img_name = title.replace(' ','_').replace('/','-').lower()
    
    folder = "one_book"
    if folder_path:
        folder = folder_path
    with open(f"data/{folder}/images/{img_name}.jpg",'wb') as img:
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
                        'number_available':table_prices[5].td.text,
                        'star_rating':star_rating
                })

    return page_dict
