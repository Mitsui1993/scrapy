# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Sp2Pipeline(object):
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        """

        :param item:  爬虫中yield回来的对象
        :param spider: 爬虫对象 obj = JianDanSpider()
        :return:
        """
        if spider.name == 'jiadnan':
            pass
        print(item)
        self.f.write('....')
        # 将item传递给下一个pipeline的process_item方法
        # return item
        # from scrapy.exceptions import DropItem
        # raise DropItem()  下一个pipeline的process_item方法不在执行

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.get('MMMM')
        print('执行pipeline的from_crawler，进行实例化对象')
        return cls()

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')
        self.f = open('a.log','a+')

    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.f.close()

class Sp3Pipeline(object):
    def __init__(self):
        self.f = None

    def process_item(self, item, spider):
        """

        :param item:  爬虫中yield回来的对象
        :param spider: 爬虫对象 obj = JianDanSpider()
        :return:
        """
        print(item)
        self.f.write('....')
        return item

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        # val = crawler.settings.get('MMMM')
        print('执行pipeline的from_crawler，进行实例化对象')
        return cls()

    def open_spider(self, spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        print('打开爬虫')
        self.f = open('a.log', 'a+')

    def close_spider(self, spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.f.close()













# class CustomPipeline(object):
#     def __init__(self,val):
#         self.val = val
#
#     def process_item(self, item, spider):
#         # 操作并进行持久化
#
#         # return表示会被后续的pipeline继续处理
#         return item
#
#         # 表示将item丢弃，不会被后续pipeline处理
#         # raise DropItem()
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         """
#         初始化时候，用于创建pipeline对象
#         :param crawler:
#         :return:
#         """
#         val = crawler.settings.get('MMMM')
#         return cls(val)
#
#     def open_spider(self,spider):
#         """
#         爬虫开始执行时，调用
#         :param spider:
#         :return:
#         """
#         print('000000')
#
#     def close_spider(self,spider):
#         """
#         爬虫关闭时，被调用
#         :param spider:
#         :return:
#         """
#         print('111111')

"""
检测 CustomPipeline类中是否有 from_crawler方法
如果有：
       obj = 类.from_crawler()
如果没有：
       obj = 类()
obj.open_spider()

while True:
    爬虫运行，并且执行parse各种各样的翻缸发，yield item
    obj.process_item()

obj.close_spider()    

"""