# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class E15Pipeline(object):
    def process_item(self, item, spider):
        print("--"*12)
        return item

class MeijuPipeline(object):
    def __init__(self):
        self.file = open('meiju.json','a',encoding='utf-8')

    def process_item(self,item,spider):
        txt = json.dumps(dict(item),ensure_ascii=False) + "\n"
        self.file.write(txt)
        return item

    def close_spider(self):
        self.file.close()