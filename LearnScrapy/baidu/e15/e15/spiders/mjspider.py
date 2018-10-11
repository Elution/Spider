import scrapy
import time
from e15.items import MeijuItem
import json

class MeijuSpider(scrapy.Spider):
    start_urls = ["http://www.meijutt.com/new100.html"]
    name = "meiju"
    def parse(self, response):

        movies = response.xpath("//ul[@class='top-list  fn-clear']/li")
        for movie in movies:
            item = MeijuItem()
            item['name'] = movie.xpath(".//h5/a/text()").extract()
            item['order'] = movie.xpath(".//div[@class='lasted-num fn-left']/i/text()").extract()
            item['status'] = movie.xpath(".//span[@class='state1 new100state1']/font/text()").extract()
            item['plot'] = movie.xpath(".//span[@class='mjjq']/text()").extract()
            item['time'] = movie.xpath(".//div[@class='lasted-time new100time fn-right']/text()").extract()
            yield item