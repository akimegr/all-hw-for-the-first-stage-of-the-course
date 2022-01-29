

def unique_in_order(a):
    arr=[]
    n = 0
    check = True
    while(n<len(a)-1):
        if(a[n]!=a[n+1]):
            arr.append(a[n])
        n+=1
    return arr

b = "AbcdfFAAAABBBBBDDDDFD"
print(unique_in_order(b))



