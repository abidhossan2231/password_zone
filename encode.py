import time
from tkinter import *
import base64
import string
import random
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as ui

co0 = "#00CCCC"
co1 = "#444466"
co2 = "#33FF99"
co3 = "#FFFF66"
co4 = "#FF3333"
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
Pass_Length = IntVar()
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()
Ran_pass = StringVar()

# function to encode
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# function to set mode
def Mode():
    if (mode.get() == 'encode'):
        Result.set(Encode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

# Function to exit window
def Exit():
    MessageBox.askquestion("Confirm", "Are you sure?")
    root.destroy()

# Function to reset
def Reset():
    MessageBox.askquestion("Confirm", "Are you sure?")
    Site_Name.set("")

    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
    Ran_pass.set("")


# Function to save
def Save():
    En_Pass = Result
    if(Unique_ID==0 or Site_Name=="" or En_Pass==""):
        MessageBox.askretrycancel("Saving Password", "try again?")
    else:
        con = mysql.Connect(host="localhost", user="root", password="root", database="passwordzone1")
        cursor = con.cursor()
        cursor.execute("INSERT INTO pass_manager (Unique_ID, Site_Name, En_Pass) VALUES ('%s', '%s', '%s')" % (Unique_ID.get(), Site_Name.get(), En_Pass.get()))
        cursor.execute("commit")
        MessageBox.showinfo("Saving Password", "Successfully save")
        con.close()

def pwd_generator():
    password = ''
    for x in range(0, 4):
        password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(
            string.digits) + random.choice(string.punctuation)
    for y in range(Pass_Length.get() - 4):
        password = password + random.choice(
            string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits)
    Text.set(password)

#################### Label and Button #############

# Qnique ID
Label(root, font='times-new-roman 12 bold', text='Qnique ID', bg=fundo).place(x=120, y=100)
Entry(root, font='times-new-roman 10', textvariable=Unique_ID, bg='ghost white', width=35).place(x=350, y=100)

# Site Name
Label(root, font='times-new-roman 12 bold', text='Site Name', bg=fundo).place(x=120, y=150)
Entry(root, font='times-new-roman 10', textvariable=Site_Name, bg='ghost white', width=35).place(x=350, y=150)

# Password Length
Label(root, font='times-new-roman 12 bold', text='Password Length', bg=fundo).place(x=120, y=200)
length_box=Spinbox(root, font='times-new-roman 12 bold', from_ = 6, to_=32, textvariable=Pass_Length, bg='ghost white', width=26).place(x=350, y=200)

# Message
Label(root, font='times-new-roman 12 bold', text='Random Password', bg=fundo).place(x=120, y=250)
Entry(root, font='times-new-roman 10', textvariable=Text, bg='ghost white', width=35).place(x=350, y=250)

# key
Label(root, font='times-new-roman 12 bold', text='PIN', bg=fundo).place(x=120, y=300)
Entry(root, font='times-new-roman 10', textvariable=private_key, bg='ghost white', width=35).place(x=350, y=300)

# mode
Label(root, font='times-new-roman 12 bold', text='MODE(encode)', bg=fundo).place(x=120, y=350)
Entry(root, font='times-new-roman 10', textvariable=mode, bg='ghost white', width=35).place(x=350, y=350)

# result
Label(root, font='times-new-roman 12 bold', text='Encoded Password', bg=fundo).place(x=120, y=400)
Entry(root, font='times-new-roman 10 bold', textvariable=Result, bg='ghost white', width=35).place(x=350, y=400)
# RANDOM-PASS button
Button(root, font='times-new-roman 10 bold', text='RANDOM-PASS', padx=2, bg=co0, command=pwd_generator).place(x=60, y=500)
# result button
Button(root, font='times-new-roman 10 bold', text='ENCODE', padx=2, bg=co1, command=Mode).place(x=250, y=500)
# save button
Button(root, font='times-new-roman 10 bold', text='SAVE', width=6, command=Save, bg=co2, padx=2).place(x=400, y=500)
# reset button
Button(root, font='times-new-roman 10 bold', text='RESET', width=6, command=Reset, bg=co3, padx=2).place(x=530, y=500)
# exit button
Button(root, font='times-new-roman 10 bold', text='EXIT', width=6, command=Exit, bg=co4, padx=2, pady=2).place(x=670, y=500)
root.mainloop()
