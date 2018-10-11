from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from lxml import etree

class Douban_Reader():
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\shenhua_mabiao\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver")

    def get_pages_frombaidu(self,url,keys):
        option = Options()
        self.driver.get(url)#http://www.baidu.com
        self.driver.find_element_by_id("kw").send_keys(keys)#豆瓣读书
        self.driver.find_element_by_id("su").send_keys(Keys.RETURN)
        time.sleep(1.5)

    def get_main_page(self):
        url = self.driver.find_elements_by_xpath("//div[@id='content_left']/div[contains(@class,'result') and @id='1']")[0].find_elements_by_xpath(".//h3/a")[0].get_attribute("href")
        self.driver.get(url)
        time.sleep(3)

    def get_douban_reader(self):
        self.driver.find_element_by_id("inp-query").send_keys("Python")
        self.driver.find_element_by_class_name("inp-btn").click()
        time.sleep(1)
        self.driver.save_screenshot("douban.png")
        with open("douban.html","w",encoding="utf-8") as f:
            f.write(self.driver.page_source)
        self.driver.quit()

    def get_resource(self):
        text = ""
        with open("douban.html","r",encoding="utf-8") as f:
            text = f.read()
        tree = etree.HTML(text)
        books = tree.xpath("//div[@class='item-root']")
        for book in books:
            name = book.xpath(".//div[@class='detail']/div[@class='title']/a/text()")
            rating_nums = book.xpath(".//div[@class='detail']/div[@class='rating sc-bwzfXH hxNRHc']/span[@class='rating_nums']/text()")
            author = book.xpath(".//div[@class='detail']/div[@class='meta abstract']/text()")
            print("书名：",name[0])
            print("评分：",rating_nums[0])
            print("作者：",author[0])

if __name__ == '__main__':
    douban = Douban_Reader()
    douban.get_pages_frombaidu("http://www.baidu.com","豆瓣读书")
    douban.get_main_page()
    douban.get_douban_reader()
    douban.get_resource()
