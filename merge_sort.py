def merge(a,b):
    c=list()
    idx_a=0
    idx_b=0
    while True:
        if(idx_a<len(a) and idx_b<len(b)):
            if(a[idx_a]<=b[idx_b]):
                c.append(a[idx_a])
                idx_a+=1
            else:
                c.append(b[idx_b])
                idx_b+=1
        elif(idx_b<len(b)):
            c.append(b[idx_b])
            idx_b+=1
        elif(idx_a<len(a)):
            c.append(a[idx_a])
            idx_a+=1
        else:
            break
    return c[:]        

def merge_sort(arr,l,h):
    mid=(l+h)//2
    if(l<h-1):
        merge_sort(arr,l,mid)
        merge_sort(arr,mid,h)
        arr[l:h]=merge(arr[l:mid],arr[mid:h])
        print(arr[l:h]," From index: ",l,h)
    return

def main():
    print("Enter space seperated input")
    num=list(map(int,input().split()))
    count=0
    merge_sort(num,0,len(num))
    print(num)

if __name__=="__main__":
    main()
    
