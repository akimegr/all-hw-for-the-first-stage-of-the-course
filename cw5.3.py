

v = 0
a = []
lst = int(input("Введите число в список: "))
while(v<10):
    g = lst%10
    a.append(g)
    lst//=10
    v+=1

b = int(input("Введите число: "))
c = 0
l = []
check = True
while(c<len(a)):
    if(b==a[c]):
        l.append(c)
        check=False
    c+=1

if(check):
    print("Отсутсвует")
else:
    print(list(l))
    print(list(a.reverse()))