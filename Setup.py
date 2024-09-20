import sqlite3 as sql
import os
import subprocess
import sys

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
    try:
        # Check if requirements.txt exists
        if os.path.exists('requirements.txt'):
            # Install the dependencies
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
            print("Requirements installed successfully!")
        else:
            print("No requirements.txt file found!")
    except Exception as e:
        print(f"Error installing requirements: {e}")
    