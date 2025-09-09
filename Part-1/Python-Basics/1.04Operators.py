'''
=====Operators======

1)Arithmetic Operators
2)Assignment Operators
3)Comparision Operators
4)Logical Operators
5)Identity Operators
6)Membership Operators

'''


# Artthimetic Operators


num_1=20
num_2=10

    # addition
sum=num_1+num_2
print('sum =', sum)

    # subtraction
diff=num_1-num_2
print('difference =' ,diff)

    # multiplication
pro=num_1*num_2
print(pro)

    # division
div=num_1/num_2
print(div)

    # exponent
exp=num_1**num_2 
print(exp)

    # modulus
mod=num_1%num_2
print("Reminder =",mod)




#Assignment Operators


a=5
print(a)

a=5
a+=5 # a=a+5
print(a)

b=5
b-=2 # b=b-2
print(b)

'''

+=
-=
*=
**=
/=
%=

'''



#Comparison Operator


a=5
b=10

print(a==b) # False
print(a!=b) # True
print(a>b) # False
print(a<b) # True
print(a<=b) # True
print(a>=b) # False



# Logical Operator



'''

and
or
not

'''

a=10
print(a>20 and a>5) # False
print(a>10 or a<15) # True
print(not(a>5 and a>=10)) # False



# Identity Operator


'''

is
is not

'''

x=5
y=5

print(x is y) # True
print(x is not y) # False




# Membership Operator


'''

in
not in

'''

a=5
b=10
c=[1,2,3,4,5]
print(a in c) # True
print(b not in c) # True

