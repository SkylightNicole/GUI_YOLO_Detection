import tkinter as tk
from tkinter import StringVar
import requests

access_token = "4PDjZEWrY8xe6CN9ahyLaMmu6OOBZCoIMpvjYreVCOt"

app = tk.Tk()
app.title("Line")
app.geometry("500x300")

def send_line_message(token, message):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "message": message
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code

data = StringVar()

entry = tk.Entry(textvariable=data)
entry.place(x=230,y=100)
def send():
    data_to_send = data.get()
    status_code = send_line_message(access_token,data_to_send)
    if status_code == 200:
        print("Message Sent Successfully")
    else:
        print(f"Failed to Send message. Status Code : {status_code}")

button = tk.Button(app,text="Send Data",command=send)
button.place(x=230,y=150)

app.mainloop()