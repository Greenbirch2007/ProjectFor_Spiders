#! -*- coding:utf-8 -*-


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
    for i in range(1,39):
        sql = 'select links from Big_Themes1 where id = %s ' % i
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
        cursor.executemany('insert into Aagin_Links1 (themes,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    for url_str in Python_sel_Mysql():
        try:


            driver = webdriver.Firefox()
            driver.get(url_str)
            big_list = []

            html = driver.page_source
            driver.quit()
            selector = etree.HTML(html)
            # 只爬取小标题，不然会造成重复爬取
            theme_title = selector.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a/span/text()')
            f_link = selector.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a/@href')

            for i1, i2 in zip(theme_title, f_link):
                big_list.append((i1, 'https://www.amazon.cn'+i2))

            insertDB(big_list)
            time.sleep(1)
        except :
            print('放过去～')


#
# create table Aagin_Links1(
# id int not null primary key auto_increment,
# themes varchar(80),
# links text
# ) engine=InnoDB  charset=utf8;


# drop  table Aagin_Links1;










