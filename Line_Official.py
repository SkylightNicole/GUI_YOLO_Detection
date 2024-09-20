import tkinter as tk
from tkinter import StringVar
import requests

token = "p+MqeGAW5R0kb1BQmLkHzsCd451UWx3FbriiQa50hy4bmYCoqeMZS03HuncIh8f0TfOtmf0pNxoFhSAtM9PXyiEQEuN37m3Xk2/pJte6co0e2wd0hMLzyjh1zO28+q7zj9A70CALxMhIDlw6rfhPPQdB04t89/1O/w1cDnyilFU="

app = tk.Tk()
app.title("Line")
app.geometry("500x300")

data = StringVar()

entry = tk.Entry(textvariable=data)
entry.place(x=230,y=100)
def send():
    data_to_send = data.get()

button = tk.Button(app,text="Send Data",command=send)
button.place(x=230,y=150)

app.mainloop()