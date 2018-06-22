from tkinter import *
root =Tk()
root.title('Color Me')
root.geometry('300x250+500+250')

def p1():
	root.configure(background='red')

def p2():
	root.configure(background='green')

def p3():
	root.configure(background='blue')


btnRed = Button(root,text='Red',width =10,command=p1)
btnGreen = Button(root,text='Green',width =10,command=p2)
btnBlue = Button(root,text='Blue',width =10,command=p3)

btnRed.pack(pady=20)
btnGreen.pack(pady=20)
btnBlue.pack(pady=20)

root.mainloop()