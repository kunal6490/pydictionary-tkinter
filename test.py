from tkinter import *
from PyDictionary import PyDictionary as P

d = P()

def set_lab():    
    #var.set("kunal")
    #var.set(str(text_var.get()))
    syn = d.synonym("Life")
    #print(syn)
    meaning.config(text=syn)
    #l.pack()

root = Tk()
root.geometry('400x400')

frame = Frame(root)

frame=Frame(root)
Label(frame, text="Meaning: ", font=("Helvetica 10 bold")).pack(side=LEFT)
meaning = Label(frame, font=("Helvetica 10"))
meaning.pack()
frame.pack(pady=10)

n1 = Button(root, text='Submit', font=("Helvetica 15 bold"), command=set_lab).pack()
#meaning.pack()

root.mainloop()