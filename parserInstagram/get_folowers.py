import subprocess
import json
from pprint import pprint
import urllib.parse


url_base = 'https://www.instagram.com/graphql/query/?'

commands = """curl 'https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables=%7B%22id%22%3A%226262583327%22%2C%22include_reel%22%3Atrue%2C%22fetch_mutual%22%3Atrue%2C%22first%22%3A24%7D' \
          -H 'authority: www.instagram.com' \
            -H 'accept: */*' \
              -H 'x-ig-www-claim: hmac.AR3DP01PqAa_73kG7bqF8stdbg6zrqvkmO8fDDh76tsNFSq6' \
                -H 'x-requested-with: XMLHttpRequest' \
                  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36' \
                    -H 'x-csrftoken: IBGvlVNhQhQGEakWYOug5D5kDDEojiBO' \
                      -H 'x-ig-app-id: 936619743392459' \
                        -H 'sec-fetch-site: same-origin' \
                          -H 'sec-fetch-mode: cors' \
                            -H 'sec-fetch-dest: empty' \
                              -H 'referer: https://www.instagram.com/dmitr5555g/followers/' \
                                -H 'accept-language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
                                  -H 'cookie: ig_did=C18E35C1-0FFB-4C57-9D1C-36E2710CB158; mid=XqKjKAAEAAEsN3VeXg-AJmf8c9Re; csrftoken=IBGvlVNhQhQGEakWYOug5D5kDDEojiBO; shbid=18929; shbts=1587717119.6038847; ds_user_id=6262583327; sessionid=6262583327%3AejGgV16mElZDdF%3A8; rur=FTW; urlgen="{\"62.133.188.81\": 28812}:1jRtlL:9wEiDdDm7HoPBeDCy0pZ8u2AjwY"' \
                                    --compressed > json/folowers.json"""
index = 1

while True:
    
    result = subprocess.run(commands,shell=True,capture_output = True)
    if result.returncode !=0:
        exit("Произошла ошибка")
    with open('json/folowers.json','r') as f:
        data = json.load(f)

    pprint(data)
    exit()
