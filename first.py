a=[[1,2,5],
   [3,4,4]]
b=[[2,4,3],
   [4,3,4]]
c=[[0,0,0],
   [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
        
for k in c:
    print(k)
