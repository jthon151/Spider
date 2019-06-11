#-*- coding:utf-8 -*-
# author:XL_Liu
# datetime:2019.06.04 下午 03:10
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
index_page = requests.get('http://www.xinshao.gov.cn/c1008/index.html')
index_page.encoding = ('utf-8')
print(index_page.text)
