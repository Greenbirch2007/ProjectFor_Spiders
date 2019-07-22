# -*- coding:utf-8 -*-
import datetime
import re
import time
import requests
from requests.exceptions import RequestException
import pymysql


from lxml import etree



def call_page(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre'
    }
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None









def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Douban',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,181):
        sql = 'select * from DouBan_DistanctLink where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['links']
        yield url


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



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Douban',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into Douban_OneBook_link (title,link) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass




# start=7580&type=T
if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        # 拼接URL
        while True:
            for num in range(0,8000,20):
                big_list = []

                f_url = url_str+'?start='+str(num)+'&type=T'
                html = call_page(f_url)
                selector = etree.HTML(html)
                Last_page = selector.xpath('//*[@id="subject_list"]/div[2]/span[last()]/a/text()')

                if Last_page != None:

                    selector = etree.HTML(html)
                    title1 = selector.xpath('//*[@id="subject_list"]/ul/li/div[2]/h2/a/text()')
                    link = selector.xpath('//*[@id="subject_list"]/ul/li/div[2]/h2/a/@href')
                    title = ifisnull_removeBlock(title1)

                    for i1, i2 in zip(title, link):
                        big_list.append((i1, i2))

                    insertDB(big_list)
                    print(big_list)
                    time.sleep(0.8)
                    print(datetime.datetime.now())
                else:
                    break
                print(f_url)




# 只公布前




#  (title,link)
# create table Douban_OneBook_link(
# id int not null primary key auto_increment,
# title text,
# link text
#  ) engine=InnoDB default charset=utf8;
# #
#
# drop table Douban_OneBook_link;
