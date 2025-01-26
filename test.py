import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()
DB_Password = os.getenv("DB_Password")

User = "ChloeyNic@gmail.com"
Pass = "ilovebluesky"


connection = None
try:
    connection = mysql.connect(
        host = "sql12.freesqldatabase.com",
        user = "sql12756667",
        password = DB_Password,
        database = "sql12756667"
    )
    if connection is not None and connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * from Moblie_User")
        result = cursor.fetchall()
        for i in result:
            if i[0] == User:
                if i[1] == Pass:
                    print("Correct!")
        print("Fetch Successfully")
except Exception as s:
    print("Error" , s)
except mysql.Error as w:
    print("MySQL Error : ",w)
finally:
    if connection is not None and connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection Closed Successfully")