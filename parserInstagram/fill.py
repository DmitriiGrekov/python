import time
import csv
import subprocess
import json
from pprint import pprint
with open('folowers.json','r') as f:
    folowers = json.load(f)


command_template = """curl 'https://www.instagram.com/{username}/?__a=1' \
          -H 'authority: www.instagram.com' \
            -H 'pragma: no-cache' \
              -H 'cache-control: no-cache' \
                -H 'accept: */*' \
                  -H 'x-ig-www-claim: hmac.AR3DP01PqAa_73kG7bqF8stdbg6zrqvkmO8fDDh76tsNFSq6' \
                    -H 'x-requested-with: XMLHttpRequest' \
                      -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36' \
                        -H 'x-ig-app-id: 936619743392459' \
                          -H 'sec-fetch-site: same-origin' \
                            -H 'sec-fetch-mode: cors' \
                              -H 'sec-fetch-dest: empty' \
                                -H 'referer: https://www.instagram.com/maksik_112/' \
                                  -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
                                    -H 'cookie: ig_did=C18E35C1-0FFB-4C57-9D1C-36E2710CB158; mid=XqKjKAAEAAEsN3VeXg-AJmf8c9Re; csrftoken=IBGvlVNhQhQGEakWYOug5D5kDDEojiBO; shbid=18929; shbts=1587717119.6038847; ds_user_id=6262583327; sessionid=6262583327%3AejGgV16mElZDdF%3A8; rur=FTW; urlgen="{{\"62.133.188.81\": 28812}}:1jRufl:NkWgRoGDhPqLsugog4lblm7koHc"' \
                                      --compressed > temp.json"""
followers_filles = []
for key,value in folowers.items():
    user = {}
    subprocess.run(command_template.format(username = value['username']),shell = True, capture_output = True)
    with open('temp.json','r') as f:
        data = json.load(f)
    user['follows'] = data['graphql']['user']['edge_follow']['count']
    user['username'] = value['username']
    user['biography'] = data['graphql']['user']['biography']
    user['full_name'] = data['graphql']['user']['full_name']

    followers_filles.append(user)
    print('Очередная итерация')
    time.sleep(5)


with open('folowers.csv','w') as f:
    print("Заполняем файл")
    writer = csv.writer(f)
    writer.writerows(['Биография','Подписчики','Имя','Username'])

    for v in followers_filles:
        writer.writerows([v['biography'],v['follows'],v['full_name'],v['username']])
