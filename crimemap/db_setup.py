import pymysql
import my_id

connection = pymysql.connect(host='localhost',
                             # port=3306,
                             user=my_id.db_user,
                             passwd=my_id.db_password)

try:
    with connection.cursor() as cursor:
        sql = 'CREATE DATABASE IF NOT EXISTS crimemap'
        cursor.execute(sql)
        sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
        id int NOT NULL AUTO_INCREMENT,
        latitude FLOAT,
        longitude FLOAT,
        date DATETIME,
        category VARCHAR(50),
        description VARCHAR(1000),
        updated_at TIMESTAMP,
        PRIMARY KEY (id)
        )"""
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
