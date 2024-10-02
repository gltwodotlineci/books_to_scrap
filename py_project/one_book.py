import requests, sys
from bs4 import BeautifulSoup


def scrap_one_book(given_url=None):
    
    if given_url is not None:
        url = given_url
    else:
        print("Entrez le lien de la page: ")
        url = input()

    try:
        response = requests.get(url)
    except Exception:
        sys.exit("Be carefull the domain name is wrong! Please restart from the begining.")


    while response.status_code != 200:
        print(" Please try again and check if your link has been copied correctly!")
        print(" Enter again your url here: ")
        url = input()
        try:
            response = requests.get(url)
        except Exception:
            sys.exit("Be carefull the domain name is wrong! Please restart from the begining.")

    # creating the dictionary
    page_dict = {'url': url,
                    'title':'',
                    'upc':'',
                    'price_including_tax':'',
                    'price_excluding_tax':'',
                    'category':'',
                    'review_rating':'',
                    'image_url':'',
                    'number_available':'',
                    'description':''
                    } 


    # Updating the new data to the dictionary
    bs_body = BeautifulSoup(response.text, 'html.parser').find('body')
    title = bs_body.find('h1').text
    table_prices = bs_body.find('table').find_all('tr')
    # Category
    bredcrumb = bs_body.find("ul")

    page_dict.update({'title':title,
                      'upc':table_prices[0].td.text,
                    'price_including_tax':table_prices[3].td.text[1:],
                    'price_excluding_tax':table_prices[2].td.text[1:],
                    'category':bredcrumb.find_all('li')[2].text.strip(),
                    'review_rating':table_prices[6].td.text,
                    'image_url':bs_body.find('img', alt=title).get('src'),
                    'number_available':table_prices[5].td.text,
                    'description':bs_body.find_all('p')[3].text
                })

    return page_dict
