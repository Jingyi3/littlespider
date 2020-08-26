import scrapy
from bs4 import BeautifulSoup
import re


class SinaNewsSpider(scrapy.Spider):
    name = 'sina_news'  # spider name
    start_urls = [
        'https://news.sina.com.cn/'
    ]
    # where to scrap

    # jie xi scrapped content
    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')
        tags = soup.find_all('a', href=re.compile(r"sina.*\d{4}-\d{2}-\d{2}.*shtml$"))
        for tag in tags:
            print(tag.get('href'))
            print(tag.text)

        # print(response.url)
        # print(response.body)
