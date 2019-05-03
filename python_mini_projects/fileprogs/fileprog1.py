import os
while True:
	try:
		op= int(input('1:Create File, 2:Delete File, 3:Read File, 4:Write File, 5:Exit : '))
		#Create File
		if op==1:
			fn= input('Enter file name to be created: ')
			if(not os.path.exists(fn)):
				f = open(fn,'a')
				print('File created.')
			else:
				print('File already exists.')
		#Delete File
		elif op==2:
			fn= input('Enter file name to be deleted: ')
			if(os.path.exists(fn)):
				os.remove(fn)
				print(fn +' was deleted.')
			else:
				print('File does not exist.')
		#Read File
		elif op==3:
			fn= input('Enter file name to read: ')
			if(os.path.isfile(fn)):
				f = open(fn)
				data = f.read()
				print(data)
				f.close()
			else:
				print('File does not exist.')
		#Write File
		elif op==4:
			fn = input('Enter file name: ')
			if(os.path.isfile(fn)):
				f=open(fn,'a')
				print('Enter data, pree q to quit. ')
				data = input()
				while  data!='q':
					f.write(data+'\n')
					data=input()
				f.close()
			else:
				print('File does not exist')
			# try:
			# 	fn = input('Enter file name: ')
			# 	if(os.path.isfile(fn)):
			# 		f = open(fn,'a')
			# 		while True:
			# 			op1= int(input('1:Write Line,2: Quit : '))
			# 			if op1 == 1:
			# 				data = input('Enter data to write: ')
			# 				f.write(data+'\n')
			# 			elif op1 == 2:
			# 				f.close()
			# 				break
			# 			else:
			# 				print('Invalid Option')
			# 	else:
			# 		print('File does not exist')
			# except ValueError:
			# 	print('You need to enter integers only')
		#exit the program
		elif op==5:
			break
		#invalid input	
		else:
			print('Invalid Option')

	except ValueError:
		print('You need to enter integers only')

