

def array(b=[]):
    a=b.copy()
    min = a[0]
    for i in a:
        if i<min:
            min = i
    check = True
    for i in a:
        if i==min and check:
            a.remove(min)
            check=False
    return a

b=[2,1,3,1,4]
c = array(b)

print(list(b))
print(list(c))