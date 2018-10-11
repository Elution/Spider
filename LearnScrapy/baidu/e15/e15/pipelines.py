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
    def process_item(self,item,spider):
        with open('meiju.json','a',encoding='utf-8') as f:
            json.dump(dict(item),f,ensure_ascii=False)
        print(type(item))
        print(item['name'])
        print(item['order'])
        print("--"*15)
        return item