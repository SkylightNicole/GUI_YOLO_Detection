from flask import Flask, request , jsonify
import subprocess
import threading
import time

last_data = None
data = None
app = Flask(__name__)

@app.route("/data",methods=["POST"])
def receive_data():
    global last_data
    try:
        data = request.get_data(as_text=True)
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

def run_ngrok():
    # Run ngrok as a subprocess
    command = "ngrok http --domain=bright-donkey-exact.ngrok-free.app 5001"
    time.sleep(2)  # Allow some time for Flask to start
    subprocess.Popen(["cmd.exe","/k",command])

if __name__ == "__main__":
    ngrok_thread = threading.Thread(target=run_ngrok)
    ngrok_thread.start()
    app.run(host="0.0.0.0", port=5001)