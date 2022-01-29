a = input("Введите 1: ")
c = ''
if(len(a)<2 ):
    c = ''
    print(c)
else:
    c = a[0:2] + a[-2:len(a)]
    print(c)