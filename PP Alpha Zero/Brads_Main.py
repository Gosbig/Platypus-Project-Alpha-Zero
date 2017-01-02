#import os
#import scv
from tkinter import *

#from email import email_user
#from converter import csv_converter

class main():

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.new_list_Button = Button(frame, text="Start new list >", command=self.newList)
        self.new_list_Button.grid(row=0, column=0)

        self.edit_list_Button = Button(frame, text="Edit list >", command=self.editList)
        self.edit_list_Button.grid(row=1, column=0)

        self.delete_list_Button = Button(frame, text="Delete list >", command=self.deleteList)
        self.delete_list_Button.grid(row=2, column=0)

    def newList(self):

        def newDict():
            nd = {input}
            nd.Pack(root)

        title = Button(root, text="New List")
        title.pack()



    def editList(self):
        print ("Place holder text for edit List")

    def deleteList(self):
        print ("Place holder text for delete List")


root = Tk()
platypusProjectMain = main(root)
root.mainloop()

