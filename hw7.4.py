import math


def cakes(a={}, b={}):
    sumCakes = 0
    min = math.inf
    for i in a:
        need = a[i]
        have = b.get(i,0)
        if have==0 or need>have:
            print(f"Нет ингредиента {a[i]}")
            return
        tmp = b.get(i)//a.get(i)
        if tmp<min:
            min = tmp

    return min

print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))
