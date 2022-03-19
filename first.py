no=int(input('enter number'))
addition=0
count=0
while no>0:
	addition=addition+(no%10)
	no=no//10
	count+=1
else:
	print(addition)	
	print(count)
	