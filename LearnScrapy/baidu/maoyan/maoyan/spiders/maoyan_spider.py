import scrapy
from maoyan.items import MaoyanItem

class maoyan_spider(scrapy.Spider):
    name = "maoyan"

    start_urls = ["http://maoyan.com/board/4"]
    #quotes to scrape
    def parse(self, response):
        movies = response.xpath("//dl[@class='board-wrapper']/dd")
        for movie in movies:
            Item = MaoyanItem()
            # print(type(movie))
            # print(movie.xpath("//div[@class='movie-item-info']").xpath('string(.)').extract()[0])
            Item["order"] = movie.xpath(".//i/text()").extract_first()
            Item["name"] = movie.xpath(".//div[@class='movie-item-info']/p[@class='name']/a/text()").extract_first()
            Item["star"] = movie.xpath(".//div[@class='movie-item-info']/p[@class='star']/text()").extract_first().strip()
            Item["releasetime"] = movie.xpath(".//div[@class='movie-item-info']/p[@class='releasetime']/text()").extract_first()
            inte = movie.xpath(".//div[contains(@class,'movie-item-number')]/p[@class='score']//i[@class='integer']/text()").extract_first()
            point = movie.xpath(".//div[contains(@class,'movie-item-number')]/p[@class='score']//i[@class='fraction']/text()").extract_first()
            Item["score"] = str(inte) + str(point)
            yield Item

        next = response.xpath("//ul[@class='list-pager']/li[@class='active']/following-sibling::li[1]/a/@href").extract_first()
        print(next)
        url = response.urljoin(next)
        print(str(url))
        yield scrapy.Request(url = url,callback = self.parse)
