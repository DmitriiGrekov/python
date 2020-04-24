import json
import glob
from pprint import pprint

files = glob.glob('json/*.json')
folowers = {}
for f in files:
    with open(f,'r') as f:
        data = json.load(f)
        for user in data['data']['user']['edge_followed_by']['edges']:
            folowers[user['node']['id']]={
                    'id':user['node']['id'],
                    'username':user['node']['username'],
                    'full_name':user['node']['full_name'],
                    'followed_by_viewer':user['node']['followed_by_viewer']

                    }


with open('folowers.json','w') as f:
    json.dump(folowers,f)                
