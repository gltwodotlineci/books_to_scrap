import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/the-metamorphosis_409/index.html"
response_request_url = requests.get(url)
if response_request_url:
    bs_body = BeautifulSoup(response_request_url.text, 'html.parser').find('body')
    title = bs_body.find('h1').text
    print("Title: ", title)
    
    # After we checked that we have one table:
    table_prices = bs_body.find('table').find_all('tr')
    # print("UPC ", table_prices[0].td.text)
    # print("price_excluding_tax ", table_prices[2].td.text)
    # print("price_including_tax ", table_prices[3].td.text)
    # print("number_available ", table_prices[5].td.text)
    # print("review_rating ", table_prices[6].td.text)

    # Description:
    description = bs_body.find_all('p')[3].text
     
    # Category
    navbar = bs_body.find_all("ul")
    category = (navbar)[0].find_all('li')[2]
    categ_txt = category.text
    categ_url = category.a.get('href')
 
    # Image url:
    img_url = bs_body.find('img', alt=title).get('src')
