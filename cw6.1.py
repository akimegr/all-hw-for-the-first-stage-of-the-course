

def search(*args):
    min = args[0]
    for i in args:
        if(min>i):
            min=i
    return min

def main():
    min = search(4,2,1,5,6,-9,13)
    print(f"MIN: {min}")
main()