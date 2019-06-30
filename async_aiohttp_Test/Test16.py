

import datetime
import re
import time
import urllib.request


import re
import requests
import pymysql
from requests.exceptions import RequestException
from lxml import etree
import pymysql

from selenium import webdriver


def get_one_page(url):
    driver = webdriver.Chrome()

    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html




def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    try:

        for i in range(1,888):
            sql = 'select f_blink from Final_linkTable where id = %s ' % i
            # #执行sql语句
            cur.execute(sql)
            # #获取所有记录列表
            data = cur.fetchone()
            book_link = data['f_blink']
            yield book_link
    except :
        print("放过去")



def parse_page1(html):
    selector = etree.HTML(html)
    book_name = selector.xpath('//*[@id="ebooksProductTitle"]/text()')
    author = selector.xpath('//*[@id="buybox"]/div/table/tbody/tr[2]/td[2]/text()')
    r_book_name = remove_block(book_name)
    r_author = remove_block(author)



    book_name1 = if_isnull(r_book_name)
    author1 = if_isnull(r_author)
    return r_book_name,r_author
    # for i1,i2 in zip(book_name1,author1):




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items



def if_isnull(content):
    if_list =[]

    if  content ==None:
        f_content  = ''
        if_list.append(f_content)
    else:

        f_content =content
        if_list = f_content
    return if_list

test_list = ['https://www.amazon.cn/dp/B07K9MM446',
             'https://www.amazon.cn/dp/B07QYM82RQ',
             'https://www.amazon.cn/dp/B07SFTNKLS']

if __name__ == '__main__':

    # for url_str in Python_sel_Mysql():
    for url_str in test_list:
        html = get_one_page(url_str)
        content =parse_page1(html)
        print(content)



