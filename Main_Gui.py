from tkinter import *
from tkinter import messagebox
from Setup import *
from Data_Base import *
from Admin_panel import *
import os

if not(os.path.isfile("Database.db")):
    Setup()

def Regis_Func(o):
    Regis = Toplevel(app)
    Re_User = StringVar()
    Re_Pass = StringVar()

    def Register_Data():
        User_Data = Re_User.get()
        Pass_Data = Re_Pass.get()
        Write_Register(User_Data,Pass_Data)
        messagebox.showinfo("Done!","Successfully Register")
        Regis.destroy()

    Regis.title("Register")
    Regis.geometry("400x300")
    Re = Label(Regis,text="Register Information",font=("",20)).place(x=100,y=10)
    Log_win2 = Label(Regis,text="Username",font=("",12)).place(x=30,y=70)
    Log2 = Entry(Regis,textvariable=Re_User,width=40).place(x=33,y=100)
    Pass_win2 = Label(Regis,text="Password",font=("",12)).place(x=30,y=140)
    Pass2 = Entry(Regis,textvariable=Re_Pass,width=40,show="*").place(x=33,y=170)
    Log_Button2 = Button(Regis,text="Register",command=Register_Data).place(x=30,y=220)
    Regis.mainloop()

def Login_Func():
    Lo = Login.get()
    Pa = Password.get()
    boo = Check(Lo,Pa)
    if boo == True:
        messagebox.showinfo("Welcome","Welcome to Administrator Panel")
        app.destroy()
        Admin()
    else:
        messagebox.showerror("Error","Either Username or Password is Wrong")

app = Tk()
app.title("KokKok TuRider")
app.geometry("400x300")
app.resizable(0,0)
Login = StringVar()
Password = StringVar()

Welcome = Label(app,text="KokKok TuRider.",font=("",20)).place(x=90,y=10)
Log_win = Label(app,text="Username",font=("",12)).place(x=30,y=70)
Log = Entry(app,textvariable=Login,width=40).place(x=33,y=100)
Pass_win = Label(app,text="Password",font=("",12)).place(x=30,y=140)
Pass = Entry(app,textvariable=Password,width=40,show="*").place(x=33,y=170)
Log_Button = Button(app,text="Login",command=Login_Func).place(x=30,y=220)
New_User = Label(app,text="New User?",font=("",9))

def hover_color(a):
    New_User.config(fg="blue",font=("",9,"underline"))
def hover_color_reverse(b):
    New_User.config(fg="black",font=("",9))

New_User.bind("<Enter>",hover_color)
New_User.bind("<Leave>",hover_color_reverse)
New_User.bind("<Button-1>",Regis_Func)

New_User.place(x=30,y=190)

app.mainloop()