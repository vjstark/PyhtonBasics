import pickle

class Student:
	def __init__(self,rno,name):
		self.rno = rno
		self.name = name
	def showinfo(self):
		print('Rno',self.rno,'Name',self.name)

student=[]
#load file on start
try:
	with open('data.ser','rb') as f:
		student = pickle.load(f)
except:
	pass
while True:
	try:
		op=int(input('1:add student,2: view,3: remove,4: exit'))
		#add student
		if op==1:
			rno = int(input('enter roll no.'))
			name = input('enter name')
			s = Student(rno, name)
			student.append(s)
		#view student
		elif op==2:
			for i in range(len(student)):
				student[i].showinfo()
		#remove student
		elif op==3:
			rno = int(input('enter roll no. to be deleted: '))
			for i in range(len(student)):
				if student[i].rno == rno:
					student.remove(student[i])
					break
		#dump file and exit
		elif op==4:
			with open('data.ser','wb') as f:
				pickle.dump(student,f)
			break
		else:
			print('Invalid Option')
	except ValueError:
		print('You need to enter integers only.')



