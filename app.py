from tkinter import *
import tkinter as tk
import tkinter
import customtkinter
from CTkMessagebox import CTkMessagebox
import random
import threading


class App():
    def __init__(self, root):
        self.toggle = False
        self.frame1 = Frame(root, bg=darkColor)
        self.frame1.pack(fill=tkinter.X)
        self.submitRange = customtkinter.CTkButton(self.frame1, text="Enter", command=self.submit, width=100, height=40,
                                                    font=importantFont)
        self.rangeEntry = customtkinter.CTkEntry(self.frame1, height=40, font=myFont, placeholder_text="Enter range of numbers")
        self.submitRange.pack(side=tk.RIGHT, anchor=NE, expand=True, padx=20, pady=20)
        self.rangeEntry.pack(side=tk.LEFT, anchor = NW, expand=True, padx=20, pady= 20, fill= tkinter.X)

        self.frame2 = Frame(root, bg=darkColor)
        self.frame2.pack(fill=tkinter.BOTH)

        self.frame3 = Frame(root, bg=darkColor)
        self.frame3.pack(fill=tkinter.X, side=tk.BOTTOM)

        self.appearanceButton = customtkinter.CTkButton(self.frame3, text="Mode", command=self.changeMode, width=100, height=40,
                                                    font=importantFont)
        self.appearanceButton.pack(side=tk.BOTTOM, expand=True, padx=20, pady=20)

        self.label = customtkinter.CTkLabel(self.frame2, text="", fg_color="transparent", height=300, font = giantFont)
        self.label.pack(side=tk.TOP, expand=True, padx=20, pady=20, fill=tkinter.BOTH)

    def submit(self):
        try:
            self.range = int(self.rangeEntry.get())
        except:
            return CTkMessagebox(title="Error", message="Enter a numeric value", icon="cancel", font=importantFont2)
        if (self.rangeEntry.get() != None and int(self.rangeEntry.get()) > 0):
            self.counter = 0
            self.set_interval(0.05)
        else:
            return CTkMessagebox(title="Error", message="Enter a positive value", icon="cancel", font=importantFont2)
    
    def set_interval(self, sec):
        self.counter = self.counter + 1
        def func_wrapper():
            self.set_interval(sec)
            self.changeNumber()
        self.t = threading.Timer(sec, func_wrapper)
        if(self.counter >= 60):
            self.t.cancel()
        self.t.start()
        return self.t
    
    def changeNumber(self):
        self.label.configure(text = str(random.randint(1, int(self.rangeEntry.get()))))

    def changeMode(self):
        if(self.toggle):
            customtkinter.set_appearance_mode("dark")
            self.frame1.configure(bg=darkColor)
            self.frame2.configure(bg=darkColor)
            self.frame3.configure(bg=darkColor)
        else:
            customtkinter.set_appearance_mode("light")
            self.frame1.configure(bg=lightColor)
            self.frame2.configure(bg=lightColor)
            self.frame3.configure(bg=lightColor)
        self.toggle = not self.toggle   


root = customtkinter.CTk()
root.title("Tambolla")
root.minsize(600, 600)
root.geometry('600x600')
root.resizable(True, True)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
darkColor = "#222325"
lightColor = "#ebebeb"
myFont = customtkinter.CTkFont(family='Poppins Light', weight='normal', size=15)
importantFont = customtkinter.CTkFont(family='Poppins Light', weight='bold', size=20)
importantFont2 = customtkinter.CTkFont(family='Poppins Light', weight='bold', size=20)
giantFont = customtkinter.CTkFont(family='Poppins Light', weight='bold', size=220)

app =App(root)

root.mainloop()