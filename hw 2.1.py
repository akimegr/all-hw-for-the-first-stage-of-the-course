b = True
while(b):
    rub = int(input("Количество рублей(выход : -1): "))
    temp = rub
    if(rub==-1):
        b = False
        break
    if(temp>20 ):
        temp%=10
    if (temp==0):
        print(f"{rub} рублей")
    elif (temp == 1):
        print(f"{rub} рубль")
    elif (temp == 2):
        print(f"{rub} рубля")

    elif (temp == 3):
        print(f"{rub} рубля")

    elif (temp == 4):
        print(f"{rub} рубля")
    else:
        print(f"{rub} рублей")
