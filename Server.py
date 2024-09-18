from flask import Flask, request , jsonify

app = Flask(__name__)

@app.route("/data",methods=["POST"])
def receive_data():
    try:
        data = request.get_json()
        print("Parsed JSON Data:", data)
        if not data:
            return jsonify({"status": "error", "message": "No data received"}), 400
        
        print("Receive Data : ",data)
        return jsonify({"status" : "success" , "data_recieve " : data}) , 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"status": "error", "message": "An error occurred"}), 500
app.run(host="0.0.0.0", port=5001)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)