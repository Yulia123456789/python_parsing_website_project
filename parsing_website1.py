import requests
from bs4 import BeautifulSoup
from time import sleep


list_card_url = []
headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'}
for count in range(1, 2):
    sleep(3)
    url = f'https://scrapingclub.com/exercise/list_basic/page={count}'

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml') #lxml парсер кода

    data = soup.find_all('div', class_='w-full rounded border')

    # for i in data:
    #
    #     name = i.find('h4').text
    #
    #     price = i.find('h5').text
    #
    #     url_img = "https://scrapingclub.com" + i.find("img").get("src")
    #
    #     print(name.replace('\n', ''), price, url_img)

    for i in data:
        card_url = "https://scrapingclub.com" + i.find('a').get('href')
        list_card_url.append(card_url)


for card_url in list_card_url:

    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml') #lxml парсер кода

    data = soup.find('div', class_='my-8 w-full rounded border')
    name = data.find('h3').text

    price = data.find('h4').text

    text = data.find('p').text

    url_img = "https://scrapingclub.com" + data.find("img").get("src")

    print(name, price, text, url_img, sep='\n')
    print()