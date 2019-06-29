#! -*- coding:utf-8 -*-

import re
import requests
import pymongo
import pymysql
from multiprocessing import Pool

from lxml import etree


#捕获异常
from requests.exceptions import RequestException
# #请求html

def get_one_page(url):
    headers = {"user-agent":'my-app/0.0.1'}
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("单一页面有js渲染～")




if __name__ == '__main__':
    url = 'http://product.dangdang.com/27872466.html'
    html = get_one_page(url)
    print(html)



