from urllib import request,parse,error
from http import cookiejar

def login():
    url = "http://passport.ziroom.com/api/index.php?r=user/login"
    data = {
        "phone":"18334703779",
        "password":"mb27270188",
        "imgVValue":"",
        "seven": 0
    }
    data = parse.urlencode(data).encode()
    headers ={
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3322.4 Safari/537.36"
    }
    f = r"ziru.txt"

    cookie = cookiejar.MozillaCookieJar(f)
    cookie_handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_handler)
    req = request.Request(url,data=data,headers=headers)
    try:
        rsp = opener.open(req)
        print(rsp.read().decode())
        cookie.save(f,ignore_discard=True,ignore_expires=True)
    except error.URLError as e:
        print(e)

def get_info():
    url = "http://i.ziroom.com/"
    f = r"ziru.txt"
    cookie = cookiejar.MozillaCookieJar()
    cookie.load(f)
    cookie_handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(cookie_handler)
    req = request.Request(url)
    rsp = opener.open(req)
    with open("ziru.html","w",encoding="utf-8") as x:
        x.write(rsp.read().decode())
    print(rsp.read().decode())

if __name__ == '__main__':
    login()