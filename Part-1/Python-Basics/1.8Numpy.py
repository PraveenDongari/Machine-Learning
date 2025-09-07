# Numpy-Numeric Python .Very Fast than other data types

'''
Advantages of Numpy Arrays :
1)Allows several Mathematical Operations
2)Faster Operations

'''

import numpy as np

"""
======List vs Numpy==========

"""

# List

from time import process_time

# process_time() : Time taken by the processer to complete the Task

python_list=[i for i in range(10000)]
start_time=process_time()
python_list=[i+5 for i in python_list]
end_time=process_time()
print(end_time-start_time)


# numpy array

np_array=np.array([i for i in range(10000)])
start_time=process_time()
np_array+=5
end_time=process_time()
print(end_time-start_time)



# Numpy Arrays


np_array=np.array([1,2,3,4,5])
print(np_array)
type(np_array)

# Creating a 1 dimentional Array


a=np.array([1,2,3,4,5])
print(a)
a.shape # => return dimention of the array.(5, )

b=np.array([[1,2,3,4],[5,6,7,8]])
print(b)
b.shape # (2,4)


c=np.array([(1,2,3),(4,5,6)],dtype=float)
print(c)

# initial place-holders
# creating a numpy array of Zeros

x=np.zeros((4,5))
print(x)


# creating a numpy array of 1's

y=np.ones((3,3))
print(y)


# creating a numpy array of perticular value

z=np.full((5,4),5)
print(z)


# creating an identity matrix

a=np.eye(4)
print(a)



# Create a numpy array with random values. 0<=random number<1

b=np.random.random((3,4))
print(b)

# random integer values array within a specific array. Eg:10-100
c=np.random.randint(10,100,(3,5))
print(c)


# array of evenly spaced values --> specifying the number of values required.

d=np.linspace(10,30,5)
print(d)


# array of evenly spaced values --> specifying the step.

e=np.arange(10,30,5)
print(e)


# converting a list to a numpy array.

list2=[10,20,30,40]
np_array=np.asarray(list2)
type(np_array)
print(np_array)


# Number of Dimentions

print(np_array.ndim)


# number of elements in an array

print(np_array.size)


# checking the Data type of the values in the array

print(np_array.dtype)


# Mathematical Operations on a np arrray



list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
print(list1+list2) # => [1,2,3,4,5,6,7,8,9,10].just like Concatination

a=np.random.randint(0,10,(3,3))
b=np.random.randint(10,20,(3,3))
print(a)
print(b)
print(a+b) # element wise addition will be performed
print(a-b)
print(a/b)
print(a*b)

    # OR

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))



# Array manipulation

# Transpose

array=np.random.randint(0,10,(2,3)) # 2,3 Matrix
trans=np.transpose(array)
print(trans) # 3,2 Matrix
print(trans.shape) # (3,2)

# OR

trans2=array.T
print(trans)
print(trans.shape)



# Reshaping a array


a=np.random.randint(0,10,(2,3))
print(a)
print(a.shape)

b=a.reshape(3,2)
print(b)
print(b.shape)
