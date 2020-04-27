import requests
from bs4 import BeautifulSoup

URL ='https://hh.ru/search/vacancy?clusters=true&area=113&enable_snippets=true&salary=&st=searchVacancy&text=Python+junior&from=suggest_post' 


def get_html(url):
    r = requests.get(url).text
    return r



    
if __name__ == '__main__':
    html = get_html(URL)
