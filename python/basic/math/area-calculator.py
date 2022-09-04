import math
while True:
    a = input("Enter the shape for the area(c/C for circle, s/S for square, p/P fpr parallelogroam: ")
    if (a == "c" or a == "C"):
        b = input("enter radius: ")
        f = b.isnumeric()
        if f == True:
            b = int(b)
            c = math.pi * b * b
            print(c, "is the area")
        else:
             print("please enter correct values")   
    elif (a == "s" or a == "S"):
        b = input("enter the side: ")
        f = b.isnumeric()
        if f == True:
            b = int(b)
            c = b * b
            print(c, "is the area")
        else:
             print("please enter correct values")
    elif (a == "p" or a == "P"):
        b = input("enter the length: ")
        d = input("enter the breadth: ")
        f = b.isnumeric()
        g = d.isnumeric()
        if f == True and g == True:
            b = int(b)
            d = int(d)
            c = b * d
            print(c, "is the area")
        else:
             print("please enter correct values")
    else:
        print("please enter correct values")
    e = input("press q to quit and any other key to continue")
    if e == "q":
        break
