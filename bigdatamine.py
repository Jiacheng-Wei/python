
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    target = 'https://xkcd.com/1883/'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html,features="html.parser")
    img1 = bf.find_all('img',attrs={'title':True})
    for eachs in img1:
       print(eachs.attrs['title'])