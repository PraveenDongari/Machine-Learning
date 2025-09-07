print("Machine Learning") # Strings
print('Machine Learning')

print("Machine"+" Learning") #concatination

print(8) #number
print(8+3) # 11

# => Single-Line comment

"""Multi-Line
Comment"""

'''Multi-Line
Comment'''




'''
=========Basic Data-Types=====
1)int
2)float
3)str

'''
type(8) # =>int
type(2.3) # =>float
type("Praveen") # =>str



'''
======Constants and variables=====
'''

super_hero='Iron Man' #super_hero => variable
print(super_hero) # => Iron Man

super_hero="spider Man" #changing value of an variable
print(super_hero)

super_hero=10 # changing value with different data type
print(super_hero)

hero1,hero2,hero3="Ironman",'Spider Man',"Captain Marvel" # Creating and Assigning multiple datatypes and variables at a time

print(hero1)
print(hero2)
print(hero3)


x=y=z=23 # single value to multiple variables.

print(x)
print(y)
print(z)



'''
=========Input function============
'''

number_1=input('Enter first Number :') 
number_2=input("Enter Second Number  :")

type(number_1) # => str
type(number_2) # => str

print(number_1)
print(number_2)
print(number_1+number_2) # => concatination

number_1=int(input('Enter first Number :'))
number_2=int(input("Enter Second Number  :"))

type(number_1) # => int
type(number_2) # => int

print(number_1)
print(number_2)
print(number_1+number_2) # addition



'''
=======Changing the Data types=====
'''

num=5
print(float(num))
