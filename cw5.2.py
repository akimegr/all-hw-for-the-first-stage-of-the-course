
a = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

c = int(input("Введите число: "))
if (c>len(a)):

    it = 6
    while(it<c):
        f = it
        z = 0
        while(z<f):
            a.append(f)
            z+=1
        it+=1

i = 0
while(i<c):
    print(a[i], end=" ")
    i+=1