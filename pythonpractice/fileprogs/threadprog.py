import threading

class Even(threading.Thread):
	def run(self):
		print('even thread starts')
		f1 = open('data.txt')
		f2 = open('even.txt','a')
		data = f1.readline()
		while data:
			if int(data)%2 == 0:
				f2.write(data + '\n')
			data = f1.readline()
		f1.close()
		f2.close()
		print('even thread ends')

class Odd(threading.Thread):
	def run(self):
		print('odd thread starts')
		f1 = open('data.txt')
		f2 = open('odd.txt','a')
		data = f1.readline()
		while data:
			if int(data)%2 != 0:
				f2.write(data + '\n')
			data = f1.readline()
		f1.close()
		f2.close()
		print('odd thread ends')


print('processing begins')
t1 = Even()
t2 = Odd()
t1.start()
t2.start()
t1.join()
t2.join()
print('processing ends')