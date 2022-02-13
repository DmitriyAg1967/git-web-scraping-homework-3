import requests
import bs4

HEADERS = {
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'If-None-Match': 'W/"37433-+qZyNZhUgblOQJvD5vdmtE4BN6w"',
    'accept-language': 'ru-RU,ru;q=0.9',
    'sec-ch-ua-mobile': '?0'
}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'

HUBS = ['дизайн', 'фото', 'web', 'python','Системное администрирование *','Финансы в IT','Биотехнологии']

response = requests.get(url, headers=HEADERS)
response.raise_for_status()
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for hub in hubs:
        #print(hub)
        if hub in HUBS:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            title = article.find('h2').find('span').text
            data = article.find(class_='tm-article-snippet__datetime-published').find('time').text
            result = data +' '+ title + ' - '+ link
            print(result)
