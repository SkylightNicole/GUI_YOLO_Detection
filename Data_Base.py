import hashlib
import os
from dotenv import load_dotenv
import mysql.connector as mysql

load_dotenv()
DB_Password = os.getenv("DB_Password")

def Write_Register(Username,Password):
    """Salt and Write it down on Database"""
    connection = None
    salt = os.urandom(10)
    hash_pass = hashlib.pbkdf2_hmac("sha256",Password.encode("utf-8"),salt,50000)
    salt = salt.hex()
    hash_pass = hash_pass.hex()
    try:
        connection = mysql.connect(
            host = "sql12.freesqldatabase.com",
            user = "sql12756667",
            password = DB_Password,
            database = "sql12756667"
        )
        if connection is not None and connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("INSERT INTO Login_Information VALUES(%s,%s,%s);",(Username,hash_pass,salt))
            connection.commit()
    except Exception as w:
        print("Error : ",w)
    except mysql.Error as s:
        print("MySQL Error : ",s)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

def Check(Username,Password):
    """Use to check whether Username nad Password is correct"""
    connection = None
    try:
        check = 0
        connection = mysql.connect(
            host = "sql12.freesqldatabase.com",
            user = "sql12756667",
            password = DB_Password,
            database = "sql12756667"
        )
        if connection is not None and connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Login_Information")
            Info = cursor.fetchall()
            for i in Info:
                if i[0] == Username:
                    Pass_bi = bytes.fromhex(i[1])
                    Salt_bi = bytes.fromhex(i[2])
                    Veri_Pass = hashlib.pbkdf2_hmac("sha256",Password.encode("utf-8"),Salt_bi,50000)
                    if Pass_bi == Veri_Pass:
                        print("Correct!")
                        return True
                    else:
                        print("Incorrect Password")
                        return False

    except Exception as w:
        print("Error : ",w)
    except mysql.Error as s:
        print("MySQL Error : ",s)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

def add_more_rider(plate,name,phone,color,brand):
    """Function to add rider to Database"""
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
            cursor.execute("INSERT INTO Information VALUES(%s,%s,%s,%s,%s);",(plate,name,phone,color,brand))
            connection.commit()
        return True
    except Exception as e:
        print("Error" , e)
        return False
    except mysql.Error as s:
        print("MySQL Error : ",s)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

def rider_check(text):
    """Function to check whether they're rider or not"""
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
            cursor.execute("SELECT * from Information")
            result = cursor.fetchall()
            for row in result:
                if row[0] in text:
                    return row
            return None
    except Exception as s:
        print("Error" , s)
    except mysql.Error as w:
        print("MySQL Error : ",w)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()