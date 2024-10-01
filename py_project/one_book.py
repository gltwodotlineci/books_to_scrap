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

    page_dt_dict = {'url': url} # renomer le variable

    bs_body = BeautifulSoup(response.text, 'html.parser').find('body')
    page_dt_dict['title'] = bs_body.find('h1').text
    # Identify the table with prices, upc, rating, number avaible
    table_prices = bs_body.find('table').find_all('tr')
    page_dt_dict['upc'] = table_prices[0].td.text
    page_dt_dict['price_including_tax'] = table_prices[3].td.text
    page_dt_dict['price_excluding_tax'] = table_prices[2].td.text
    # Category
    navbar = bs_body.find("ul")
    category = navbar.find_all('li')[2].text
    page_dt_dict['category'] = category.replace('\n','')
    page_dt_dict['review_rating'] = table_prices[6].td.text
    img_url = bs_body.find('img', alt=page_dt_dict['title']).get('src')
    page_dt_dict['image_url'] = img_url
    page_dt_dict['number_available'] = table_prices[5].td.text
    page_dt_dict['description'] = bs_body.find_all('p')[3].text

    return page_dt_dict
