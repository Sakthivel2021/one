
no1=1
no2=100
for no in range(no1,no2):
    for div in range(2,no):
        if no%div==0:
            break
        div+=1
    else:
        print(no,"prime number")

