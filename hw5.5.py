

a = int(input("Введите число: "))
ch=a
le=0
i = 0
sp = []
while(a>0):
    tmp = a%10
    sp.append(tmp)
    a//=10
    le+=1
sum = 0
for z in sp:
    sum+=(z**le)
if(sum==ch):
    print("Число самовлюблённое")
else:
    print("Нет")