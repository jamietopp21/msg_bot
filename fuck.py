import requests
import random
import json

base_url = 'https://www.foaas.com/'

fucks = [
    'back',
    'bday',
    'blackadder',
    'bus',
    'chainsaw',
    'cocksplat',
    'dalton',
    'deraadt',
    'donut',
    'equity',
    'fts',
    'gfy',
    'ing',
    'keep',
    'king',
    'linus',
    'look',
    'madison',
    'nugget',
    'off',
    'outside',
    'problem',
    'shakespeare',
    'shutup',
    'think',
    'thinking',
    'thumbs',
    'xmas',
    'yoda',
    'you',
]

def get_fuck(name):
    url = f'{base_url}{random.choice(fucks)}/{name}/life'
    print(url)

    head = {'Accept':'application/json'}
    r = json.loads(requests.get(url,headers=head).text)
    return(r['message'])