# -*- coding:utf-8 -*-
# author:XL_Liu
# datetime:2019.05.30 下午 08:33
from selenium import webdriver
from scrapy.selector import Selector
import MySQLdb
import requests
from numpy import array

conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="root", db="baidu", charset="utf8")
cursor = conn.cursor()

def get_realurl(url):
    try:
        temp = requests.get(url.rstrip(), timeout=0.5)
    except Exception as e:
        return url
    return temp.url

def insert_baidu_xinshao(result):
    cursor.executemany("insert baidu_xinshao(url,title,time,content) VALUES(%s,%s,%s,%s)", (result))
    return conn.commit()

# 设置chromedriver不加载图片
chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_opt.add_experimental_option("prefs", prefs)
brower = webdriver.Chrome(executable_path=
                          r"C:\Users\刘鑫霖\AppData\Local\Programs"
                          r"\Python\Python36\chromedriver.exe", chrome_options=chrome_opt)

from time import sleep

brower.get('http://baidu.com/')
sleep(5)
brower.find_element_by_id('kw').send_keys('新邵扶贫')
sleep(1)
brower.find_element_by_id('su').click()
z =1
while True:
    try:
        print('{0}第{1}个页面爬取{0}'.format('-'*20,z))
        z+=1
        if z>126000:
            break
        sleep(2)
        page = Selector(text=brower.page_source)
        href1 = page.xpath('//*[@class="result c-container "]/h3/a/@href').extract()
        href = []
        for i in href1:
            href.append(get_realurl(i))
        title1 = page.xpath('//*[@class="result c-container "]/h3/a')
        title = []
        for i in title1:
            title.append(i.xpath('string(.)').extract_first())
        for i in range(len(title), len(href)):
            title.append('NULL')
        time = page.xpath('//*[@class="c-abstract"]/span/text()').extract()
        time = [str(i).replace('\xa0', '').replace('-', '') for i in time]
        for i in range(len(time), len(href)):
            time.append('NULL')

        bd_content1 = page.xpath('//*[@class="c-abstract"]')
        bd_content = []
        for i in bd_content1:
            bd_content.append(i.xpath('string(.)').extract_first().replace('\xa0', ''))

        for i in range(len(bd_content), len(href)):
            bd_content.append('NULL')

        try:
            brower.find_elements_by_id('page')[-1].click()
        except Exception as e:
            print(e)

        resule = []
        num_list = array([href, title, time, bd_content]).T
        for i in num_list:
            resule.append(tuple(i))
        insert_baidu_xinshao(result=resule)
    except Exception as e:
        print(e)
