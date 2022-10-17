import time
from tkinter import *
import base64
import pyperclip
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as ui

fundo = "#3b3b3b"
# initialize window
root = Tk()
root.resizable(0, 0)

window_height = 600
window_width = 800

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width / 2) - (window_width / 2))
y_cordinate = int((screen_height / 2) - (window_height / 1.8))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# title of the window
root.title("PASSWORD ZONE")
root.iconbitmap("images/log.ico")
root.configure(bg=fundo)

# label

Label(root, text='Safety & Security First', font='times-new-roman 24 bold', bg=fundo).pack()
def digital_clock():
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + " " + am_or_pm
    dc.config(text=time_text)
    dc.after(1000, digital_clock)
dc = ui.Label(root, text="00:00:00", font="Helvetica 18 bold", padx=2, bg=fundo)
dc.pack(side=BOTTOM)
digital_clock()

# define variables
Site_Name = StringVar()
Unique_ID = IntVar()
En_Pass = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()
Ran_pass = StringVar()

# function to database
def Take():
    if(Unique_ID==0):
        MessageBox.askretrycancel("Password Getting", "try again?")
    else:
        con = mysql.Connect(host="localhost", user="root", password="root", database="passwordzone1")
        cursor = con.cursor()
        my = "SELECT Site_Name, En_Pass FROM pass_manager WHERE Unique_Id='%s'" % Unique_ID
        cursor.execute(my)
        rows = cursor.fetchone()
        for x in rows:
            Site_Name.get(x[1])
            En_Pass.get(x[2])
        #Unique_ID.configure(stat='disabled')
        MessageBox.showinfo("Password Getting", "Successfully Get")
        con.close()

# function to decode
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)

# function to set mode
def Mode():
    if(En_Pass== "" or private_key== "" or mode== ""):
        MessageBox.askretrycancel("ENCODE TO DECODE", "try again?")
    elif (mode.get() == 'decode'):
        Result.set(Decode(private_key.get(), En_Pass.get()))
    else:
        Result.set('Invalid Mode')

# Function to exit window
def Exit():
    MessageBox.askquestion("Confirm", "Are you sure?")
    root.destroy()

# Add copy to clip board function
def copy_password():
    MessageBox.askquestion("Confirm", "Are you sure?")
    pyperclip.copy(Result.get())

#################### Label and Button #############

# Qnique ID
Label(root, font='times-new-roman 12 bold', text='Qnique ID', bg=fundo).place(x=120, y=150)
Entry(root, font='times-new-roman 10', textvariable=Unique_ID, bg='ghost white', width=35).place(x=350, y=150)

# Site Name
Label(root, font='times-new-roman 12 bold', text='Site Name', bg=fundo).place(x=120, y=200)
Entry(root, font='times-new-roman 10', textvariable=Site_Name, bg='ghost white', width=35).place(x=350, y=200)

# Message
Label(root, font='times-new-roman 12 bold', text='Encoded Password', bg=fundo).place(x=120, y=250)
Entry(root, font='times-new-roman 10', textvariable=En_Pass, bg='ghost white', width=35).place(x=350, y=250)

# key
Label(root, font='times-new-roman 12 bold', text='PIN', bg=fundo).place(x=120, y=300)
Entry(root, font='times-new-roman 10', textvariable=private_key, bg='ghost white', width=35).place(x=350, y=300)

# mode
Label(root, font='times-new-roman 12 bold', text='MODE(decode)', bg=fundo).place(x=120, y=350)
Entry(root, font='times-new-roman 10', textvariable=mode, bg='ghost white', width=35).place(x=350, y=350)

# result
Label(root, font='times-new-roman 12 bold', text='Decoded Password', bg=fundo).place(x=120, y=400)
Entry(root, font='times-new-roman 10 bold', textvariable=Result, bg='ghost white', width=35).place(x=350, y=400)

# DATA-BASE button
Button(root, font='times-new-roman 10 bold', text='Take', padx=2, bg='LightGray', command=Take).place(x=115, y=500)
# result button
Button(root, font='times-new-roman 10 bold', text='DECODE', padx=2, bg='Green', command=Mode).place(x=250, y=500)
# copy password button
Button(root, font='times-new-roman 10 bold', text='COPY TO CLIPBOARD', command=copy_password, bg='Blue', padx=2).place(x=400, y=500)
# exit button
Button(root, font='times-new-roman 10 bold', text='EXIT', width=6, command=Exit, bg='Red', padx=2, pady=2).place(x=630,
                                                                                                                 y=500)
root.mainloop()
