import os
import pymysql

conn = pymysql.connect(
    host=os.getenv('TAKEOUT_DB_HOST', 'localhost'),
    port=int(os.getenv('TAKEOUT_DB_PORT', '3306')),
    user=os.getenv('TAKEOUT_DB_USER', 'root'),
    password=os.getenv('TAKEOUT_DB_PASSWORD', ''),
    database=os.getenv('TAKEOUT_DB_NAME', 'west2_takeout'),
    charset='utf8'
)
