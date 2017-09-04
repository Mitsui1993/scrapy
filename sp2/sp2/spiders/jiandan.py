# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector

class JianDanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = ['jandan.net']
    start_urls = ['http://jandan.net/']

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True,callback=self.parse1)
    def parse1(self,response):
        # response.text 首页所有内容
        hxs = Selector(response)
        a_list = hxs.xpath('//div[@class="indexs"]/h2')
        for tag in a_list:
            url = tag.xpath('./a/@href').extract_first()
            text = tag.xpath('./a/text()').extract_first()
            from ..items import Sp2Item
            yield Sp2Item(url=url,text=text)
        # 获取页码 [url,url]
        """
        for url in url_list:
            yield Request(url=url,callback=self.parse1)
        """











