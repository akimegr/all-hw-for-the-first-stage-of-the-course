
a1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
for i in a1:
    if (int(i)<5):
        b.append(i)

print(list(b))

"_______________"

a = [1,1,2,3,5,8,13,21,34,55,89]
c = [1,2,3,4,5,6,7,8,9,10,11,12,13]
new=[]

for i in a:
    for z in c:
        if(int(i)==int(z)):
            new.append(z)

print(list(new))