

#! -*- coding:utf-8 -*-
import datetime
import time
import pymysql
from lxml import etree
from selenium import webdriver






def Python_sel_Mysql():
    # 使用cursor()方法获取操作游标
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for i in range(1,888):
        sql = 'select links from An_Big_links where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['links']
        yield url


if __name__ == '__main__':
    for url_str in Python_sel_Mysql():
        try:
            big_list = []
            driver = webdriver.Chrome()
            driver.get(url_str)
            html = driver.page_source
            selector = etree.HTML(html)
            themes = selector.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a/span/text()')
            links = selector.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a/@href')

            for i1, i2 in zip(themes, links):
                big_list.append((i1, 'https://www.amazon.cn' + i2))
            driver.quit()

            connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            # 这里是判断big_list的长度，不是content字符的长度
            try:
                cursor.executemany('insert into An_Middle_link (themes,links) values (%s,%s)', big_list)
                connection.commit()
                connection.close()
                print('向MySQL中添加数据成功！')
            except:
                print('出列啦')
            print(datetime.datetime.now())
            # del big_list  #插入一次之后，销毁列表数据
            time.sleep(1)

        except :
            print("放过～")



#
# create table An_Middle_link(
# id int not null primary key auto_increment,
# themes varchar(80),
# links text
# ) engine=InnoDB  charset=utf8;


# drop  table An_Middle_link;










