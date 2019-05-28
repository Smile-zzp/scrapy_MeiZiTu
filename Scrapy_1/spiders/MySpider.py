from Scrapy_1.items import Scrapy1Item
import scrapy
import re
import time
class scrapyMyspider(scrapy.Spider):
    name = "MySpider"
    def start_requests(self):
        # 主页面
        start_urls = ['https://www.mzitu.com/taiwan']
        for url in start_urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        item = Scrapy1Item()
        html_1 = response.text
        # urls是主页面中板块的链接
        urls = re.findall(r'''href="(.*?)" target="_blank"><img class='lazy''', html_1)
        for i in range(0, len(urls)):
            item['url_1'] = urls[i]
            yield scrapy.Request(item['url_1'], meta={'url_1': urls[i]}, callback=self.content_1)

    def content_1(self, response):
        item = Scrapy1Item()
        html_2 = response.text
        url_2 = response.meta['url_1']
        # 获取每组图片的总翻页数量，num
        num = re.findall(r''+str(url_2)+'/(\d\d)', html_2)
        if len(num)>0:
            for i in range(1,int(num[0])+1):
                # 构造每组图片其余的图片的url
                url_3 = url_2 + "/" + str(i)
                item['url_3'] = url_3
                yield scrapy.Request(item['url_3'],  callback=self.content_2)

    def content_2(self, response):
        # 得到每张图片的url
        item = Scrapy1Item()
        html_3 = response.text
        img_url = re.findall(r'''img src="(.*?)"''',html_3)
        item['img_url'] = img_url[0]
        yield item










