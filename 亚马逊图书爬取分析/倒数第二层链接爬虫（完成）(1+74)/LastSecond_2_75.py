

#! -*- coding:utf-8 -*-
import datetime
import time

import pyautogui
import pymysql
from lxml import etree

from selenium import webdriver

driver = webdriver.Firefox()  # 换一个浏览器好多了

def get_one_page(url):

    driver.get(url)

    html = driver.page_source
    return html


def next_page():
    for i in range(1,76):  # 有一个翻页小技巧
        driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[7]/div/div/div/ul/li[last()]/a').click()
        html = driver.page_source
        return html

def parse_page(html):
    selector = etree.HTML(html)
    title = selector.xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/h2/a/span/text()')
    half_link = selector.xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/h2/a/@href')
    f_theme = selector.xpath('//*[@id="search"]/span/h1/div/div[1]/div/div/span[last()]/text()')
    theme = len(title) * f_theme

    for i1,i2,i3 in zip(title,theme,half_link):
        big_list.append((i1,i2,'https://www.amazon.cn'+i3))
    return big_list





def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into Final_linkTable (f_book_title,theme,f_blink) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    url = 'https://www.amazon.cn/s?i=stripbooks&rh=n%3A658390051%2Cn%3A658391051%2Cn%3A658394051%2Cn%3A658508051%2Cn%3A659356051&lo=list&page=2&qid=1561621216&ref=sr_pg_2'
    time.sleep(1)
    html = get_one_page(url)
    content = parse_page(html)
    insertDB(content)


    while True:
        html = next_page()
        content = parse_page(html)
        insertDB(content)
        print(datetime.datetime.now())

# f_book_title,theme,f_blink
# create table Final_linkTable(
# id int not null primary key auto_increment,
# f_book_title text,
# theme varchar(80),
# f_blink text
# ) engine=InnoDB  charset=utf8;
#

# drop  table Final_linkTable;



