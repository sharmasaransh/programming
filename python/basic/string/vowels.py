a=input("enter a string: ")
f='AEIOUaeuio'
k=0
for b in a:
    for s in f:
        if s==b:
            print (b, "is a vowel")
    if b not in f:
        print (b, "is a consonent")
    
            
