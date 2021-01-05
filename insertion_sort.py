print("Enter space seperated input")
num=list(map(int,input().split()))
for i in range(1,len(num)):
    print(num)
    for j in range(i-1,-1,-1):
        if(num[j+1]<num[j]):
            temp=num[j+1]
            num[j+1]=num[j]
            num[j]=temp
        else:
            break
print("sorted list is: ",num)            
