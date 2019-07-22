# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql
import requests
from requests.exceptions import RequestException

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



def parse_note(html):
    big_list = []
    selector = etree.HTML(html)

    # 分类浏览的解析
    themes = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/tr/td/a/text()')
    links = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/tr/td/a/@href')


    # 按所有热门标签的解析
    # themes = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/tr/td/a/text()')
    # links = selector.xpath('//*[@id="content"]/div/div[1]/div[2]/div/table/tbody/tr/td/a/@href')

    for i1,i2 in zip(themes,links):
        big_list.append((i1,'https://book.douban.com'+i2))


    return big_list










def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Douban',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into DouBan_ThemeLinks (themes,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






#
if __name__ == '__main__':
    # 分类浏览的url
    url_list =['https://book.douban.com/tag/?view=type']
    # 按热门标签 的url
    # url_list =['https://book.douban.com/tag/?view=cloud']
    for item in url_list:
        html = call_page(item)
        content = parse_note(html)
        insertDB(content)
        print(item)





# themes,links
# create table DouBan_ThemeLinks(
# id int not null primary key auto_increment,
# themes varchar(120) ,
# links varchar(120)
#  ) engine=InnoDB default charset=utf8;
# #
#
# drop table DouBan_ThemeLinks;
