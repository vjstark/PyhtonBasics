##pp to read name from user and welcome him with GM/GA/GE/GN
import datetime
n = input('Enter your name: ')
dh = datetime.datetime.now().hour
if dh>=0 and dh<=11:
	print('GM',n)
elif dh>11 and dh<=16:
	print('GA',n)
elif dh>16 and dh<20:
	print('GE',n)
elif dh>=20 and dh<=24:
	print('GN',n)