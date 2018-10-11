from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree
from bs4 import BeautifulSoup as bs
import time
from urllib import request


def save_file(filename,driver):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(driver.page_source)

def baidu(driver):
    '''通过selenium搜索自如网首页，并保存'''
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("自如")
    driver.find_element_by_id("su").click()
    time.sleep(3)
    filename = "BaiDu_Zroom.html"
    save_file(filename,driver)
    return filename

def get_url(filename):
    '''获取响应网址'''
    url = ""
    if filename == "BaiDu_Zroom.html":
        f = open(filename,'r',encoding="utf-8")
        soup = bs(f,"lxml")
        content_left_divs = soup.select("div#wrapper_wrapper")[0].select("div#container")[0].select("div#content_left")
        divs = content_left_divs[0].contents[1]
        links = divs.select("a[target='_blank']")
        url = links[0].get("href")
        f.close()
        # driver.close()
        return url
    elif filename == "Zroom_main.html":
        f = open(filename,'r',encoding="utf-8")
        soup = bs(f,'lxml')
        # li = soup.select("div#sub-header")[0].select("ul#topRightList")[0].contents[3]
        li = soup.select("div#sub-header")[0].select("ul#topRightList")[0].select("li#ziroom_login")[0].contents[0]
        url = li.get("href")
        return url


def getZroom(driver,url):
    '''通过selenium链接至响应网址，并将响应页面保存'''
    driver.get(url)
    filename = "Zroom_main.html"
    save_file(filename,driver)
    return filename

def zroom_getcookies(driver):
    return driver.get_cookies()

def passZroom(driver,url):
    '''自动登陆，并获取cookie'''
    driver.get(url)
    driver.find_element_by_id("user_name").send_keys("18334703779")
    driver.find_element_by_id("user_pas").send_keys("mb27270188")
    time.sleep(3)
    driver.find_element_by_id("login_button").click()
    time.sleep(3)
    cookies_list = zroom_getcookies(driver)
    cookie ={}
    for cookies in cookies_list:
        cookie[cookies["name"]] = cookies["value"]
    return cookie


if __name__ == '__main__':
    driver = webdriver.Chrome(r"C:\Users\shenhua_mabiao\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    filename_baidu = baidu(driver)
    zroom_url = get_url(filename_baidu)
    filename_zroom = getZroom(driver,zroom_url)
    zroom_pass_url = get_url(filename_zroom)
    cookie = passZroom(driver,zroom_pass_url)




    driver.quit()