import sqlite3 as sql
import hashlib
import os

Database = "Database.db"

def Write_Register(Username,Password):
    """Salt and Write it down on Database"""
    salt = os.urandom(10)
    hash_pass = hashlib.pbkdf2_hmac("sha256",Password.encode("utf-8"),salt,50000)
    salt = salt.hex()
    hash_pass = hash_pass.hex()
    try:
        Connect = sql.connect(Database)
        Connect.execute("INSERT INTO Login_Info VALUES(?,?,?);",(Username,hash_pass,salt))
        Connect.commit()
    except Exception as w:
        print("Error : ",w)
    finally:
        Connect.close()
        print("Connection Closed Successfully")

def Check(Username,Password):
    """Use to check whether Username nad Password is correct"""
    check = 0
    Connect = sql.connect(Database)
    Info = Connect.execute("SELECT * FROM Login_Info")
    for i in Info:
        if i[0] == Username:
            Pass_bi = bytes.fromhex(i[1])
            Salt_bi = bytes.fromhex(i[2])
            Veri_Pass = hashlib.pbkdf2_hmac("sha256",Password.encode("utf-8"),Salt_bi,50000)
            if Pass_bi == Veri_Pass:
                print("Correct!")
                Connect.close()
                return True
            else:
                print("Incorrect Password")
                Connect.close()
                return False
    Connect.close()
    return False

def add_more_rider(plate,name,phone,color,brand):
    """Function to add rider to Database"""
    try:
        Connect = sql.connect(Database)
        Connect.execute("INSERT INTO Information VALUES(?,?,?,?,?);",(plate,name,phone,color,brand))
        Connect.commit()
        return True
    except Exception as e:
        print("Error" , e)
        return False
    finally:
        Connect.close()

def rider_check(text):
    """Function to check whether they're rider or not"""
    try:
        Connect = sql.connect(Database)
        Cursor = Connect.cursor()
        Cursor.execute("SELECT * from Information")
        result = Cursor.fetchall()
        for row in result:
            if row[0] == text:
                return row
        return None
    except Exception as s:
        print("Error" , s)
    finally:
        Connect.close()
    
