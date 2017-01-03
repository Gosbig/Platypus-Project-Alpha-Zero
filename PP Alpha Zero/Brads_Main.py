#import os
#import scv
from tkinter import *


#from email import email_user
#from converter import csv_converter



class main():


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.newListBut = Button(frame, text="New List", command=NewList)
        self.newListBut.pack(side=LEFT)

        self.editList = Button(frame, text="Edit List")
        self.editList.pack(side=LEFT)

        self.delList = Button(frame, text="Delete List")
        self.delList.pack(side=LEFT)



class NewList():

    def newitem(self):
        print(strVar.get())


root = Tk()
strVar = StringVar()

strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

entButton = Button(root, text="Enter")
entButton.bind("<Button-1", )
entButton.pack()

infoLabel = Label(root, text=strEntry)
infoLabel.pack()

PlatyApp = main(root)
root.mainloop()

