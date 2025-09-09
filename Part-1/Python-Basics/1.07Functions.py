# Function  : it is a block of code that can be reused in a program

# Factorial of a number

number=int(input("enter a number"))
def factorial(number):
    if(number==0):
        return 1
    else :
        fact=1
        for i in range(1,number+1,1):
            fact*=i
    return fact
print(factorial(5))
