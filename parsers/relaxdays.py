from bs4 import BeautifulSoup
import requests
from cachecontrol import CacheControl
from cachecontrol.caches.file_cache import FileCache
import sys

sess = CacheControl(requests.Session(), cache=FileCache('relaxdays_cache'))  # wir wollen den Server ja nicht unnötig foltern
standard_url = 'https://relaxdays.de/catalogsearch/result/index/?q={}&product_list_dir=asc&product_list_order=sale_rank&product_list_limit=48'


def get_items(category: str):
    url = standard_url.format(category)
    r = sess.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    items_html = soup.find('ol', {'class': 'products list items product-items'}).find_all('li')
    #TODO: nothing here works
    print(items_html)
    items = []
    for item in items_html:
        print(item)
        sys.exit()
        i = {}
        i['category'] = ""
        i['url'] = ""
        i['image'] = ""
        i['name'] = ""
