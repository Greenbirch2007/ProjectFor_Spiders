

#! -*- coding:utf-8 -*-
import datetime
import re
import time
import urllib.request


import re
import requests
import pymongo
import pymysql
from requests.exceptions import RequestException
from lxml import etree


import pymysql
from lxml import etree

from selenium import webdriver


def get_one_page(url):
    driver = webdriver.Firefox()

    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html


def parse_page1(html):
    selector = etree.HTML(html)
    book_name = selector.xpath('//*[@id="productTitle"]/text()')

    # 如果作者有两个或多个！
    f_author = selector.xpath('//*[@id="bylineInfo"]/span/a/text()')
    author = []
    # 拼接是放入整个列表
    author.append((",".join(f_author)))



    # # 图片用一个正则

    patt = re.compile('<img alt="" src="(.*?)" class=".*?" id=".*?" data-a-dynamic-image=".*?" style=".*?">',re.S)
    items  = re.findall(patt,html)

    try:
        book_cover = items[0]

        urllib.request.urlretrieve(book_cover, '/home/r/亚马逊图书爬取分析/Pictures/%s' % (r'%s' % book_name[0]))
    except FileNotFoundError:
        print('图片下载有问题')

    book_name1 = if_isnull(book_name)
    author1 = if_isnull(author)

    for i1,i2 in zip(book_name1,author1):
        big_list.append(i1)
        big_list.append(i2)

# 单独写一个剔除空格的函数


def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items



def parse_page2(html):
    selector = etree.HTML(html)

    all_publishing = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[1]/text()')

    publishing = []
    publishing1 = all_publishing[0][:-17]
    publishing.append(publishing1)

    publishing_time = []
    publishing_time1 = all_publishing[0][-11:]
    publishing_time.append(publishing_time1)

    price = []
    f_price = selector.xpath('//*[@id="soldByThirdParty"]/span[2]/text()')
    for item in f_price:
        f = "".join(item.split())
        price.append(f)

    publishing1 = if_isnull(publishing)
    publishing_time1 = if_isnull(publishing_time)
    price1= if_isnull(price)

    for i1,i2,i3 in zip(publishing1,publishing_time1,price1):
        big_list.append(i1)
        big_list.append(i2)
        big_list.append(i3)







def parse_page3(html):
    selector = etree.HTML(html)
    all_publishing = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[1]/text()')

    book_size = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[4]/text()')
    page_count = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[2]/text()')
    score = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[11]/span/span[1]/a[2]/i/span/text()')
    isbn = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[5]/text()')
    bar_code = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[6]/text()')
    graphic_design_f = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[2]/b/text()')
    graphic_design = []
    graphic_design1 = graphic_design_f[0][:-1]
    graphic_design.append(graphic_design1)

    edition =[]
    edition1 = all_publishing[0][-15:-11]
    edition.append(edition1)

    book_size1= if_isnull(book_size)
    page_count1= if_isnull(page_count)
    score1 = if_isnull(score)
    isbn1 =if_isnull(isbn)
    bar_code1 = if_isnull(bar_code)
    graphic_design1 = if_isnull(graphic_design)
    edition1 =if_isnull(edition)




    for i1,i2,i3,i4,i5,i6,i7 in zip(book_size1,page_count1,score1,isbn1,bar_code1,graphic_design1,edition1):
        big_list.append(i1)
        big_list.append(i2)
        big_list.append(i3)
        big_list.append(i4)
        big_list.append(i5)
        big_list.append(i6)
        big_list.append(i7)



def parse_page4(html):
    selector = etree.HTML(html)

    f_product_size =selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[7]/text()')

    product_size = []
    for item in f_product_size:
        f = "".join(item.split())
        product_size.append(f)

    weight = []
    f_weight = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[8]/text()')
    for item in f_weight:
        f = "".join(item.split())
        weight.append(f)

    f_classify = selector.xpath('//*[@id="SalesRank"]/ul/li[1]/span[2]/a/text()')
    classify = []
    classify1 = f_classify[0][:4]
    classify.append(classify1)
    language = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[3]/text()')
    brand = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[9]/text()')

    product_size1 = if_isnull(product_size)
    weight1 = if_isnull(weight)
    classify1 =if_isnull(classify)
    language1 = if_isnull(language)
    brand1= if_isnull(brand)


    for i1,i2,i3,i4,i5 in zip(product_size1,weight1,classify1,language1,brand1):
        big_list.append(i1)
        big_list.append(i2)
        big_list.append(i3)
        big_list.append(i4)
        big_list.append(i5)



def ifisnull_removeBlock(content):
    if_list =[]

    if  content ==None:
        f_content  = ''
        if_list.append(f_content)
    else:

        f_content =content
        if_list = f_content

    new_items = []
    for it in if_list:
        f = "".join(it.split())
        new_items.append(f)
    return new_items















def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    try:

        for i in range(1,888):
            sql = 'select * from Final_linkTable where id = %s ' % i
            # #执行sql语句
            cur.execute(sql)
            # #获取所有记录列表
            data = cur.fetchone()
            book_link = data['f_blink']
            yield book_link
    except :
        print("放过去")



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into amazon_book_Info2 (book_name,author,publishing,publishing_time,price,book_size,page_count,score,isbn,bar_code,graphic_design,edition,product_size,weight,classify,language,brand) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')







if __name__ == "__main__":


    for url_str in Python_sel_Mysql():
        try:

            html = get_one_page(url_str)
            big_list = []
            ff_l = []
            time.sleep(1)

            parse_page1(html)
            print(url_str)
            #     parse_page2(html)
        #     parse_page3(html)
        #     parse_page4(html)
        #     l_t = tuple(big_list)
        #     ff_l.append(l_t)
        except IndexError as e :
            print(e)
        #     print(ff_l)
        # insertDB(ff_l)








#
# create table amazon_book_Info2(
# id int not null primary key auto_increment,
# book_name varchar(60),
# author varchar(50),
# publishing  varchar(20),
# publishing_time varchar(20),
# price varchar(20),
# book_size varchar(20),
# page_count varchar(20),
# score varchar(20),
# isbn varchar(20),
# bar_code varchar(80),
# graphic_design varchar(10),
#  edition varchar(10),
# product_size  varchar(20),
# weight varchar(10),
# classify varchar(20),
# language varchar(20),
# brand varchar(20)
# ) engine=InnoDB  charset=utf8;



# drop  table amazon_book_Info;