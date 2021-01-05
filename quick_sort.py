print("Enter space seperated input")
arr=list(map(int,input().split()))
def quick(num):
    if(len(num)<=1):
        return num
    ele=num.pop(len(num)//2)
    l=list()
    r=list()
    new=list()
    for i in num:
        if(i<=ele):
            l.append(i)
        else:
            r.append(i)     
    l=quick(l)
    r=quick(r)     
    print("left part: ",l," Right part: ",r," Centre element : ",ele)      
    new=l
    new.append(ele)
    new.extend(r)
    print("Combined part : ",new)
    return new
print("Sorted List is: ",quick(arr))    