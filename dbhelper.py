import pymysql
import db_config


class DBHelper:

    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=db_config.db_user,
                               passwd=db_config.db_password,
                               db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def add_crime(self, category, date, description):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (category, date, description)" \
                    "VALUES (%s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(query, (category, date, description))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
