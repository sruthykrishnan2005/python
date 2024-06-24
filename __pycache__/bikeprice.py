a=int(input("enter the cost price"))
b=0
if a>100000:
    b=15/100*a
    print("tax is 15%",b)
elif (a>50000) and (a<=100000):
    b=10/100*a
    print("tax is 10%",b)
elif a<=50000:
    print("tax is 5%",b)
    b=5/100*a
    