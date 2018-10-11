# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class MeijuItem(scrapy.Item):
    order = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
    plot = scrapy.Field()
    time = scrapy.Field()

