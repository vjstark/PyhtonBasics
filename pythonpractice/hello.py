import sys
try:
    n1= int(sys.argv[1])
    n2= int(sys.argv[2])
    ans = n1/n2
    print("answer=",ans)
except ValueError:
    print('You can only input integers')
except IndexError:
	print('Please enter both the numbers')
except ZeroDivisionError:
    print('you cannot divide by zero')