from bs4 import BeautifulSoup


def parse_html(fh):
    garbage = ('Y\nYouTube', 'Männlich', 'Weiblich')
    set_categories = set()
    with open(fh, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        categories = soup.find('ul')
        for cat in categories.find_all('li'):
            if cat.text.strip() not in garbage:
                set_categories.add(cat.text.strip())
    return set_categories


if __name__ == '__main__':
    print(parse_html('Einstellungen für Werbung2.html'))
