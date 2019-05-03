#Even Odd finder
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('400x200+500+300')
root.title('EvenOdd Finder')

def evenOdd():
	try:
		n = entNumber.get()
		num = float(n)
		if num % 2 == 0:
			res = 'The number is Even'
			lblAnswer.config(text = 'Even')
		else:
			res = 'The number is Odd'
			lblAnswer.config(text = 'Odd')
		messagebox.showinfo('Result',res)

	except ValueError:
		messagebox.showerror('Issue','Incorrect Input')
		entNumber.delete(0,End)
		entNumber.focus()

def f2():
	ans = messagebox.askyesno('Exit','Do you want to exit the Program?')
	if ans:
		import sys
		sys.exit()

lblNumber = Label(root,text='Enter a number')
lblNumber.place(x=10,y=10)

entNumber = Entry(root,bd=2) #bd: border depth
entNumber.place(x=200,y=10)

btnFind = Button(root, text='Check',command=evenOdd)
btnFind.place(x=150,y=50)
lblAnswer = Label(root,text='')
lblAnswer.pack()
root.protocol('WM_DELETE_WINDOW',f2)
root.mainloop()

