import scrapy

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    start_urls= ['http://www.baidu.com']
    # allow_domains = [""]
    def parse(self, response):
        print("----"*10)
        print(type(response))
        print("----"*10)
        with open("baidu.html","w",encoding="utf-8") as f:
            f.write(response.body.decode('utf-8'))