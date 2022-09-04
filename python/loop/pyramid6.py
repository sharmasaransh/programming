a=""
h=4
for s in range (1, 6):
    j=str(s)
    f= " "*h
    h=h-1
    a=j+a
    print (f,a)
    a=a.replace("5", " ")
k=""
for l in range(4, 0, -1):
    g=str(l)
    print(k,a)
    a=a.replace(g," ")
