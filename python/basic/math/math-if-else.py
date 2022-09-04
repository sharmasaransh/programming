a=input("enter equator: ")
s=int(input("enter No1: "))
d=int(input("enter No2: "))
if a=='add':
    f=s+d
    print ("the sum is", f)
elif a=='subtract':
    f=s-d
    print ("the difference is", f)
elif a=='multiply':
    f=s*d
    print ("the product is", f)
elif a=='divide':
    f=s/d
    print ("the quotient is", f)
else:
    print ("enter correct operator")
