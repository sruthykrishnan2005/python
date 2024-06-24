a=int(input("enter the number of unit"))
if a<=100:
    b=0
    print("no charge")
elif a<=200:
    b=(a-100)*5
    print(b)
elif a>200:
    b=(500)+(a-200)*10
    print(b)
else:
    print("invalid")
