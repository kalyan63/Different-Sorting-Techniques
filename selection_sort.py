print("Enter space seperated input")
num=list(map(int,input().split()))
for i in range(len(num)):
    print(num)
    min=i
    for j in range(i+1,len(num)):
        if(num[j]<num[min]):
            min=j
    temp=num[min]
    num[min]=num[i]
    num[i]=temp
print("sorted list is: ",num)             
