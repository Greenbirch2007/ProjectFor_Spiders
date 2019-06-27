#! -*- coding:utf-8 -*-


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
        cursor.executemany('insert into An_Big_links (themes,links) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except :
        print('出列啦')



if __name__ == "__main__":
    big_list = []
    time.sleep(1)
    url = 'https://www.amazon.cn/gp/book/all_category/ref=sv_b_0'
    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    driver.quit()
    selector = etree.HTML(html)
    # 只爬取小标题，不然会造成重复爬取
    # big_title = selector.xpath('//*[@id="content"]/div/div/h5/a/span/text()')
    # big_link = selector.xpath('//*[@id="content"]/div/div/h5/a/@href')
    small_title = selector.xpath('//*[@id="content"]/div/div/table/tbody/tr/td/a/text()')
    ss_list= []
    for item in small_title:
        f_s_title = "".join(item.split())
        ss_list.append(f_s_title)

    small_link = selector.xpath('//*[@id="content"]/div/div/table/tbody/tr/td/a/@href')
    # for i1, i2 in zip(big_title, big_link):
    #     big_list1.append((i1, i2))
    for i1, i2 in zip(ss_list, small_link):
        big_list.append((i1, i2))

    insertDB(big_list)


#
# create table An_Big_links(
# id int not null primary key auto_increment,
# themes varchar(80),
# links text
# ) engine=InnoDB  charset=utf8;


# drop  table An_Big_links;










