

#! -*- coding:utf-8 -*-
import datetime
import time

import pyautogui
import pymysql
from lxml import etree

from selenium import webdriver




def parse_page(html):
    selector = etree.HTML(html)

    book1 = selector.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book2 = selector.xpath('//*[@id="result_1"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book3 = selector.xpath('//*[@id="result_2"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book4 = selector.xpath('//*[@id="result_3"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book5 = selector.xpath('//*[@id="result_4"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book6 = selector.xpath('//*[@id="result_5"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book7 = selector.xpath('//*[@id="result_6"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book8 = selector.xpath('//*[@id="result_7"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book9 = selector.xpath('//*[@id="result_8"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book10 = selector.xpath('//*[@id="result_9"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book11 = selector.xpath('//*[@id="result_10"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book12= selector.xpath('//*[@id="result_11"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book13= selector.xpath('//*[@id="result_12"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book14= selector.xpath('//*[@id="result_13"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book15= selector.xpath('//*[@id="result_14"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')
    book16= selector.xpath('//*[@id="result_15"]/div/div/div/div[2]/div[1]/div[1]/a/h2/text()')

    f_book_title= book1+book2 +book3+book4+book5+book6+book7+book8+book9+book10+book11+book12+book13+book14+book15+book16


    blink1 = selector.xpath('//*[@id="result_0"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink2 = selector.xpath('//*[@id="result_1"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink3 = selector.xpath('//*[@id="result_2"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink4 = selector.xpath('//*[@id="result_3"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink5 = selector.xpath('//*[@id="result_4"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink6 = selector.xpath('//*[@id="result_5"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink7 = selector.xpath('//*[@id="result_6"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink8 = selector.xpath('//*[@id="result_7"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink9 = selector.xpath('//*[@id="result_8"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink10 = selector.xpath('//*[@id="result_9"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink11 = selector.xpath('//*[@id="result_10"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink12 = selector.xpath('//*[@id="result_11"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink13 = selector.xpath('//*[@id="result_12"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink14 = selector.xpath('//*[@id="result_13"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink15 = selector.xpath('//*[@id="result_14"]/div/div/div/div[2]/div[1]/div[1]/a/@href')
    blink16 = selector.xpath('//*[@id="result_15"]/div/div/div/div[2]/div[1]/div[1]/a/@href')

    f_blink = blink1+ blink2+ blink3+ blink4+ blink5+ blink6+ blink7+ blink8+ blink9+ blink10+ blink11+ blink12+ blink13+ blink14+ blink14+ blink15+ blink16




    f_theme = selector.xpath('//*[@id="s-result-count"]/span/span/text()')
    theme = f_theme * 16




    for i1,i2,i3 in zip(f_book_title,theme,f_blink):
        big_list.append((i1,i2,i3))
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
    url = 'https://www.amazon.cn/s?i=stripbooks&rh=n%3A658390051%2Cn%3A658391051%2Cn%3A658394051%2Cn%3A658508051%2Cn%3A659356051&qid=1561618452&ref=sr_pg_1'
    time.sleep(1)
    driver = webdriver.Chrome()  # 换一个浏览器好多了
    driver.get(url)
    html = driver.page_source

    content = parse_page(html)
    driver.quit()
    insertDB(content)

    # 用来回点击破掉，翻页的反爬虫
    # 首页会跳转　６６０个，人海战术，同时跑１０个爬虫！




# f_book_title,theme,f_blink


# create table Final_linkTable(
# id int not null primary key auto_increment,
# f_book_title text,
# theme varchar(80),
# f_blink text
# ) engine=InnoDB  charset=utf8;
#

# drop  table Final_linkTable;


