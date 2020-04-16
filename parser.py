import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup

URL = 'http://www.orenburg.ru/official/news/246/38173/%20/background/konkurs_sotsialnykh_videorolikov_vybiray_zhizn!/index.php?special=Y%26PAGEN_2%3D890'

HEADER = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36','accept':"*/*"}


site = 'http://www.orenburg.ru'

def get_html(url,params = None):
    r = requests.get(url,headers = HEADER,params = params  )
    return r.text



def get_pages(html):
    bs = BeautifulSoup(html,'html.parser')

    arr = bs.findAll('font',{'class':'text'})[-1]
    link = arr.findAll('a')[-1].get('href').split('=')[-1]
    return int(link) 


def get_content(html):
    bs = BeautifulSoup(html,'html.parser')
    lists = bs.findAll('div',{'class':"list"})[-1]
    items = lists.findAll('div',{'class':'item'})
    article = []
    for i in items[1:]:
        article.append({
            'title':i.find('div',{'class':'name'}).get_text(strip = True),
            'link':site+i.find('a').get('href'),
            'date':i.find('div',{'class':'date'}).get_text()
            })

    return article


ARTICLE = []
def make_all(page):
    print(f'Парсим страницу {page}')
    html = get_html(URL,params = {"PAGEN_2":page})
    ARTICLE.extend(get_content(html))



if __name__ =='__main__':
    html = get_html(URL)
    pages = get_pages(html)
    ARTICLES = []

    with Pool(2) as p:

        p.map(make_all,[i for i in range(1,pages+1)])

    print(len(ARTICLES))

