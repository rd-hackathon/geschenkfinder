import sqlite3

import requests
from bs4 import BeautifulSoup
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache

sess = CacheControl(requests.Session(), cache=FileCache('relaxdays_cache'))  # wir wollen den Server ja nicht unnötig foltern
standard_url = 'https://relaxdays.de/catalogsearch/result/index/?q={}&product_list_dir=asc&product_list_order=sale_rank&product_list_limit=48'

db = sqlite3.connect("daten.db")
c = db.cursor()

working = []
broken = []


def get_items(category: str):
    url = standard_url.format(category)
    r = sess.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        warning = soup.find('div', {'class': 'message notice'})
        if warning is None:
            items_html = soup.find('ol', {'class': 'products list items product-items'}).find_all('li')
            c.execute('CREATE TABLE IF NOT EXISTS "{}" (id NUMERIC UNIQUE, name TEXT, price NUMERIC, url TEXT, image TEXT)'.format(category))
        else:
            print("{} hat eine Warning: {}".format(category, warning.text))
            broken.append(category)
            return
    except AttributeError:
        print("{} hat keine Einträge.".format(category))
        broken.append(category)
        return
    for x, item in enumerate(items_html):
        i = {
            'url': item.find('a', {'class': 'product-item-link'})['href'],
            'image': item.find('img')['src'],
            'name': item.find('a', {'class': 'product-item-link'}).text,
            'price': item.find('span', {'class': 'price'}).text.replace('\xa0€', '').replace(',', '.')
        }
        c.execute("INSERT INTO '{}' (id, name, price, url, image) VALUES (?, ?, ?, ?, ?);".format(category), (x, i['name'], str(i['price']), i['url'], i['image']))
    db.commit()
    working.append(category)


if __name__ == '__main__':
    with open('bereinigte_kategorien.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        print('Suche: {}'.format(l.strip()))
        get_items(l.strip())


    with open('broken.txt', 'w') as f:
        for cat in broken:
            f.write("%s\n" % cat)
    with open('working.txt', 'w') as f:
        for cat in working:
            f.write("%s\n" % cat)
    c.close()
