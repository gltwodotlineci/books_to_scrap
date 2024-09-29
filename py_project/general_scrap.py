import requests
from bs4 import BeautifulSoup

url_general_list = ["https://books.toscrape.com/catalogue/"]
resp = requests.get(url_general_list[0]+'page-1.html')
bs_general = BeautifulSoup(resp.text, "html.parser")

def checking_next_pages(bs):
    try:
        return bs.find_all('li', class_='next')[0].a['href']
    except:
        return ''

next_pgs = checking_next_pages(bs_general)
i = 1
while next_pgs !='':
    url_general_list.append(url_general_list[0] + next_pgs )

    request_url_main = requests.get(url_general_list[i])
    next_pgs = checking_next_pages(BeautifulSoup(request_url_main.text, 'html.parser'))
    i = i+1


print("Number of category pages: ", i)
print("List of urls: ", url_general_list)
