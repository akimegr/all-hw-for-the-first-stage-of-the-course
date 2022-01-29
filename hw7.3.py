

def move_zero(a=[]):
    n=[]
    count = 0
    for i in a:
        if i==0:
            n.append(count)
        count+=1
    minus = 0
    for i in n:
        a.pop(i-minus)
        a.append(0)
        minus+=1

b=[1,5,7,0,5,9,6,0,0,25,15]
move_zero(b)
print(list(b))
