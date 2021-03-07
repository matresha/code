import urllib.request
import requests
import json

url_pritchi = 'https://aerostatica.ru/2018/01/07/660-pritchi/'


def main():
    url = 'https://aerostatica.ru'
    with open("aero.txt", "w") as fout:
        for page in range(2, 69):
            resp = urllib.request.urlopen(url).read().decode()
            count_blocks = 10
            if page == 68:
                count_blocks = 3
            i = 0
            while count_blocks > 0:
                ind = resp[i:].find('headline') + i   
                ind = resp[ind:].find('href=') + ind  
                number = resp[ind + 18 : ind + 21]     
                ind_begOfName = resp[ind:].find('">') + ind + 2
                ind_endOfName = resp[ind_begOfName:].find('</a>') + ind_begOfName - 1
                Name = resp[ind_begOfName : ind_endOfName].strip()
                Name = Name.replace('&amp;', '&')
                Name = Name.replace('&quot;', '"')
                Name = Name.replace('&quot;', '"')
                Name = Name.replace('&#39;', "'")
                i = ind_endOfName
                count_blocks -= 1
                print(number, Name, file = fout)

            url = 'https://aerostatica.ru/page/' + str(page) + '/'
             

if __name__ == '__main__':
    main()