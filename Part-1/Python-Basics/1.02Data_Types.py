'''
===========Data Types==========
Integer
Floating point
Complex
Boolean
String

'''

# Integer

a=8
type(a)
print(a)

# Floating point

b=2.3
type(b)
print(b)

# Complex numbers

c=1+3j
type(c)
print(c)


# Boolean(True,False)

a=True
type(a)
print(a)

b=False
type(b)
print(b)

a=6<3 # False
type(a) #boolean
print(a)

a=6>3 # True
type(a) #boolean
print(a)


# String

my_string="Machine Learning"
type(my_string)
print(my_string)

print(my_string*5) # prints 5 times
print(my_string[1:5]) # slicing => achi ; values from 1 to 5-1 will be printed.
print(my_string[0:10:2]) # 2 is step ; => McieL
word_1='Machine'
word_2=" Learning"
print(word_1+word_2) # string concatination


# convertion of one data type to another

    # int to float
x=10
type(x) # int
print(x)

y=float(x)
type(y) # float
print(y)

    #float to int
x=5.88
type(x) # float
print(x)

y=int(x)
type(y) #int
print(y) # print's only integer value


