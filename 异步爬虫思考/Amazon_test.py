

#! -*- coding:utf-8 -*-
import datetime
import time
import urllib.request
import re
import pymysql
from lxml import etree


# 异步处理的模块
import aiohttp
import asyncio


# 请求url
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()




# 请求页面
async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()







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


fetch_list= Python_sel_Mysql()

async def parse(url):
    html = await fetch(url)

    selector = etree.HTML(html)
    book_name = selector.xpath('//*[@id="productTitle"]/text()')
    price = []
    f_price = selector.xpath('//*[@id="soldByThirdParty"]/span[2]/text()')
    for item in f_price:
        f = "".join(item.split())
        price.append(f)


    for i1,i2 in zip(book_name,price):
        big_list.append((i1,i2))

    tasks = [fetch_content(url) for url in fetch_list]
    pages = await asyncio.gather(*tasks)





# 如果为空，就添加一个空字段，这里专门编写一个函数

def if_isnull(content):
    if len(content) ==0:
        f_content  = ''
    else:
        f_content =content

    return f_content



if __name__ == '__main__':


    for url_str in Python_sel_Mysql():
        big_list = []

        loop = asyncio.get_event_loop()
        start = time.time()
        loop.run_until_complete(parse(url_str))
        end = time.time()
        print('Cost {} seconds'.format(end - start))
        print(big_list)
# 需要有一个高并发的限制！比如100个！

#
# async def download(url):
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session, url)
#         await parse(html)
#
#
#
#
#
# def parse_page1(html):
#     selector = etree.HTML(html)
#     book_name = selector.xpath('//*[@id="productTitle"]/text()')
#
#     author = selector.xpath('//*[@id="bylineInfo"]/span/a/text()')
#
#
#     # # 图片用一个正则
#
#     patt = re.compile('<img alt="" src="(.*?)" class=".*?" id=".*?" data-a-dynamic-image=".*?" style=".*?">',re.S)
#     items  = re.findall(patt,html)
#
#     try:
#         book_cover = items[0]
#
#         urllib.request.urlretrieve(book_cover, '/home/r/亚马逊图书爬取分析/Pictures/%s' % (r'%s' % book_name[0]))
#     except FileNotFoundError:
#         print('图片下载有问题')
#
#     for i1,i2 in zip(book_name,author):
#         big_list.append(i1)
#         big_list.append(i2)
#
#
#
# def parse_page2(html):
#     selector = etree.HTML(html)
#
#     all_publishing = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[1]/text()')
#
#     publishing = []
#     publishing1 = all_publishing[0][:-17]
#     publishing.append(publishing1)
#
#     publishing_time = []
#     publishing_time1 = all_publishing[0][-11:]
#     publishing_time.append(publishing_time1)
#
#     price = []
#     f_price = selector.xpath('//*[@id="soldByThirdParty"]/span[2]/text()')
#     for item in f_price:
#         f = "".join(item.split())
#         price.append(f)
#
#     for i1,i2,i3 in zip(publishing,publishing_time,price):
#         big_list.append(i1)
#         big_list.append(i2)
#         big_list.append(i3)
#
#
#
#
#
#
#
# def parse_page3(html):
#     selector = etree.HTML(html)
#     all_publishing = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[1]/text()')
#
#     book_size = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[4]/text()')
#     page_count = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[2]/text()')
#     score = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[11]/span/span[1]/a[2]/i/span/text()')
#     isbn = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[5]/text()')
#     bar_code = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[6]/text()')
#     graphic_design_f = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[2]/b/text()')
#     graphic_design = []
#     graphic_design1 = graphic_design_f[0][:-1]
#     graphic_design.append(graphic_design1)
#
#     edition =[]
#     edition1 = all_publishing[0][-15:-11]
#     edition.append(edition1)
#
#     for i1,i2,i3,i4,i5,i6,i7 in zip(book_size,page_count,score,isbn,bar_code,graphic_design,edition):
#         big_list.append(i1)
#         big_list.append(i2)
#         big_list.append(i3)
#         big_list.append(i4)
#         big_list.append(i5)
#         big_list.append(i6)
#         big_list.append(i7)
#
#
#
# def parse_page4(html):
#     selector = etree.HTML(html)
#
#     f_product_size =selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[7]/text()')
#
#     product_size = []
#     for item in f_product_size:
#         f = "".join(item.split())
#         product_size.append(f)
#
#     weight = []
#     f_weight = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[8]/text()')
#     for item in f_weight:
#         f = "".join(item.split())
#         weight.append(f)
#
#     f_classify = selector.xpath('//*[@id="SalesRank"]/ul/li[1]/span[2]/a/text()')
#     classify = []
#     classify1 = f_classify[0][:4]
#     classify.append(classify1)
#     language = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[3]/text()')
#     brand = selector.xpath('//*[@id="detail_bullets_id"]/table/tbody/tr/td/div/ul/li[9]/text()')
#
#     for i1,i2,i3,i4,i5 in zip(product_size,weight,classify,language,brand):
#         big_list.append(i1)
#         big_list.append(i2)
#         big_list.append(i3)
#         big_list.append(i4)
#         big_list.append(i5)
#
#
#
#
#
#
#
#
# 请求100万个链接不是很理想：
# 1.原因是看不到异步处理的细节，
# 2.一旦中间报错，无法定位错误位置
# 3. 请求太快，来不及等待回复，因为页面的回复时间都不相同！
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# if __name__ == "__main__":
#
#
#     for url_str in Python_sel_Mysql():
#         try:
#
#
#             html = get_one_page(url_str)
#             big_list = []
#             ff_l = []
#             time.sleep(1)
#
#             parse_page1(html)
#             parse_page2(html)
#             parse_page3(html)
#             parse_page4(html)
#             l_t = tuple(big_list)
#             ff_l.append(l_t)
#         except IndexError as e :
#             print(e)
#         # insertDB(ff_l)
#
#
#
#
#
#
#
#
# #
# # create table amazon_book_Info2(
# # id int not null primary key auto_increment,
# # book_name varchar(60),
# # author varchar(50),
# # publishing  varchar(20),
# # publishing_time varchar(20),
# # price varchar(20),
# # book_size varchar(20),
# # page_count varchar(20),
# # score varchar(20),
# # isbn varchar(20),
# # bar_code varchar(80),
# # graphic_design varchar(10),
# #  edition varchar(10),
# # product_size  varchar(20),
# # weight varchar(10),
# # classify varchar(20),
# # language varchar(20),
# # brand varchar(20)
# # ) engine=InnoDB  charset=utf8;
#
#
#
# # drop  table amazon_book_Info;





