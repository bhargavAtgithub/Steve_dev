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


import tkinter as tk

Window = tk.Tk()
Window.title("Steve")
Window.geometry("250x400")
Window.configure(bg = "#23223e")
Window.resizable(0,0)
SteveOP = tk.Text(master = Window,width = 28,height = 10,bg = "#c4c1ea",highlightbackground = "#14182b",highlightthickness = 3)
SteveOP.grid(pady=10, padx= 7,columnspan = 2)
SteveOP.configure(state="disabled")
UserIP = tk.Entry(Window,width = 28, bg = "#c1e1de",highlightbackground = "#14182b", highlightthickness = 3)
UserIP.grid(padx = 5 ,pady = 10)
ImgBtn = tk.PhotoImage(file = "Untitled-1.png")
UserSend = tk.Button(Window,image = ImgBtn, width = 15, height = 15)
UserSend.grid(row = 1, column = 1)


Window.mainloop()