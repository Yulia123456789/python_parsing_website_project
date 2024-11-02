from requests import Session
from bs4 import BeautifulSoup
from time import sleep


headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'}

work = Session()

work.get('https://quotes.toscrape.com', headers=headers)

response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form').find('input').get('value')

data = {"csrf_token" : token, "username" : "noname", "password" : "password"}

result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True) #разрешает перенаправление на другую станицу код 302

