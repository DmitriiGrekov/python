import requests
from bs4 import BeautifulSoup

from random import choice






def get_html(url,useragent=None,proxy=None):
    pr= choice(proxy)

    prox = {
            'https':'85.10.219.102:1080',
            'http':'85.10.219.102:1080',

            }


    ua = choice(useragent)
    user = {'User-Agent':ua}

    r = requests.get('https://www.google.com/',headers = user,proxies = prox)
    print(r.text)
    return r.text





def get_ip(html):
    bs = BeautifulSoup(html,'html.parser')

    ip = bs.find('span',{'class':'ip'}).get_text()

    ua = bs.find('span',{'style':'font-size: 20px;'}).get_text()

    print(ip)
    print(ua)





if __name__ =='__main__':

    proxy  = open('proxy.txt','r').read().split('\n')
    user_agent = open('useragents.txt').read().split('\n')
    html = get_html('http://sitespy.ru/my-ip',user_agent,proxy)
    print(html)
    get_ip(html)
    

