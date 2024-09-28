import requests
from bs4 import BeautifulSoup
import re

def send_category_list():
        
    url = "https://books.toscrape.com/index.html"

    response = requests.get(url)
    if response:
        bs_ul = BeautifulSoup(response.text, 'html.parser')
        nav_list = bs_ul.find('ul', class_='nav nav-list').ul.find_all('a')
        
        categ_dict = {}
        for i,ls in enumerate(nav_list):
            l = re.sub(r'\n\s*\n', r'\n\n', ls.get_text().strip(), flags=re.M)
            categ_dict[i+1] = l#.lower().replace(' ','-') + f"_{i+1}"

    
        return categ_dict
    
    return f"Error, please check if there is something wrong with your url! "



    