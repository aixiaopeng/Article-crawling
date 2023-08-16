import hashlib
import json

import mysql.connector
import requests

from sql_connector import DatabaseConnector

# 创建一个DatabaseConnector对象
db_connector = DatabaseConnector("lm", 3306, "root", "nantongpark", "lingman-home")

# 连接到数据库
db_connector.connect()

def get_date():
    url = 'https://www.toutiao.com/api/pc/list/user/feed?category=profile_all&token=MS4wLjABAAAA_Q07NxeCa4hDPFoRcdphaZOk2X6C8BApfpTPTMLJswI&max_behot_time=0&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo00101-MNeCAAAIDDYw-CYB6rW6fjKXyAAJwpcfBcoV6Ylu0z.KHznzk.HIP0fjFn1rffNc6CRLDhqjJqgZrY1eOV2zexjDhuj3-JgbDiUgmDfFTWYKnbiGOrKS2v8MSVQqswyI1W37'
    # 创建MD5对象

    resp = requests.get(url)
    data = json.loads(resp.text)
    for i in data["data"]:
        try:  # 去除广告推广内容的报错
            # 更新MD5对象的哈希值
            title = i["title"]
            url = i["display_url"]
            print("标题："+title+"----"+"链接："+url)
        except:
            continue


if __name__ == '__main__':
    get_date()