from urllib import request,parse,error
from http import cookiejar

file = "renren_cookie.txt"
# cookie = cookiejar.MozillaCookieJar(file)
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()
opener = request.build_opener(cookie_handler,http_handler,https_handler)

def login():
    url = "http://www.renren.com/PLogin.do"
    data ={
        "email":"1311914422",
        "password":"123456"
    }
    # headers = {
    #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #     "Accept-Language": "zh-CN,zh;q=0.9",
    #     "Cache-Control": "max-age=0",
    #     "Connection": "keep-alive",
    #     "Cookie": "anonymid=jkdffn9v-fc51l6; depovince=GW; jebecookies=2133e3f0-9820-44e1-a6f1-f7c78431d104|||||; _r01_=1; JSESSIONID=abcnPBOLP6rrHa4sE09tw; ick_login=1d0e3143-9c68-4ac1-86d4-5eba758ea103; jebe_key=41782589-f653-4485-8e69-4706ab700adc%7Ccfcd208495d565ef66e7dff9f98764da%7C1533266751744%7C0%7C1533266759134",
    #     "Host": "www.renren.com",
    #     "Referer": "https://www.baidu.com/link?url=xNRmB8xMZusyXJho0hTTpGDV0nWAsHYhr_wpWVZSpwK&wd=&eqid=df483c1b0000e8ac000000025b63c58d",
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36"
    # }
    data = parse.urlencode(data).encode()
    req = request.Request(url,data=data)
    resp = opener.open(req)
    # cookie.save(file)
    print(resp.read().decode())

def get_info():
    url = "http://www.renren.com/965187997/profile"
    # cookie = cookiejar.MozillaCookieJar()
    # cookie.load("renren_cookie.txt")
    # cookie_handler = request.HTTPCookieProcessor(cookie)
    # opener = request.build_opener(cookie_handler)
    req = request.Request(url)
    resp = opener.open(req)
    with open("renren.html","w",encoding="utf-8") as f:
        f.write(resp.read().decode())




if __name__ == '__main__':
    login()
    get_info()