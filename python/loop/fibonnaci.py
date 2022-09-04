a=int(input("enter a number: "))
i,n=1,2
while True:
    # print (i,a,n)
    if i > a or n > a:
        break
    else:
        print (i)
        i=i+n
        print(n)
        n=n+i
