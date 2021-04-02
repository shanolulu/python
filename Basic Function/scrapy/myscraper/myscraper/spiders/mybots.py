# -*- coding: utf-8 -*-


import scrapy
from myscraper.items import MyscraperItem

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['naver.com']
    start_urls = ["https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001"]

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[2]/a/text()').extract() # dt[2] 는 고정값이기 떄문에 [2]를 지워주지 않음
        authors = response.css('.writing::text').extract()
        previews = response.css('.lede::text').extract()

        items = []
        for idx in range(len(titles)):
            item = MyscraperItem()
            item['title'] = titles[idx]
            item['author'] = authors[idx]
            item['preview'] = previews[idx]
            items.append(item)
        return items