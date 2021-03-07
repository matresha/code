import re
import math
import requests
from bs4 import BeautifulSoup
from lxml import html

"""Данная программа читает код со страниц сайтов 
Farfetch.com и tsum.ru и считает среднюю стоимость толстовки."""

# Farfetch
# sweatshirts
linkPart1 = 'https://www.farfetch.com/ru/shopping/men/sweaters-knitwear-2/items.aspx?page='
linkPart2 = '&view=180&category=136397'
farfetchSweatshirtsCountPrice = 0
farfetchSweatshirtsCountItems = 0
for num in range(1, 21):
   url = linkPart1 + str(num) + linkPart2
   html = requests.get(url).text
   soup = BeautifulSoup(html, 'lxml')
   text = soup.find_all('script')[5].text.strip()
   priceList = re.findall(r'("unitSalePrice":)(.*?)\,', text, flags = re.I)
   itemsNumber = len(priceList)
   farfetchSweatshirtsCountItems += itemsNumber
   for i in range(itemsNumber):
      itemPrice = int(priceList[i][1].split('.')[0])
      farfetchSweatshirtsCountPrice += itemPrice
farfetchSweatshirtsAveragePrice = round(farfetchSweatshirtsCountPrice / farfetchSweatshirtsCountItems)
print(farfetchSweatshirtsCountItems, farfetchSweatshirtsCountPrice, farfetchSweatshirtsAveragePrice)

#hoodies
linkPart1 = 'https://www.farfetch.com/ru/shopping/men/sweaters-knitwear-2/items.aspx?page='
linkPart2 = '&view=180&category=136398'
farfetchHoodiesCountPrice = 0
farfetchHoodiesCountItems = 0
for num in range(1, 16):
   url = linkPart1 + str(num) + linkPart2
   html = requests.get(url).text
   soup = BeautifulSoup(html, 'lxml')
   text = soup.find_all('script')[5].text.strip()
   priceList = re.findall(r'("unitSalePrice":)(.*?)\,', text, flags = re.I)
   itemsNumber = len(priceList)
   farfetchHoodiesCountItems += itemsNumber
   for i in range(itemsNumber):
      itemPrice = int(priceList[i][1].split('.')[0])
      farfetchHoodiesCountPrice += itemPrice
farfetchHoodiesAveragePrice = round(farfetchHoodiesCountPrice / farfetchHoodiesCountItems)
print(farfetchHoodiesCountItems, farfetchHoodiesCountPrice, farfetchHoodiesAveragePrice)


#TSUM
#All sweaters
# link = 'https://www.tsum.ru/catalog/svitery-2460/?page='
# tsumAllCountPrice = 0
# tsumAllCountItems = 0
# for num in range(1, 10):
#    url = link + str(num)
#    html = requests.get(url).text
#    data = BeautifulSoup(html, 'lxml').find_all('div', class_="product-list__item ng-star-inserted")
#    for elem in data:
#       text = elem.text[::-1]
#       itemPrice = int(str(re.search(r'[0-9]+\s[0-9]+', text).group(0)).replace("\xa0", "").strip()[::-1])
#       if itemPrice < 196000:
#          tsumAllCountItems += 1
#          tsumAllCountPrice += itemPrice
# tsumAllAveragePrice = round(tsumAllCountPrice / tsumAllCountItems)      
# print(tsumAllCountItems, tsumAllCountPrice, tsumAllAveragePrice)

#Cotton sweatshirts and hoodies
link = 'https://www.tsum.ru/catalog/svitery-2460/?page='
tsumCottonCountPrice = 0
tsumCottonCountItems = 0
for num in range(1, 10):
   url = link + str(num)
   html = requests.get(url).text
   data = BeautifulSoup(html, 'lxml').find_all('div', class_="product-list__item ng-star-inserted")
   for elem in data:
      text = elem.text
      hasCotton = re.search(r'Хлопк|хлопк', text)
      itemPrice = int(str(re.search(r'[0-9]+\s[0-9]+', text[::-1]).group(0)).replace("\xa0", "").strip()[::-1])
      if itemPrice < 196000 and hasCotton:
         tsumCottonCountItems += 1
         tsumCottonCountPrice += itemPrice
tsumCottonAveragePrice = round(tsumCottonCountPrice / tsumCottonCountItems)      
print(tsumCottonCountItems, tsumCottonCountPrice, tsumCottonAveragePrice)

vansAveragePrice = 4900

allAverage = farfetchHoodiesAveragePrice + farfetchSweatshirtsAveragePrice + tsumCottonAveragePrice +  vansAveragePrice
totalAveragePrice = round(allAverage / 4) 
print("Average cost: ", totalAveragePrice)

















