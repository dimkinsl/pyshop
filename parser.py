#! Python3
# Парсер сайта python.org выводящий в консоль STDOUT
# информацию о предстоящих событиях (Upcoming Events)

import requests
import sys
from bs4 import BeautifulSoup as bs

URL = 'https://python.org'

try:
    page = requests.get(URL)
    soup = bs(page.text, 'html.parser')
    events = soup.findAll(class_='medium-widget event-widget last')

    for name in events:
        tmp = name.get_text()
        count = 0
        # -------------------вывод через stdout--------------------
        for txt in tmp.split('\n'):
            if len(txt) > 0 and txt != str('More'):
                if count % 2 == 0:
                    sys.stdout.write(str(txt) + '\n')
                else:
                    sys.stdout.write(str(txt) + ' : ')
                count += 1

except:
    print('Page not found')








