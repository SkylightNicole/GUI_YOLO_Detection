import sqlite3 as sql
import os

def Setup():
    try:
        connect = sql.connect("Database.db")
        connect.execute("CREATE TABLE Login_Info(Username varchar[255],Password varchar[255],Salt varchar[255]);")
        connect.execute("CREATE TABLE Information(License_Plate varchar[255],Name varchar[255],Phone_Num varchar[255],Car_Color varchar[255],Brand varchar[255]);")
        print("Command executed!")
    except Exception as e:
        print(f"Error : {e}")
    finally:
        connect.close()
        print("Login Database successfully created!")