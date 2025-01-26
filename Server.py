from flask import Flask, request , jsonify
import mysql.connector as mysql
from dotenv import load_dotenv
import os


load_dotenv()
DB_Password = os.getenv("DB_Password")
last_data = None
data = None
app = Flask(__name__)
rider_data = None


@app.route("/data",methods=["POST"])
def receive_data():
    global last_data
    print("Called!")
    try:
        data = request.get_data(as_text=True)
        print(data)
        if not data:
            return jsonify({"status": "error", "message": "No data received"}), 400
        if data is not None:
            last_data = data
        return jsonify({"status" : "success" , "data_recieve " : data}) , 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred"}), 500

@app.route("/data", methods=["GET"])
def send_data():
    global last_data
    # This could be any data you want to return
    if last_data is not None:
        return last_data, 200 , {'Content-Type': 'text/plain'}
    return "No Data Available" , 400

@app.route("/phone/register" , methods=["POST"])
def regis_phone():
    data = request.get_json()
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
            cursor.execute("INSERT INTO Moblie_User VALUES(%s,%s,%s);",(data["Username"],data["Password"],data["Salt"]))
            connection.commit()
            
    except Exception as s:
        print("Error" , s)
    except mysql.Error as w:
        print("MySQL Error : ",w)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection Closed Successfully")

    return jsonify({"status" : "success"}) , 200

@app.route("/get_data" , methods=["GET"])
def get_data():
    connection = None
    try:
        connection = mysql.connect(
            host = "sql12.freesqldatabase.com",
            user = "sql12756667",
            password = DB_Password,
            database = "sql12756667"
        )
        if connection is not None and connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * from Moblie_User")
            result = cursor.fetchall()
            custom_json = []
            for row in result:
                custom_json.append({               
                    "Username" : row["Gmail"],
                    "Password" : row["Password"],
                    "Salt" : row["Salt"]})
            
            return jsonify(custom_json) , 200

    except Exception as s:
        print("Error" , s)
    except mysql.Error as w:
        print("MySQL Error : ",w)
    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection Closed Successfully")

@app.route("/rider/upload" , methods=["POST"])
def upload_rider():
    global rider_data
    try:
        incoming_data = request.get_json()
        if incoming_data:
            rider_data = incoming_data
            return jsonify({"message" : "Data Receive Successfully"}) , 200
        return jsonify({"message" : "No Data Received!"}) , 400
    except Exception as e:
        return jsonify({"Error" : str(e)}), 500

@app.route("/rider/retrieve", methods=["GET"])
def get_rider():
    try:
        return jsonify(rider_data) , 200
    except Exception as e:
        return jsonify({"Error" : str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)