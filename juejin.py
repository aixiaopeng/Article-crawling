import hashlib
import json
import requests
from sql_connector import DatabaseConnector

info = {"id_type": 2, "sort_type": 200, "cate_id": "0", "cursor": "0", "limit": 20}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}
home = {}

# 创建MD5对象
md5_hash = hashlib.md5()


# 创建一个DatabaseConnector对象
db_connector = DatabaseConnector("lm", 3306, "root", "nantongpark", "lingman-home")

# 连接到数据库
db_connector.connect()

def get_home():
    url = 'https://api.juejin.cn/tag_api/v1/query_category_briefs'
    resp = requests.get(url)
    data = json.loads(resp.text)
    for i in data["data"]:
        try:  # 去除广告推广内容的报错
            home[i["category_name"]] = i["category_id"]

        except:
            continue
    for i in home:
        print(i)
    get_data()


def get_data():
    type = input("请输入分类：")
    key = home[type]
    url = 'https://api.juejin.cn/recommend_api/v1/article/recommend_cate_feed'
    info = {"id_type": 2, "sort_type": 200, "cate_id": key, "cursor": "0", "limit": 20}
    resp1 = requests.post(url, json=info, headers=headers)  # data自动使用json方式发送
    data = json.loads(resp1.text)
    for i in data["data"]:
        try:  # 去除广告推广内容的报错
            author= i["author_user_info"]["user_name"]
            title = i["article_info"]["title"]
            url = "https://juejin.cn/post/" + i["article_id"]
            print("作者："+author+"----"+"标题："+title+"----"+"链接："+url)

        except:
            continue






if __name__ == '__main__':
    get_home()
    # 断开与数据库的连接
    db_connector.disconnect()