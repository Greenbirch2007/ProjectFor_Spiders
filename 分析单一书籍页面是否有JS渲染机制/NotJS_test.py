#! -*- coding:utf-8 -*-

import re
import requests
import pymongo
import pymysql
from multiprocessing import Pool

from lxml import etree
#捕获异常
from requests.exceptions import RequestException
# #请求html

headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Cookie': 'x-wl-uid=1L4fMz/d6VRXeI/lf0y32wKTYIUPyOOD4WXNtpN99Mij/sJQ0adK5zEYdRGU+tv50Hg2WHbvLhdg=; session-id=458-9495223-4103462; ubid-acbcn=457-1233814-2015331; i18n-prefs=CNY; p2dPopoverID_all_1=1561562813.163; p2dPopoverID_default_1=1561562813.163; lc-acbcn=zh_CN; session-token="leHlWOZ3X2AcCudwOaSpgyTWyNH+zb33Bk2w71YTrsWbN9Cfupo4mJ/sTD0jsy04hbwlr/Re49jrx4dBgUHAMFAm70/XfdAn48FjvCSp1EZpjzgWDtyUttMWUZ3UmjG3nCn9UQWU4TZ5SNr5L195aGlZojK/xnZj142snHHQR0Rbdq+4z5DdzgvT9DcoWyxoieI0Auq14Hl9WsbkSQPntw=="; session-id-time=2082787201l; csm-hit=tb:s-C3MQN799QSS47A11BTZA|1561863024459&t:1561863025101&adb:adblk_no',
'Host': 'www.amazon.cn',
'Referer': 'https://www.amazon.cn/b/ref=bsm14_0_0_0?ie=UTF8&node=658512051',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
def get_one_page(url):



    # headers = {'Cookie': 'x-wl-uid=1L4fMz/d6VRXeI/lf0y32wKTYIUPyOOD4WXNtpN99Mij/sJQ0adK5zEYdRGU+tv50Hg2WHbvLhdg=; session-id=458-9495223-4103462; ubid-acbcn=457-1233814-2015331; i18n-prefs=CNY; p2dPopoverID_all_1=1561562813.163; p2dPopoverID_default_1=1561562813.163; lc-acbcn=zh_CN; session-token="leHlWOZ3X2AcCudwOaSpgyTWyNH+zb33Bk2w71YTrsWbN9Cfupo4mJ/sTD0jsy04hbwlr/Re49jrx4dBgUHAMFAm70/XfdAn48FjvCSp1EZpjzgWDtyUttMWUZ3UmjG3nCn9UQWU4TZ5SNr5L195aGlZojK/xnZj142snHHQR0Rbdq+4z5DdzgvT9DcoWyxoieI0Auq14Hl9WsbkSQPntw=="; session-id-time=2082787201l; csm-hit=tb:s-C3MQN799QSS47A11BTZA|1561863024459&t:1561863025101&adb:adblk_no'}
    req= requests.get(url,headers=headers)
      #  requests 中文编码的终极办法！
    if req.encoding == 'ISO-8859-1':
        encodings = requests.utils.get_encodings_from_content(req.text)
        if encodings:
            encoding = encodings[0]
        else:
            encoding = req.apparent_encoding

        # encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
        global encode_content
        encode_content = req.content.decode(encoding, 'replace')  # 如果设置为replace，则会用?取代非法字符；
        return  (encode_content)




if __name__ == '__main__':
    url = 'https://www.amazon.cn/dp/B07SFTNKLS'
    html = get_one_page(url)
    print(html)



