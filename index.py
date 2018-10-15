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

#global variables

def displayOnSteve(Data):
    SteveOP.configure(state = "normal")
    SteveOP.delete('1.0',tk.END)
    SteveOP.insert(tk.END,"%s"%Data)
    SteveOP.configure(state = "disabled")

def weatherReq():
    WeatherResponse = req.get("http://api.openweathermap.org/data/2.5/forecast?q=Jalandhar,IND&appid=6c844c5bb5c65e8ec55ab4cf702b96cb")
    displayOnSteve(WeatherResponse.content)


def userEntry():
    userDiag = UserIPBox.get()
    diagFilter(userDiag)

#loginFrame

#mainFrame
Window = tk.Tk()
Window.title("Steve")
Window.geometry("250x400")
Window.configure(bg = "#23223e")
Window.resizable(0,0)

SteveOP = tk.Text(master = Window, width = 28, height = 10,bg = "#c4c1ea", fg = "black" ,highlightbackground = "#14182b",highlightthickness = 3)
SteveOP.grid(pady=10, padx= 7,columnspan = 2)
SteveOP.configure(state="disabled")

UserIPBox = tk.Entry(Window, width = 28, bg = "#c1e1de",highlightbackground = "#14182b", highlightthickness = 3)
UserIPBox.grid(padx = 5 ,pady = 10)

ImgBtn = tk.PhotoImage(file = "speak.png")
UserEntry = tk.Button(Window ,image = ImgBtn, width = 20, height = 20, bg = "#23223e", borderwidth = 0, activebackground = "#23223e", command = userEntry).grid(row = 1, column = 1)

# Module 0.1 - Database

dbConnect = sqlite3.connect("StevesBrain.db")

def userInfoDB():
    username = UserName.get()
    email = UserMail.get()
    usercontact = UserContact.get()
    dbConnect.execute("insert into UserBasic values( %s,%s, %s)", username, email, usercontact)

#Module 1.1-Greetings and User Recognition
uValid = 0

def userValidation(userDiag):
    expIP = userDiag
    global uValid
    regUsers = dbConnect.execute("SELECT UserName FROM UserBasic;")
    for col in regUsers:
        if(expIP == col[0]):
            displayOnSteve("Welcome back %s"%expIP)
            uValid = 1
            time.sleep(1)
            break
        else:
            uValid = 0
            displayOnSteve("Probably this is your first time. Please register to chat :)")

def diagFilter(userDiag):
    global uValid
    if(uValid == 0):
        userValidation(userDiag)



class OnStart(object):
    def __init__(self):
        greeting = dbConnect.execute("SELECT OnStart FROM UserRecog ORDER BY RANDOM() LIMIT 1;")
        for column in greeting:
            displayOnSteve(column[0])

onStart= OnStart()
Window.mainloop()