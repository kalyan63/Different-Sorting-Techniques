print("Enter space seperated input")
num=list(map(int,input().split()))
for i in range(1,len(num)):
    idx=i+1
    while(idx>1):
        if(num[idx-1]>num[idx//2-1]):
            temp=num[idx//2-1]
            num[idx//2-1]=num[idx-1]
            num[idx-1]=temp
        else:
            break    
        idx=idx//2
sort=list()
for i in range(len(num)-1):
    sort.append(num[0])
    print("Heap content : ",num)
    num[0]=num.pop()
    idx=1
    while(idx*2<=len(num)):
        maxidx=0
        if((idx*2+1)>=len(num)):
            maxidx=idx*2
        else:
            maxidx= idx*2 if(num[idx*2-1]>num[idx*2]) else (idx*2+1) 
        if(num[idx-1]>num[maxidx-1]):
            break
        else:
            temp=num[maxidx-1]
            num[maxidx-1]=num[idx-1]
            num[idx-1]=temp    
            idx=maxidx       
sort.append(num[0])
print("sorted list is: ",sort)

