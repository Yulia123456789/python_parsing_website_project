import requests
from bs4 import BeautifulSoup
from time import sleep


headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'}
def get_url():

    for count in range(1, 7):

        url = f'https://scrapingclub.com/exercise/list_basic/page={count}'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml') #lxml парсер кода

        data = soup.find_all('div', class_='w-full rounded border')



        for i in data:
            card_url = "https://scrapingclub.com" + i.find('a').get('href')
            yield card_url

def array():

    for card_url in get_url():

        response = requests.get(card_url, headers=headers)

        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml') #lxml парсер кода

        data = soup.find('div', class_='my-8 w-full rounded border')
        name = data.find('h3').text

        price = data.find('h4').text

        text = data.find('p').text

        url_img = "https://scrapingclub.com" + data.find("img").get("src")

        yield name, price, text, url_img