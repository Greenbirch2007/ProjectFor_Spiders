

#! -*- coding:utf-8 -*-
import datetime
import re
import time
import urllib.request

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

    author = selector.xpath('//*[@id="bylineInfo"]/span/a/text()')


    # # 图片用一个正则

    patt = re.compile('<img alt="" src="(.*?)" class=".*?" id=".*?" data-a-dynamic-image=".*?" style=".*?">',re.S)
    items  = re.findall(patt,html)
    book_cover = items[0]
    try:
        urllib.request.urlretrieve(book_cover, '/home/r/亚马逊图书爬取分析/Pictures/%s' % (r'%s' % book_name[0]))
    except FileNotFoundError:
        print('图片下载有问题')

    for i1,i2 in zip(book_name,author):
        big_list.append(i1)
        big_list.append(i2)



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

    for i1,i2,i3 in zip(publishing,publishing_time,price):
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

    for i1,i2,i3,i4,i5,i6,i7 in zip(book_size,page_count,score,isbn,bar_code,graphic_design,edition):
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

    for i1,i2,i3,i4,i5 in zip(product_size,weight,classify,language,brand):
        big_list.append(i1)
        big_list.append(i2)
        big_list.append(i3)
        big_list.append(i4)
        big_list.append(i5)



def parse_page5(html):
    selector = etree.HTML(html)

    about_the_author = []
    f_about_the_author = selector.xpath('//*[@id="s_content_1"]/p/text()')

    for item in f_about_the_author:
        f = "".join(item.split())
        about_the_author.append(f)


    f_book_review = selector.xpath('//*[@id="customer_review-R1TH8OGQH7PEW9"]/div[4]/span/div/div[1]/span/text()')
    book_review1  =",".join(f_book_review)
    book_review = [book_review1]
    create_time = selector.xpath('//*[@id="customer_review-R1TH8OGQH7PEW9"]/span/text()')
    commentator = selector.xpath('//*[@id="customer_review-R1TH8OGQH7PEW9"]/div[2]/a[2]/span/text()')
    rating = selector.xpath('//*[@id="customer_review-R1TH8OGQH7PEW9"]/div[2]/a[1]/i/span/text()')

    for i1,i2,i3,i4,i5 in zip(about_the_author,book_review,create_time,commentator,rating):
        big_list.append(i1)
        big_list.append(i2)
        big_list.append(i3)
        big_list.append(i4)
        big_list.append(i5)
















def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,888):
        sql = 'select links from An_small_links where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['links']
        yield url



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into amazon_book_Info (book_name,author,publishing,publishing_time,price,book_size,page_count,score,isbn,bar_code,graphic_design,edition,product_size,weight,classify,language,brand,about_the_author,book_review,create_time,commentator,rating) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":


    for url_str in Python_sel_Mysql():


        html = get_one_page(url_str)
        print(html)
        # big_list = []
        # ff_l = []
        # time.sleep(1)
        #
        # parse_page1(html)
        # parse_page2(html)
        # parse_page3(html)
        # parse_page4(html)
        # parse_page5(html)
        # l_t = tuple(big_list)
        # ff_l.append(l_t)
        # insertDB(ff_l)
        # print(datetime.datetime.now())








#
# create table amazon_book_Info(
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
# brand varchar(20),
# about_the_author text,
# book_review text,
# create_time  varchar(20),
# commentator varchar(20),
# rating varchar(20)
# ) engine=InnoDB  charset=utf8;


# drop  table amazon_book_Info;





