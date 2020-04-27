from bs4 import BeautifulSoup
import csv
from pprint import pprint
import requests
from user_agent import generate_user_agent
# generate a user agent

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.63 Safari/537.36'}
page_link='https://hh.ru/search/vacancy?clusters=true&area=113&enable_snippets=true&salary=&st=searchVacancy&text=python+developer'



def get_html(url,page=0):
    headers = {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}    
    r = requests.get(url,timeout=5,headers = headers,params={'page':page})


    return r.text


def get_page(html):
    bs = BeautifulSoup(html,'html.parser')

    link = bs.find('div',{'data-qa':'pager-block'}).find('span',{'class':'pager-item-not-in-short-range'}).find('a',{'class':'bloko-button HH-Pager-Control','data-qa':'pager-page'}).get('data-page')
    return int(link)

def get_content(html):
    bs = BeautifulSoup(html,'html.parser')
    vacancyes = bs.findAll('div',{'data-qa':'vacancy-serp__vacancy'})
    vacancy = []

    for vac in vacancyes:
        cost = vac.find('span',{'class':'bloko-section-header-3 bloko-section-header-3_lite','data-qa':'vacancy-serp__vacancy-compensation'})
        if cost==None:
            cost = 'Зарплата не указана'
        else:
            cost = cost.get_text(strip=True)
        vacancy.append({
            'title':vac.find('a',{'class':'bloko-link HH-LinkModifier','data-qa':'vacancy-serp__vacancy-title'}).get_text(strip=True),
            'link':vac.find('a',{'class':'bloko-link HH-LinkModifier','data-qa':'vacancy-serp__vacancy-title'}).get('href'),
            'cost':cost,
            'city':vac.find('span',{'class':'vacancy-serp-item__meta-info','data-qa':'vacancy-serp__vacancy-address'}).get_text(strip=True),
            'date':vac.find('span',{'class':'vacancy-serp-item__publication-date'}).get_text(strip=True),
            })


    return vacancy
    

def save_data(vac):
    with open('file.csv','w') as f:
        writer = csv.writer(f)
        writer.writerow(('Заголовок','Зарплата','Город','Дата','Ссылка'))
        for v in vac:
            writer.writerow((v['title'],v['cost'],v['city'],v['date'],v['link']))



if __name__ == '__main__':
    html = get_html(page_link)
    pages = get_page(html)
    vacancy = []
    print(pages)
    for i in range(pages):
        html = get_html(page_link,i)
        vacancy.extend(get_content(html))

    save_data(vacancy)


    print(len(vacancy))

