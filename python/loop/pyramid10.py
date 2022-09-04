l,g="",""
h=7
for s in range (1, 6):
    a=""
    j=str(s)
    l=l+j
    g=j+g
    f=" "*h
    h=h-2
    if g=='54321':
        g=g.strip('5')
    a=l+f+g
    print (a)
