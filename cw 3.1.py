a = 1
max = int(input("Введите число: "))
it = 1
while(it<=max):
    a*=it
    it+=1
print(f"Факториал числа {max} равен {a}")