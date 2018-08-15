import requests
from bs4 import BeautifulSoup

def get_definition(word):
    def_req = requests.get(f'https://www.bing.com/search?q=define+{word}').text
    print(def_req[0:25])
    soup = BeautifulSoup(def_req,'lxml')
    print(soup.select_one('.dc_mn').text)
    return (soup.select_one('.dc_mn').text)