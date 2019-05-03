
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Course Feedback')
root.geometry('400x200+300+300')

reason = IntVar()
#set defaul to Excellent
reason.set(1) # if multiple goes to latest
rbExcellent = Radiobutton(root,text='Excellent',variable=reason,value=1)
rbGood = Radiobutton(root,text='Good',variable=reason,value=2)
rbAverage = Radiobutton(root,text='Average',variable=reason,value=3)
rbPoor = Radiobutton(root,text='Poor',variable=reason,value=4)

def f1():
	r = reason.get()
	if r == 1:
		f = 'Excellent'
	elif r == 2:
		f = 'Good'
	elif r == 3:
		f = 'Average'
	else:
		f = 'Poor'
	messagebox.showinfo('Feedback',f)
	import zerosms
	un = '9930215800'
	pw = 'JARVIS67'
	msg = 'Feedback' + f
	sendto = '8639084928'
	zerosms.sms(phno=un,passwd=pw,message=msg,receivernum=sendto)


btnSubmit = Button(root,text='Submit',command=f1)

rbExcellent.grid(sticky='W') #,row=20,column=30
rbGood.grid(sticky='W')
rbAverage.grid(sticky='W')
rbPoor.grid(sticky='W')
btnSubmit.grid()

root.mainloop()