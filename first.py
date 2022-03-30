
q=[78,67,76,89,78,67,56,45,78,90]
h=[65,45,35,93,97]
high=len(q) if len(q)>len(h) else len(h)
small=len(q) if len(q)<len(h) else len(h)
a=[]
for i in range(small):
	a.append(q[i]+h[i])

i=high-small
for no in range(i,high):
	a.append(q[no])
	
print(a)	
			 
			 

	