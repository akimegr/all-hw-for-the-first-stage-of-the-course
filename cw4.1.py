import random

a = list(range(12))
i = 0
while(i<len(a)):
    a[i]=random.randint(1,25)
    i+=1
print(list(a))
i=0
max = a[i]
min = a[i]
while(i<len(a)):
    if(a[i]>max):
        max=a[i]
    if(a[i]<min):
        min = a[i]
    i+=1

print(f"max: {max}")
print(f"min: {min}")
