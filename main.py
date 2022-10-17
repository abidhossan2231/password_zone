import time
from tkinter import *
import base64
import string
import random
import mysql
import pyperclip
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import tkinter as ui
def home():
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
    pz = PhotoImage(file="images\logo.png")
    Label(root, image=pz).place(x=270, y=125)
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

    # Function to create window
    def cr():
        root.destroy()
        create()

    # Function to take window
    def ta():
        root.destroy()
        take()

    # Function to update window
    def ud():
        root.destroy()
        update()

    # Function to about window
    def ab():
        root.destroy()
        about()

    # Function to exit window
    def exit():
        MessageBox.askquestion("Confirm", "Are you sure?")
        root.destroy()

    # button images
    cp = PhotoImage(file="images\create-pass.png")
    tp = PhotoImage(file="images\ke-pass.png")
    up = PhotoImage(file="images\pdate-pass.png")
    ap = PhotoImage(file="images\out.png")
    ep = PhotoImage(file="images\exit.png")

    # Password Create button
    Button(root, image=cp, command=cr, bg=fundo, borderwidth=5).place(x=60, y=110)
    # Take Password button
    Button(root, image=tp, command=ta, bg=fundo, borderwidth=5).place(x=60, y=190)
    # Update Password button
    Button(root, image=up, command=ud, bg=fundo, borderwidth=5).place(x=60, y=270)
    # About button
    Button(root, image=ap, bg=fundo, command=ab, borderwidth=5).place(x=60, y=350)
    # exit button
    Button(root, image=ep, command=exit, bg=fundo, borderwidth=5).place(x=60, y=430)

    root.mainloop()

def create():
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
        if (Unique_ID == "" or Site_Name == "" or En_Pass == ""):
            MessageBox.askretrycancel("Saving Password", "try again?")
        else:
            con = mysql.connect(host="localhost", port="3306", user="root", password="", database="passwordzone")
            cursor = con.cursor()
            cursor.execute("INSERT INTO pass_manager (Unique_ID, Site_Name, En_Pass) VALUES ('%s', '%s', '%s')" % (
            Unique_ID.get(), Site_Name.get(), En_Pass.get()))
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

    #back function
    def back():
        root.destroy()
        home()
    #################### Label and Button ###############

    # unique ID
    Label(root, font='times-new-roman 12 bold', text='unique ID', bg=fundo).place(x=120, y=100)
    Entry(root, font='times-new-roman 10', textvariable=Unique_ID, bg='ghost white', width=35).place(x=350, y=100)

    # Site Name
    Label(root, font='times-new-roman 12 bold', text='Site Name', bg=fundo).place(x=120, y=150)
    Entry(root, font='times-new-roman 10', textvariable=Site_Name, bg='ghost white', width=35).place(x=350, y=150)

    # Password Length
    Label(root, font='times-new-roman 12 bold', text='Password Length', bg=fundo).place(x=120, y=200)
    length_box = Spinbox(root, font='times-new-roman 12 bold', from_=6, to_=32, textvariable=Pass_Length,
                         bg='ghost white', width=26).place(x=350, y=200)

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

    # button images
    rnp = PhotoImage(file="images\on_random-pass.png")
    np = PhotoImage(file="images\on_encode.png")
    sp = PhotoImage(file="images\on_save.png")
    rp = PhotoImage(file="images\on_reset.png")
    bp = PhotoImage(file="images\on_back.png")

    # RANDOM-PASS button
    Button(root, image=rnp, command=pwd_generator, bg=fundo, borderwidth=5).place(x=45, y=500)
    # result button
    Button(root, image=np, bg=fundo, command=Mode, borderwidth=5).place(x=195, y=500)
    # save button
    Button(root, image=sp, command=Save, bg=fundo,  borderwidth=5).place(x=345, y=500)
    # reset button
    Button(root, image=rp, command=Reset, bg=fundo,  borderwidth=5).place(x=495, y=500)
    # exit button
    Button(root, image=bp, command=back, bg=fundo,  borderwidth=5).place(x=645, y=500)

    root.mainloop()

def take():
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
        Unique_ID.get()
        Site_Name.get()
        En_Pass.get()
        if (Unique_ID == 0):
            MessageBox.askretrycancel("Password Getting", "try again?")
        else:
            con = mysql.Connect(host="localhost", port="3306", user="root", password="", database="passwordzone")
            cursor = con.cursor()
            try:
                cursor.execute("SELECT * FROM pass_manager WHERE Unique_ID='%s'" % Unique_ID)
                rows = cursor.fetchall()
                for x in rows:
                    print(x)
                    Site_Name.delete(0, END)
                    Site_Name.insert(END, x[2])
                    En_Pass.delete(0, END)
                    En_Pass.insert(END, x[3])
            except Exception as e:
                print(e)
                con.rollback()
                con.close()
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
        if (En_Pass == "" or private_key == "" or mode == ""):
            MessageBox.askretrycancel("ENCODE TO DECODE", "try again?")
        elif (mode.get() == 'decode'):
            Result.set(Decode(private_key.get(), En_Pass.get()))
        else:
            Result.set('Invalid Mode')

    # Add copy to clip board function
    def copy_password():
        MessageBox.askquestion("Confirm", "Are you sure?")
        pyperclip.copy(Result.get())

    #back function
    def back():
        root.destroy()
        home()
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

    # button images
    tp = PhotoImage(file="images\on_get.png")
    dp = PhotoImage(file="images\on_decode.png")
    cp = PhotoImage(file="images\on_clipboard.png")
    bp = PhotoImage(file="images\on_back.png")

    # DATA-BASE button
    Button(root, image=tp, bg=fundo, command=Take,  borderwidth=5).place(x=115, y=500)
    # result button
    Button(root, image=dp, bg=fundo, command=Mode,  borderwidth=5).place(x=275, y=500)
    # copy password button
    Button(root, image=cp, command=copy_password, bg=fundo,  borderwidth=5).place(x=435, y=500)
    # back button
    Button(root, image=bp, command=back, bg=fundo,  borderwidth=5).place(x=595, y=500)

    root.mainloop()

def update():
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
    pz = PhotoImage(file="images\logo.png")
    Label(root, image=pz).place(x=270, y=125)
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

    #back function
    def back():
        root.destroy()
        home()

    #button image
    bp = PhotoImage(file="images\on_back.png")

    # back button
    Button(root, image=bp, command=back, bg=fundo, borderwidth=5).place(x=595, y=500)

    root.mainloop()

def about():
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
    pz = PhotoImage(file="images\logo.png")
    Label(root, image=pz).place(x=270, y=125)
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

    # back function
    def back():
        root.destroy()
        home()

    # button image
    bp = PhotoImage(file="images\on_back.png")

    # back button
    Button(root, image=bp, command=back, bg=fundo, borderwidth=5).place(x=595, y=500)

    root.mainloop()

home()
