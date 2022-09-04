a= int(input("enter a number: "))
s= int(input("enter another number: "))
d= int(input("enter another number: "))
if a > s :
    if a > d :
        print("the biggest is ", a)
    
elif s > d :
    if s > a :
        print("the biggest is ", s)

else :
    print ("the biggest is ", d)
