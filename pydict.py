# Required libraries
from tkinter import *
from PyDictionary import PyDictionary
import requests
from bs4 import BeautifulSoup

# Create Object
dk = PyDictionary()
root = Tk()

# Set geometry
root.geometry('400x400')

# Function for Meaning, Synonym and Antonym
def dicto():    
    tw = StringVar()
    tw = txt_word.get()
    
    mean = dk.meaning(tw)
    synm = dk.meaning(tw)
    antm = dk.meaning(tw)

    a = str(mean)
    b = str(synm)
    c = str(antm)
    
    meaning.config(text=a.replace(",", "\n"))
    synonym.config(text=b.replace(",", "\n"))
    antonym.config(text=c.replace(",", "\n"))
    
def main():
    global meaning
    global synonym
    global antonym
    # Add button, label and frame
    Label(root, text='Dictionary', font=("Helvetica 20 bold"), fg="Green").pack(pady=10)    

    # Frame1
    frame=Frame(root)
    Label(frame, text="Type Word", font=("Helvetica 15 bold")).pack(side=LEFT)
    global txt_word
    txt_word = StringVar()
    word = Entry(frame, font=("Helvetica 15 bold"), textvariable = txt_word)
    word.pack()
    frame.pack(pady=10)

    Button(root, text='Submit', font=("Helvetica 15 bold"), command=dicto).pack()

    # Frame2
    frame1=Frame(root)
    Label(frame1, text="Meaning: ", font=("Helvetica 10 bold")).pack(side=LEFT)
    meaning = Label(frame1, font=("Helvetica 10"), justify=LEFT)
    meaning.pack()
    frame1.pack(pady=10)

    # Frame3
    frame2=Frame(root)
    Label(frame2, text="Synonym: ", font=("Helvetica 10 bold")).pack(side=LEFT)
    synonym = Label(frame2, font=("Helvetica 10"), justify=LEFT)
    synonym.pack()
    frame2.pack(pady=10)

    # Frame4
    frame3=Frame(root)
    Label(frame3, text="Antonym: ", font=("Helvetica 10 bold")).pack(side=LEFT)
    antonym = Label(frame3, font=("Helvetica 10"), justify=LEFT)
    antonym.pack()
    frame3.pack(pady=10)
    
    root.mainloop()

if __name__ == '__main__':
    main()

