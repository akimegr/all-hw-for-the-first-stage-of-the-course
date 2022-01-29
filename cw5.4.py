

a = int(input("Введите число: "))
b = a**(1/2)
c=b
if c*10000000//10000000==b:
    print(f"Это {c}.TRUE")
else:
    print("FALSE")