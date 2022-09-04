a=""
h=4
for s in range (1, 6):
    g=""
    j=str(s)
    f= "-"*h
    h=h-1
    a=j+a
    g=f+a
    print (g)
for s in range (5, 0, -1):
    j=str(s)
    a=a.replace(j, "-")
    print (a)
