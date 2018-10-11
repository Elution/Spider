from urllib import request
from http import cookiejar
from urllib import parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
cookies = cookiejar.CookieJar()
cookie_handlar = request.HTTPCookieProcessor(cookies)
http_handlar = request.HTTPHandler()
https_handlar = request.HTTPSHandler()
opener = request.build_opener(cookie_handlar,http_handlar,https_handlar)

def login():
    url = "https://security.kaixin001.com/login/login_post.php"
    data = {
        "loginemail":13119144223,
        "password":123456
    }
    data = parse.urlencode(data)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36"
    }
    req = request.Request(url,data=data.encode(),headers=headers)

    resp = opener.open(req)
    # print(resp.read().decode())

def check():
    url = "http://www.kaixin001.com"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36"
    }
    req = request.Request(url,headers=headers)
    resp = opener.open(req)
    print(resp.read().decode())

login()
check()

