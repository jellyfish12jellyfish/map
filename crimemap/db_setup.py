import pymysql
import db_config

connection = pymysql.connect(host='localhost',
                             # port=3306,
                             user=db_config.db_user,
                             passwd=db_config.db_password)

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
