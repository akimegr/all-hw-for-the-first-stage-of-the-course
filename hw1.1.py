a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
p = (a+b+c)/2
print("Half perimetr: ",p)
s = (p*(p-a)*(p-b)*(p-c))**(1/2)
print("Area: ", s)