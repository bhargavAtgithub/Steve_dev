"""Steve in a chat bot.
Steve tries to respond to the user using him.
We, the Developer and Programmers of this project as a team are building this Chatter bot.
This is phase 1 of the project.
In phase 1 its just a simple GUI based project. """

"""Principles to followed by those who are involved in this project.
1) Spacing-
I, strictly recommend not to use any unwanted spaces.
After every loop and function only one line space should be left empty.
2)Indentation should be given by using tabspace.

So understanding the conventions for usage of variables-
Constant Variable names - Upper case 
Class Names should be noun- First letter Uppercase
Methods or Function - Lower CamelCase ->multi-word name that begins with verb in lowercase and Next words first letter in UpperCase.
Variable -Lower CamelCase. But the intent of the usage of the variable should be understood.
Reference for the above conventions - https://en.wikipedia.org/wiki/Naming_convention_(programming)
"""

import sqlite3
import tkinter as tk
import requests as req
import time
import sys
import tkinter.messagebox as tm
import pdb as pdb

# global variables


tempD = ''
uSitu = '.'


def display(Data):
    SteveOP.configure(state="normal")
    SteveOP.delete('1.0', tk.END)
    SteveOP.insert(tk.END, "%s" % Data)
    SteveOP.configure(state="disabled")


def weatherReq():
    WeatherResponse = req.get(
        "http://api.openweathermap.org/data/2.5/forecast?q=Jalandhar,IND&appid=6c844c5bb5c65e8ec55ab4cf702b96cb")
    display(WeatherResponse.content)


def userEntry():
    userDiag = UserIPBox.get()
    print('dialogue received:',userDiag)
    if (userDiag != ''):
        UserIPBox.delete(0, 'end')
        print('Entry: dialogue sent to filter')
        OnStart.diagFilter(userDiag)


# Module 0.1 - Database

brain = sqlite3.connect("StevesBrain.db")

# Module 1.1-Greetings and User Recognition
uValid = 0


class OnStart(object):
    global uSitu
    name = ''
    number = ''
    mail = ''
    locSitu = ''
    loc = ''

    def __init__(self):
        greeting = brain.execute("SELECT OnStart FROM UserRecog ORDER BY RANDOM() LIMIT 1;")
        print("Initial greeting")
        for column in greeting:
            greeting = column[0]
            intro = "Hi! This is Steve\n"+greeting
            display(intro)

    def userValidation(userDiag):
        print("Validator: Dialogue received")
        expIP = userDiag
        global uValid
        regUsers = brain.execute("SELECT UserName FROM UserBasic;")
        for col in regUsers:
            if (expIP.lower() == col[0].lower()):
                print('Validator: Dialogue Received and recognised')
                display("Welcome back %s" % expIP)
                uValid = 1
                time.sleep(1)
                break
            else:
                print('Validator: Dialogue reveived. Couldnt recognise and sent to Investigator(Unknown)')
                uValid = 0
                OnStart.unknown(userDiag)
                print('BreatPoint')
                break
    def unknown(reply):
        print('Investigator: Dialogue received and Processing')
        global uSitu
        if (uSitu == '.' or OnStart.locSitu == ''):
            print('Investigator: Universal situation Locked and processing local situation')
            OnStart.locSitu = 'unknown' + uSitu
            print('Investigator: Uni. situ. and loc. situ. locked')
            if(OnStart.locSitu == 'unknown.' and uSitu == '.'):
                print('Investigator: Enquiry starts')
                display("I'm afraid of talking to strangers :( \nCan I ask you few questions???")
                OnStart.loc = reply.lower()
                if(OnStart.loc == 'yes'):
                        print('Investigator: Yes begining')
                        OnStart.locSitu = 'unknown.y'
                elif(OnStart.loc == 'no'):
                    display("Oops!")
                    sleep(1)
                    Window.destroy()
        if (OnStart.name == '' and OnStart.locSitu == 'unknown.y'):
            question = brain.execute('select Question from NewUserData where Data="name"')
            for que in question:
                display(que)
            uSitu = '.y'
            OnStart.locSitu = 'unknown.yn'
        elif(OnStart.name=='' and OnStart.locSitu == 'unknown.yn'):
            OnStart.name = reply
            OnStart.locSitu = 'unknown.n'
        if(OnStart.number == '' and OnStart.locSitu == 'unknown.n'):
            question = brain.execute('select Question from NewUserData where Data="number"')
            for que in question:
                display(que)
            uSitu = '.y'
            OnStart.locSitu = "unknown.nn"
        elif (OnStart.number == '' and OnStart.locSitu == "unknown.nn"):
                OnStart.number = reply
                OnStart.locSitu = "unknown.nnm"
        if (OnStart.mail == '' and OnStart.locSitu == 'unknown.nnm'):
            question = brain.execute('select Question from NewUserData where Data="mail"')
            for que in question:
                display(que)
            uSitu = '.y'
            OnStart.locSitu = "unknown.nnmm"
        elif (OnStart.mail == '' and OnStart.locSitu == "unknown.nnmm"):
            OnStart.mail = reply
            OnStart.locSitu = ""
        if (OnStart.name != '' and OnStart.number != '' and OnStart.mail != ''):
            done = "It is good to see you in my database " + OnStart.name
            display(done)
            list = [OnStart.name, OnStart.mail, OnStart.number]
            for i in range(len(list)):
               brain.execute("insert into UserBasic(UserName, UserMail, UserNumber) values( ? , ? , ?)", list)
               brain.commit()
        print('Investigator: Process::Ongoing')



    def diagFilter(userDiag):
        global uValid
        global tempD
        print("Filter: Dialogue Received")
        tempD = userDiag
        if (uValid == 0):
            print("Filter: Dialogue Filtered and Sent")
            OnStart.userValidation(userDiag)


# mainFrame
Window = tk.Tk()
Window.title("Steve")
Window.geometry("250x400")
Window.configure(bg="#23223e")
Window.resizable(0, 0)

SteveOP = tk.Text(master=Window, width=28, height=10, bg="#c4c1ea", fg="black", highlightbackground="#14182b",
                  highlightthickness=3)
SteveOP.grid(pady=10, padx=7, columnspan=2)
SteveOP.configure(state="disabled")

UserIPBox = tk.Entry(Window, width=28, bg="#c4c1ea", highlightbackground="#14182b", highlightthickness=3)
UserIPBox.grid(padx=0, pady=10)

ImgBtn = tk.PhotoImage(file="speak.png")
UserEntry = tk.Button(Window, image=ImgBtn, width=20, height=20, bg="#23223e", borderwidth=0,
                      activebackground="#23223e", command=userEntry).grid(row=1, column=1)
UserIPBox.focus()
onStart = OnStart()
Window.mainloop()