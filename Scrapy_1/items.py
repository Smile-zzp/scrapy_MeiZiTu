# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    url_1 = scrapy.Field()
    url_3 = scrapy.Field()
    img_url = scrapy.Field()
    img_num = scrapy.Field()
    img_path = scrapy.Field()
