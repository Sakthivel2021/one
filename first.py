s1=(1,2,3,4,5)
s2=(1,9,3,8,5)

s3=[]
for i in s1:
    
    for j in s2:
         if i==j:
                s3.append(i)
                
print(s3) 