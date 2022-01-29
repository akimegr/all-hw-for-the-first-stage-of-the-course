


def manTen (a):

    if(a==10 ):
        print("десять", end=" ")
    elif(a==11):
        print("одинадцать", end=" ")
    elif(a==12 ):
        print("двенадцать" , end=" ")
    elif (a==13):
        print("тринадцать" , end=" ")
    elif (a==14):
        print("четырнадцать" , end=" ")
    elif(a==15):
        print("пятнадцать" , end=" ")
    elif(a==16):
        print("шестнадцать", end=" ")
    elif(a==17):
        print("семнадцать" , end=" ")
    elif(a==18):
        print("восемнадцать" , end=" ")
    elif(a==19):
        print("девятнадцать", end=" ")


def manLessThenTen(a):
    a = a
    if(a%10==0):
        print("", end=" ")
    if(a%10==1):
        print("один", end=" ")
    elif(a%10==2):
        print("два" , end=" ")
    elif(a%10==3 ):
        print("три", end=" ")
    elif(a%10==4 ):
        print("четыре", end=" ")
    elif(a%10==5):
        print("пять", end=" ")
    elif(a%10==6 ):
        print("шесть", end=" ")
    elif(a%10==7 ):
        print("семь", end=" ")
    elif(a%10==8 ):
        print("восемь", end=" ")
    elif(a%10==9 ):
        print("девять", end=" ")

def Lesshung(a):

    if (a//10==0):
        print("",end ="")
    if(a//10==2):
        print("двадцать ", end=" ")
    elif (a // 10==3):
        print("тридцать ", end=" ")
    elif (a // 10==4):
        print("сорок ", end=" ")
    elif (a // 10==5):
        print("пятьдесят ", end=" ")
    elif (a // 10 == 6):
        print("шестьдесят ", end=" ")
    elif (a // 10==7):
        print("семьдесят ", end=" ")
    elif (a // 10==8):
        print("восемьдесят ", end=" ")
    elif (a // 10==9):
        print("девяноста ", end=" ")

def Morehung(a):

    if(a//100==0):
        print("", end="")
        return

    if (a // 100 == 1):
        print("сто ", end=" ")
    elif(a//100==2):
        print("двести ", end=" ")
    elif (a // 100==3):
        print("триста ", end=" ")
    elif (a // 100==4):
        print("четыреста ", end=" ")
    elif (a // 100==5):
        print("пятьсот ", end=" ")
    elif (a // 100 == 6):
        print("шестьсот ", end=" ")
    elif (a // 100==7):
        print("семьсот ", end=" ")
    elif (a // 100==8):
        print("восемьсот ", end=" ")
    elif (a // 100==9):
        print("девятьсот ", end=" ")
    a%=100
    return a





def floats(a):

        if (a>99):
            Morehung(a)
            a%=100
        if(a>19 or a<10):
            Lesshung(a)
            manLessThenTen(a)
        else:
            manTen(a)

        # Lesshung(a)
        # if(a//100

def main():
    while (True):
        a = abs(float(input("Введите число: ")))
        a*=1000
        b = a%1000
        a//=1000
        floats(a)
        if (a == 0):
            print("ноль ", end="")

        print("и ", end="")
        if(b==0):
            print("ноль ", end="")
        floats(b)
        print("")
main()


        # if(a<10):
        #     manLessThenTen(a)
        #     print("\n")
        # elif (9<a<21):
        #     manTen(a)
        #     print("\n")
        # elif (21<a<100):
        #     Lesshung(a)
        #     manTen(a)



