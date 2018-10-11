# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        score = float(item['score'])
        if score > 9:
            print(item['name'])
        else:
            print("*********************该片不足9.0***********************")
        return item
