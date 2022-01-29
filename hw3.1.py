import random
a = int(input("Введите высоту ёлки от 2 до 20: "))
while(a<2 or a>20):
    a = int(input("Введите высоту ёлки от 2 до 20: "))
k=None
for i in range(a):
    b = a-1
    check = True
    k = None
    for z in range(0,2*a-1):
        if (i % 2 != 0 and check):
            k = random.randint(b-i,b+i)
            check = False
        if (z == k):
            print("o",end="")
        elif (z<=b+i and z>=b-i):
            print("*", end="")

        else:
            print("_", end="")
    print("\n")

