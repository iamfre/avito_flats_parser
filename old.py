import requests
from bs4 import BeautifulSoup
import csv
import re

CSV = 'flats.csv'
HOST = 'https://www.avito.ru'
URL = 'https://www.avito.ru/moskva/kvartiry/sdam/na_dlitelnyy_srok/1-komnatnye-ASgBAQICAkSSA8gQ8AeQUgFAzAgUjlk'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='snippet-horizontal')
    flats = []

    for item in items:
        try:
            metro_station = item.find(
                'span', class_='item-address-georeferences-item__content').get_text(strip=True)
        except:
            metro_station = 'No metro station'
        try:
            address = item.find(
                'span', class_='item-address__string').get_text(strip=True)
        except:
            address = 'No address'
        flats.append(
            {
                'link': HOST + item.a.get('href'),
                'address': address,
                'price': item.find('meta', itemprop='price').get('content'),
                'date': item.find('div', class_='snippet-date-info').get_text(strip=True),
                'metro_station': metro_station
            }
        )
    return flats


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Ссыслка', 'Адрес', 'Цена', 'Дата', 'Метро'])
        for item in items:

            # разбиение строки
            txt = item['date']
            txt_split = re.split('\s+', txt)

            # поиск чисел
            time_number_regular = re.search('\d+', txt_split[0])
            time_number = time_number_regular.group()
            time_number = int(time_number)

            # поиск текста
            result = re.match(
                r'[минут][минут][минут][минут][минут]', txt_split[1])
            if result == None:
                result = 'not'
            else:
                time_find = result.group(0)

                if time_find != 'минут':
                    continue
                else:
                    if time_number < 59:
                        writer.writerow(
                            [item['link'], item['address'], item['price'], item['date'], item['metro_station']])


def parser():
    PAGENATION = 3
    # PAGENATION = input('Введите кол-во страниц для парсинга: ')
    # PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        flats = []
        for page in range(1, PAGENATION):
            print(f'Парсим страницу: {page}')
            html = get_html(URL, params={
                'p': page,
                'pmax': 30000,
                'pmin': 27000,
                'user': 1
            })
            flats.extend(get_content(html.text))
            save_doc(flats, CSV)
    else:
        print('Error')


parser()
