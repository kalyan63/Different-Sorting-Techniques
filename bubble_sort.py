print("Enter space seperated input")
num=list(map(int,input().split()))
for i in range(len(num)):
    print(num)
    cnt=0
    for j in range(0,len(num)-i-1):
        if(num[j]>num[j+1]):
            temp=num[j+1]
            num[j+1]=num[j]
            num[j]=temp
            cnt+=1
    # This is used to check if the list is already sorted
    if(cnt==0):
        break        
print("sorted list is: ",num)