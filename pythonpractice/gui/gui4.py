from tkinter import *
from tkinter import messagebox
#Window
root = Tk()
root.title('Course Material')
root.geometry('400x200+300+300')
#Label
need = Label(root,text='Course Material req.',font=('ariel',18,'bold'))
need.grid()

m1 = IntVar()
m11 = Checkbutton(root,text='Notes',variable=m1,font=('ariel',18,'bold'))
m11.grid(sticky='W')

m2 = IntVar()
m22 = Checkbutton(root,text='DVD',variable=m2,font=('ariel',18,'bold'))
m22.grid(sticky='W')

m3 = IntVar()
m33 = Checkbutton(root,text='Certificate',variable=m3,font=('ariel',18,'bold'))
m33.grid(sticky='W')

m4 = IntVar()
m44 = Checkbutton(root,text='PPT',variable=m4,font=('ariel',18,'bold'))
m44.grid(sticky='W')

def f1():
	msg=''
	if m1.get() == 1:
		msg = msg + 'Notes' + '\n'
	if m2.get() == 1:
		msg = msg + 'DVD' + '\n'
	if m3.get() == 1:
		msg = msg + 'Certificate' + '\n'
	if m4.get() == 1:
		msg = msg + 'PPT' + '\n'
	messagebox.showinfo('Material received',msg)

	to = 'kamalsir@ymail.com'
	subject = 'Materials received by Virat'
	text = msg
	import smtplib
	sender = 'starkenterprises.vj@gmail.com'
	password = 'jaeger7931cdcrimsontyphoon'
	message = 'Subject: {}\n\n{}'.format(subject,text)
	server = smtplib.SMTP_SSL('smtp.gmail.com',465)
	server.ehlo()
	server.login(sender,password)
	print('logged in')

	try:
		server.sendmail(sender,to,message)
		print('email sent')
	except:
		print('error sending mail')

	server.quit

submit = Button(root,text='Submit',command=f1,font=('ariel',18,'bold'))
submit.grid()
root.mainloop()