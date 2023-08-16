# Article-crawling

爬取掘金和今日头条文章

juejin.py 用于爬取掘金文章，我进行了文章分类，可通过输入分类查询不同的文章（没有做异常处理）

toutiao.py 用于爬取今日头条里一个大牛的的文章，你可以修改链接爬取其他人的文章

## 支持存入数据库

### 创建一个 DatabaseConnector 对象

db_connector = DatabaseConnector("127.0.0.1", 3306, "root", "root", "root")

### 连接到数据库

db_connector.connect()

### 执行查询

result = db_connector.execute_query("SELECT \* FROM your_table")

### 断开与数据库的连接

db_connector.disconnect()
