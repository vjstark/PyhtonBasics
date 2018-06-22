from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
#import cx_Oracle

#main window using tkinter
root = Tk()
root.title('Student Management System')
root.gemoetry('400x400+200+200')
root.configure(background = 'gray')
#welcome label
Welcome = Label(root, text='Welcome ',font = ('ariel',20,'bold'))
Welcome.pack(pady = 5)
#Add Button
adst = Toplevel(root)
adst.title('Add Student Details')
adst.geometry('400x400+200+200')
adst.withdraw()
#labels to add student name and roll no.
lblRno. = Label(adst,text = 'Enter Roll No.')

lblRno. = Label(adst,text = 'Enter Roll No.')