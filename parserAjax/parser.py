import requests



r = requests.get('https://www.avito.ru/web/1/main/items?forceLocation=false&locationId=646240&lastStamp=1587405316588&limit=30&offset=120')
data = r.json()
item = data['items']
print(item[0])
