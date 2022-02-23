import pymysql

conn = pymysql.connect(  # 创建数据库连接
    host='localhost',  # 要连接的数据库所在主机ip
    user='root',  # 数据库登录用户名
    password='66666666',  # 登录用户密码
    database='west2_takeout',  # 连接的数据库名，也可以后续通过cursor.execture('user test_db')指定
    charset='utf8'  # 编码，注意不能写成utf-8
)