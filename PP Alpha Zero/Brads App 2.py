from tkinter import *



def newItem(event:None):

    print(strVar.get())

    l1 = Label(root, text=strVar.get())
    l1.pack()

root = Tk()

strVar = StringVar()

en = Entry(root, textvariable=strVar)
en.pack()

chButton = Button(root, text="Enter")
chButton.bind("<Button-1>", newItem)
chButton.pack()

root.mainloop()

