import random
import urllib
from urllib import urlopen

from bs4 import BeautifulSoup as soup


def news():
    client = urlopen("https://book.douban.com/?utm_source=weibolife")
    html_page = client.read()
    client.close()
    content = soup(html_page, "html")
    images = content.findAll("img")
    for image in images:
        print(image.get('alt'))
        print(image.get('src'))
        image_name = image.get('alt')
        if image_name is None:
            image_name = random.random() * 10
        image_url = image.get('src')
        urllib.urlretrieve(image_url, "/opt/python/%2s.jpg"%image_name)
        print("-" * 150)


if __name__ == '__main__':
    news()
