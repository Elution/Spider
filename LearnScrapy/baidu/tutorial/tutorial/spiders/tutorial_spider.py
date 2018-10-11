import scrapy
from tutorial.items import TutorialItem

class Tutorial_Spider(scrapy.Spider):
    name = "tutorial"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        divs = response.xpath("//div[@class='col-md-8']/div")
        for div in divs:
            item = TutorialItem()
            item['text'] = div.xpath(".//span[@class='text']/text()").extract_first()
            item['author'] = div.xpath(".//span/small[@class='author']/text()").extract_first()
            item['tags'] = div.xpath(".//div[@class='tags']/a/text()").extract()
            yield item
        next = response.xpath("//ul[@class='pager']/li[@class='next']/a/@href").extract_first()
        if next:
            url = response.urljoin(next)
            print('---'*12)
            print(str(url))
            print('###' * 12)
            yield scrapy.Request(url=url,callback=self.parse)
        else:
            print("--"*12)