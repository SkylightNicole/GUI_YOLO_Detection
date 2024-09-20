import tkinter as tk
from tkinter import StringVar
from tkinter import Toplevel
from tkinter import messagebox
import cv2
from dotenv import load_dotenv
from PIL import Image , ImageTk
from Recog_Vdo import recognized , get_current_frame , get_current_text
from Recog_Img import Img_Reg
from Data_Base import add_more_rider , rider_check
import threading
import subprocess
import os
import requests

check = None
Text_Pic = ""
server_process = None
last_data = None
def Admin():
    def Rider():
        Ride = Toplevel(panel)
        Ride.title("Add more Rider")
        Ride.geometry("500x300")
        plate_id = StringVar()
        name_id = StringVar()
        phone_id = StringVar()
        color_id = StringVar()
        brand_id = StringVar()
        def add():
            pate = plate_id.get()
            pate = pate.lower()
            nae = name_id.get()
            phoe = phone_id.get()
            colo = color_id.get()
            brad = brand_id.get()
            che = add_more_rider(pate,nae,phoe,colo,brad)
            if che == True:
                messagebox.showinfo("Done!","Successfully Add Rider")
            else:
                messagebox.showerror("Error","And Error has occurred")
        Top_Ride = tk.Label(Ride,text="Add Rider Information",font=("",20)).place(x=110,y=10)
        Plate = tk.Label(Ride,text="Plate ID",font=("",12)).place(x=30,y=70)
        Plate_entry = tk.Entry(Ride,textvariable=plate_id,width=17).place(x=33,y=100)
        Name = tk.Label(Ride,text="Name",font=("",12)).place(x=200,y=70)
        name_entry = tk.Entry(Ride,textvariable=name_id,width=17).place(x=203,y=100)
        phone = tk.Label(Ride,text="Phone Number",font=("",12)).place(x=30,y=170)
        phone_entry = tk.Entry(Ride,textvariable=phone_id,width=17).place(x=33,y=200)
        color = tk.Label(Ride,text="Car Color",font=("",12)).place(x=200,y=170)
        color_entry = tk.Entry(Ride,textvariable=color_id,width=17).place(x=203,y=200)
        brand = tk.Label(Ride,text="Car Brand",font=("",12)).place(x=370,y=170)
        brand_entry = tk.Entry(Ride,textvariable=brand_id,width=17).place(x=373,y=200)
        submit = tk.Button(Ride,text="Add",command=add).place(x=30,y=250)

    global process_frame
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
    def Start_Server():
        global server_process , check
        server_script = "Server.py"
        if server_process is None or server_process.poll() is not None:
            server_process = subprocess.Popen(["python",server_script],cwd=os.getcwd())
            messagebox.showinfo("Server Start Successfully")
            check = True
    def Stop_Server():
        global server_process
        if server_process is not None:
            server_process.terminate()
            server_process = None
            print("Server Stopped")
    def resize_frame(frame, target_width=None, target_height=None):
        '''Resize the frame while maintaining aspect ratio.'''
        original_height, original_width = frame.shape[:2]

        if target_width and not target_height:
            # Calculate the new height while maintaining the aspect ratio
            aspect_ratio = original_height / original_width
            target_height = int(target_width * aspect_ratio)
        elif target_height and not target_width:
            # Calculate the new width while maintaining the aspect ratio
            aspect_ratio = original_width / original_height
            target_width = int(target_height * aspect_ratio)
            
        # Resize the frame to the calculated size
        resized_frame = cv2.resize(frame, (target_width, target_height))
        return resized_frame
    def update_frame():
        global Text_Pic
        # Get the current frame from Recog.py
        frame = get_current_frame()
        Text_Pic = get_current_text()
        if Text_Pic is not None:
            Text_Pic = "".join(Text_Pic)
            Text_Pic = Text_Pic.replace(" ","")
            Text_Pic = Text_Pic.lower()
            print(Text_Pic)
        if frame is not None:
            # Resize the frame to fit into the Tkinter window
            frame = resize_frame(frame, target_width=640)  # Adjust the size as needed

            # Convert the frame to ImageTk format for display in Tkinter
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            img_tk = ImageTk.PhotoImage(image=img)

            # Update the label with the new image
            label_video.img_tk = img_tk  # Keep a reference to avoid garbage collection
            label_video.config(image=img_tk)

        # Call update_frame again after 30 milliseconds
        panel.after(30, update_frame)
    def show():
        threading.Thread(target=recognized, daemon=True).start()
        update_frame()
    def show_pic():
        global Text_Pic
        
        Picture,Text = Img_Reg()
        Text_Pic = "".join(Text.copy())
        Text_Pic = Text_Pic.replace(" ","")
        Text_Pic = Text_Pic.lower()
        print(Text_Pic)
        if Picture is not None:
            Picture = resize_frame(Picture.copy(),target_width=640)
            image = cv2.cvtColor(Picture, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            img_tk = ImageTk.PhotoImage(image=image)
            label_video.img_tk = img_tk
            label_video.config(image=img_tk)
    def info_update():
        global Text_Pic , last_data , check
        info = rider_check(Text_Pic)
        if info is None:
            pass
        else:
            plate_name_2.config(fg="green", text=info[0])
            Name_2.config(fg="green", text=info[1])
            Phone_2.config(fg="green", text=info[2])
            Color_2.config(fg="green", text=info[3])
            Car_Brand_2.config(fg="green", text=info[4])
        if check is not None:
            get_request()
        panel.after(1000,info_update)
    def get_request():
        global last_data
        try:
            response = requests.get("http://127.0.0.1:5001/data")  # Adjust URL as needed

            if response.status_code == 200 and response.text:
                data = response.text
                last_data = data
                Order.config(text=last_data,fg="green")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def Send():
        load_dotenv()
        access_token = os.getenv("LINE_AUTH_TOKEN")
        global last_data
        data_to_send = last_data
        status_code = send_line_message(access_token,data_to_send)
        if status_code == 200:
            messagebox.showinfo("Message Sent Successfully")
        else:
            messagebox.showerror(f"Failed to Send message. Status Code : {status_code}")
    panel = tk.Tk()
    panel.title("Administrator")
    panel.geometry("1100x600")
    label_video = tk.Label(panel)
    label_video.place(x=25,y=10)
    plate_name = tk.Label(panel,text="Plate",font=("Arial",18))
    plate_name.place(x=800,y=50)
    plate_name_2 = tk.Label(panel,fg="red", text="No Data",font=("Arial",18))
    plate_name_2.place(x=800,y=100)
    Name = tk.Label(panel,text="Name",font=("Arial",18))
    Name.place(x=700,y=150)
    Name_2 = tk.Label(panel,fg="red", text="No Data",font=("Arial",18))
    Name_2.place(x=700,y=200)
    Phone = tk.Label(panel,text="Phone Number",font=("Arial",18))
    Phone.place(x=900,y=150)
    Phone_2 = tk.Label(panel,fg="red", text="No Data",font=("Arial",18))
    Phone_2.place(x=900,y=200)
    Color = tk.Label(panel,text="Color",font=("Arial",18))
    Color.place(x=700,y=250)
    Color_2 = tk.Label(panel,fg="red", text="No Data",font=("Arial",18))
    Color_2.place(x=700,y=300)
    Car_Brand = tk.Label(panel,text="Car Brand",font=("Arial",18))
    Car_Brand.place(x=900,y=250)
    Car_Brand_2 = tk.Label(panel,fg="red", text="No Data",font=("Arial",18))
    Car_Brand_2.place(x=900,y=300)

    Order = tk.Label(panel,text=0,font=("Arial",18),fg="black")
    Order.place(x=700,y=350)
    Order_Button = tk.Button(panel,text="Send Order",command=Send)
    Order_Button.place(x=700,y=550)

    show_vdo_button = tk.Button(panel,text="Show Video",command=show)
    show_vdo_button.place(x=50,y=500)

    show_img_button = tk.Button(panel,text="Show Picture",command=show_pic)
    show_img_button.place(x=150,y=500)

    Run_Server = tk.Button(panel,text="Start Server",command=Start_Server)
    Run_Server.place(x=50,y=550)

    Add_Rider = tk.Button(panel,text="Add Rider",command=Rider)
    Add_Rider.place(x=150,y=550)
    info_update()
    panel.mainloop()
    Stop_Server()

if __name__ == "__main__" :
    Admin()
