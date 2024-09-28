import requests
from bs4 import BeautifulSoup
import re

url = "https://books.toscrape.com/index.html"

response = requests.get(url)
if response:
    bs_ul = BeautifulSoup(response.text, 'html.parser')
    nav_list = bs_ul.find('ul', class_='nav nav-list').ul
    
    list_categ = []
    for li in nav_list:
        l = re.sub(r'\n\s*\n', r'\n\n', li.get_text().strip(), flags=re.M)
        if l != '':
            list_categ.append(l.lower())

print(list_categ)
