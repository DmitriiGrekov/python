from random import choice
import requests
from bs4 import BeautifulSoup



class Proxy:
    proxy_list=[]

    def __init__(self):
        r = requests.get('https://www.ip-adress.com/proxy-list')

        bs = BeautifulSoup(r.text,'html.parser')

        table = bs.find('table',{'class':'htable proxylist'})

        tr = table.findAll('tr')

        for i in tr:
            td = i.findAll('td')
            for j in range(len(td)):
                if j==0:
                    self.proxy_list.append(td[j].get_text())
   


    def get_proxy(self):
        for i in self.proxy_list:
            url = 'http://'+i
            try:
                r  = requests.get('https://yandex.ru/',proxies = {'http':url})

                if r.status_code==200:
                    return url
            except:
                continue










def get_html(url,useragent=None,proxy=None):
    ua = choice(useragent)
    user = {'User-Agent':ua}

    r = requests.get('http://sitespy.ru/my-ip',headers = user,proxies = {'http':proxy})
    print(r.text)
    return r.text





def get_ip(html):
    bs = BeautifulSoup(html,'html.parser')

    ip = bs.find('span',{'class':'ip'}).get_text()

    ua = bs.find('span',{'style':'font-size: 20px;'}).get_text()

    print(ip)
    print(ua)





if __name__ =='__main__':
    proxy = Proxy()
    proxy = proxy.get_proxy()
    print(proxy)

    user_agent = open('useragents.txt').read().split('\n')
    html = get_html('http://sitespy.ru/my-ip',user_agent,proxy)
    print(html)
    get_ip(html)
    

















