# for loop : used when we know how many times the task should execute

laptop1=int(input("Enter the prize of laptop"))
laptop2=int(input("Enter the prize of laptop"))
laptop3=int(input("Enter the prize of laptop"))
laptop4=int(input("Enter the prize of laptop"))
laptop5=int(input("Enter the prize of laptop"))


for i in range(5): # 0,1,2,3,4
    laptop_prize=int(input("Enter the Prize of the laptop"))
    
    
numbers=[10,100,150,200]

print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

for i in range(len(numbers)):
    print(numbers[i])
    
for i in numbers:
    print(i)



# While Loop : we use when we dont know how many times this code has to be execute
# while(True) : then the code inside the while will be executed


i=0
while(i<10):
    print(i)
    i+=1 # i=i+1
