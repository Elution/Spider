from urllib import request,parse,error
import requests
from bs4 import BeautifulSoup as bs
from pyquery import PyQuery
import csv
url = "http://maoyan.com/board/4"

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Host": "analytics.meituan.com",
    "If-Modified-Since": "Thu, 19 Jul 2018 12:10:57 GMT",
    "Referer": "http://maoyan.com/board/4",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36"
}

proxies = {"http":"39.137.69.10:80",
    "https":"61.157.136.105:808",
    "http":"119.179.133.25:8060",
    "http":"121.8.98.196:80",
    "http":"61.136.163.245:8103"}


proxy_handler = request.ProxyHandler(proxies=proxies)
http_handler = request.HTTPHandler()
https_handlers = request.HTTPSHandler()
opener = request.build_opener(proxy_handler,http_handler,https_handlers)
request.install_opener(opener)
with open("../maoyan.csv","w",newline="") as f:
    csvobj = csv.writer(f)
    csvobj.writerow(["name", "person", "time", "point"])
    for i in range(10):
        offset = i*10
        fullurl = url + "?offset=" +str(offset)
        req = request.Request(fullurl,headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode()
        soup = bs(html,"lxml")
        dd = soup.select(".board-wrapper")[0].select("dd")
        for i in dd:
            p = i.select('p')
            img = i.select("img")
            attr = img[1].attrs['data-src']
            print(attr)
            name = p[0].select('a')[0].string.rstrip("\n")
            person = p[1].string.lstrip().rstrip("\n").strip(" ")
            time = p[2].string
            point = p[3].select('i')[0].string + p[3].select('i')[1].string
            csvobj.writerow([name,person,time,point])