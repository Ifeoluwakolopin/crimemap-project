import datetime
import dbconfig
import pymysql

class DBHelper:

    def connect(self, database="crimemap"):
        return pymysql.connect(
            host="localhost",
            user=dbconfig.db_user,
            passwd=dbconfig.db_password,
            db=database
        )

    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT latitude, logitude, date, category, description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            named_crimes = []
            for crime in crimes:
                named_crimes.append({
                    'latitude':crime[0],
                    'longitude':crime[1],
                    'date':crime[2],
                    'category':crime[3],
                    'description':crime[4]
                })
            return named_crimes    
        finally:
            connection.close()


    def add_crime(self, category, date, latitude, longitude, description):
        connection = self.connect()
        try:
            query = """
            INSERT INTO crimes (category, date, latitude, longitude, description)
            VALUES (%s, %s, %s, %s, %s);
            """
            with connection.cursor() as cursor:
                cursor.execute(query, (
                    category, date, latitude, longitude, description
                ))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
            