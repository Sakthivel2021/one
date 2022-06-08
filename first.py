a=[1,9,8,4,0,0,2,7,0,6,0]
for i in a:
    if i==0:
        a.remove(i)
        a.append(i)
        
        
print(a)
