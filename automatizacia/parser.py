import requests
import os
import wget
from bs4 import BeautifulSoup

URL = 'https://xkcd.com/'
def get_html(url):
    r = requests.get(url).text
    print('Парсим страницу',url)
    return r





def get_photo(html):
    print('Собираем данные со страницы')
    bs = BeautifulSoup(html,'html.parser')
    photo = bs.find('div',{'id':'comic'})
    link = photo.find('img').get('src')[7:]

    link  = 'https://'+link
    filename = wget.download(link)
    os.rename(filename,os.path.join('photo/',filename))
    

def get_prev(html):
    bs = BeautifulSoup(html,'html.parser')

    link = bs.findAll('a',{'rel':'prev'})[0].get('href')
    link = 'https://xkcd.com/'+ link[1:]
    return link
    

if __name__ =='__main__':
    for i in range(2297):
        if i == 0:
            URL =URL
        else:
             
            URL = get_prev(html)
        print(URL)
        html = get_html(URL)
        get_photo(html)
        

