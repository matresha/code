import requests
import csv
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)




url = 'https://www.avito.ru/moskva/telefony?p=1&q=apple'
html = get_html(url)
total_pages = get_total_pages(html)
num = 0
for page_num in range(1, total_pages // 25):
    url = 'https://www.avito.ru/moskva/telefony?p=' + str(page_num) + '&q=apple'
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
    for ad in ads:
        try:
            title = ad.find('div', class_='item_table-header').find('h3').text.strip()
        except:
            title = ''
        try:
            url = 'https://www.avito.ru' + ad.find('div', class_='item_table-header').find('h3').find('a').get('href')
        except:
            url = ''
        try:
            price = ad.find('div', class_='item_table-header').find('span', class_='price').get('content')
        except:
            price = ''

        if int(price) > 1000:
            num += 1
            data = {'num':num,
                'title':title,
                'price':price + 'RUB',
                'url':url}
            write_csv(data)
