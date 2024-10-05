import requests
from bs4 import BeautifulSoup
import re

def send_category_list():
        
    url = "https://books.toscrape.com/index.html"

    response = requests.get(url)
    if response:
        bs_ul = BeautifulSoup(response.text, 'html.parser')
        nav_list = bs_ul.find('ul', class_='nav nav-list').ul.find_all('a')
        
        return [{"Name Category": ls.get_text().strip()} for ls in nav_list]
   
    return f"Error, please check if there is something wrong with your url! "



    