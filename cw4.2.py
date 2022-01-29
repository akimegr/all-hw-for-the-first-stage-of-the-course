
b = ["abc", "bbb", "sdwd", "bbb"]

for i in b:
    count=0
    b.remove(i)
    for z in b:
        if(i==z):
            count+=1

    if(count>=1):
        print(f"{i} встречается {count} раз")
--------------