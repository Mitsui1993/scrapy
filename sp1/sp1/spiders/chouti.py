# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.http.cookies import CookieJar

class ChoutiSpider(scrapy.Spider):
    #爬虫名称，必须
    name = 'chouti'
    #允许的url范围
    allowed_domains = ['chouti.com']
    #起始url
    start_urls = ['http://dig.chouti.com/']
    #维护请求cookies
    cookie_dict = {}

    def start_requests(self):
        """
        根据继承的类源码，自定制自己的起始函数，如没有此函数则用
        继承类默认的函数，本质就是生成一个生成器，next生成器做操作
        :return:Request()
        """
        for url in self.start_urls:
            yield Request(url,dont_filter=True,callback=self.login)

    def login(self, response):
        """
        获取响应页面发来的cookies,分析登录请求，获取所需数据进行登录
        :param response: 首页内容
        :return:
        """

        #获取cookie
        cookie_jar = CookieJar()
        cookie_jar.extract_cookies(response,response.request)
        for k,v in cookie_jar._cookies.items():
            for i,j in v.items():
                for m,n in j.items():
                    self.cookie_dict[m] = n.value

        #登录需要的post数据
        post_data = {
            'phone':'861767712xxxx',
            'password':'xxxx',
            'oneMonth':1,
        }
        import urllib.parse

        yield Request(
            url="http://dig.chouti.com/login",
            method='POST',
            cookies=self.cookie_dict,
            #将字典转化成k1=v1&k2=v2的格式，放在请求头中
            body=urllib.parse.urlencode(post_data),
            headers={'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'},
            callback=self.show
        )

    def show(self,response):
        """
        登录成功，获取新闻列表
        :return:
        """
        yield Request(url='http://dig.chouti.com/',cookies=self.cookie_dict,callback=self.find_tag)

    def find_tag(self,response):
        """
        分析每一个页面取到点赞id，发送POST请求对每一个页面的文章进行点赞
        :return:
        """
        hxs = Selector(response=response)
        link_id_list = hxs.xpath('//div[@class="part2"]/@share-linkid').extract()
        print(link_id_list)
        for link_id in link_id_list:
            #获取首页所有文章ID点赞
            link_url = 'http://dig.chouti.com/link/vote?linksId=%s' % link_id
            yield Request(url=link_url,method="POST",cookies=self.cookie_dict,callback=self.show_res)

        #获取其它分页的文章点赞
        page_list = hxs.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        print(1)
        for page in page_list:
            page_url = "http://dig.chouti.com%s" % (page,)
            #将每一页结果重新交给这个函数，递归的执行每一页的点赞
            yield Request(url=page_url,method='GET',callback=self.find_tag)

    def show_res(self,response):
        """
        显示点赞结果
        :param response:
        :return:
        """
        print(response.text)




