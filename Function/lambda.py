# add=lambda a,b:a+b
# print(add(10,5))



def add(a,b):
    return a+b
def sub(a,b):
    return a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b
def numbers():
    a=int(input("enter first num"))
    b=int(input("enter second num"))
    return a,b

while True:
    print("1.add\n 2.sub\n 3.mul\n 4.div\n 5.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        a,b=numbers()
        print(add(a,b))
    elif ch==2:
        a,b=numbers()
        print(sub(a,b))
    elif ch==3:
        a,b=numbers()
        print(mul(a,b))
    elif ch==4:
        a,b=numbers()
        print(div(a,b))
    elif ch==5:
        break

    