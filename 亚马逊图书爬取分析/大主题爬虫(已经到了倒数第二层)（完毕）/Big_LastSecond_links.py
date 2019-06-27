#! -*- coding:utf-8 -*-
import datetime
import time
import pymysql
from lxml import etree
from selenium import webdriver






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into LastSecond_links (themes,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Amazon',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    # sql 语句
    for i in range(64, 527):  #共有５２７行
        sql = 'select * from Aagin_Links1 where id = %s ' % i
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        url = data['links']
        theme = data['themes']
        Test_list =[]
        Test_list.append((theme,url))
        for item in Test_list:
            # item[0]:主题名   #item[1]:链接
            item_theme = item[0]
            item_link = item[1]
            driver = webdriver.Chrome()
            driver.get(item_link)
            big_list = []

            html = driver.page_source
            driver.quit()
            try:
                selector = etree.HTML(html)

                theme_title = selector.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a/span/text()')
                f_link = selector.xpath('//*[@id="leftNav"]/ul[1]/ul/div/li/span/a/@href')
                if len(theme_title) !=0 :

                    for i1, i2 in zip(theme_title, f_link):
                        big_list.append((i1,i2))  # I2在解析时，意外不需要添加其他字段

                    insertDB(big_list)
                    time.sleep(1)
                else:
                    list_item = []
                    list_item.append(item)
                    insertDB(list_item)
            except :
                print('放过了～')
            print(datetime.datetime.now())
            print("这已经是第　%s 页了！"% str(i))

        #



     # 通过请求，解析，１．如果返回的解析len就把Aagin_Links1提取的字段直接插入到新的表　LastSecond_links中
        # 如果解析结果为０时，就直接解析后插入到新表　LastSecond_links中
        # 通过




#
# create table LastSecond_links(
# id int not null primary key auto_increment,
# themes varchar(80),
# links text
# ) engine=InnoDB  charset=utf8;





# drop  table LastSecond_links;


# 大主题通过










