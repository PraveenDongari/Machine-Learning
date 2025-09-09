# Simple if else Statement

a=30
b=50
if (a>b):
    print("a is greater")
else:
    print("b is greater")
    
    

a=int(input("Enter the first Number"))
b=int(input("Enter the Second number"))

if(a>b) :
    print("a is Greater")
else :
    print("b is greater")
    
    


# if elif else Statement

a=15
b=25
c=30

if(a>b and a>c): # or  b<a>c
    print("a is greatest")
elif(b>a and b>c): # or a<b>c
    print("b is greatest")
else :
    print("c is greatest")
    
    
    
    
# Nested if Statement


a=20
b=40
c=60

if(a>b):
    if(a>c):
        print("a is the Greatest")
    else :
        print("c is the Greatest")
else :
    if(b>c):
        print("b is Greatest")
    else :
        print("c is greatest")
