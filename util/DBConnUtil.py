#util/DBConnUtil.py

import mysql.connector
from mysql.connector import Error
import mysql.connector

class DBConnUtil:
    @staticmethod
    def get_connection():
        connection = None
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='CMS',
                user='root',
                password='0000'
            )
            if connection.is_connected():
                print("Database connection established successfully")
        except Error as e:
            print("Error connecting to the database:", e)
        return connection
