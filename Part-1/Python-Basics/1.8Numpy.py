# Numpy-Numeric Python .Very Fast than other data types.All elements in a array must be of same type.

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



# Common functions

print(np.mean(b)) # mean
print(np.sum(b))
print(np.min(b))
print(np.max(b))
print(np.std(b)) # standard deviation


# Linear Algebra


A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[6,7]])

print(np.dot(A,B)) # Matrix multiplication
print(np.linalg.inv(A)) # Inverse
print(np.linalg.det(A)) # Determinant
print(np.linalg.eig(A)) # Eigen-Values and Eigen-vectors


# Accessing Elements


arr=np.array([[10,20,30],[40,50,60],[70,80,90]])

# single element
print(arr[0,1]) #20 (row 0,col1)

# whole row
print(arr[1]) #[40,50,60] row1
print(arr[:,2]) # [30,60,,90] col2

# slicing
print(arr[0:2,1:3]) # [[20,30],[50,60]] (sub-array first 2 rows,cols 1-2).



# Inserting Element


a=np.array([1,2,3,4])
print(a)
new_a=np.insert(a,2,99) # insert 99 at index 2
print(new_a)

b=np.array([[1,2],[3,4]])

# insert column
new_b=np.insert(b,1,[9,9] ,axis=1)
print(new_b)
#[[1,9,2]
# [3,9,4]]

# insert row
new_b2=np.insert(b,1,[7,7], axis=0)
print(new_b2)
#[[1,2]
# [7,7]
#[3,4]]



#Deleting Elements


a=np.array([1,2,3,4,5])
new_a=np.delete(a,2) # delete index 2
print(new_a)

b=np.array([[1,2,3],[4,5,6],[7,8,9]])

#delete row
print(np.delete(b,1,axis=0))

#[[1,2,3]
# [7,8,9]]


# delete column
print(np.delete(b,0,axis=1))

#[[2,3]
# [5,6]
# [8,9]]
