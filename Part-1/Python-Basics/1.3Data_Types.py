''' 
=========Types of Objects==========
1)Immutable Objects : cannot be changed
2)Mutable Objects : can be changed

Immutable Objects :
    int
    float
    string
    bool
    tuple
    
Mutable Objects :
    List
    Set
    Dictionary

'''

# list : it should be enclosed in [].


my_list=[1,2,3,4,5]
type(my_list) # list
print(my_list)

# it can have Multiple Data types.
my_list=[1,'English',True,1+3j,2.2]

#adding elements to List
my_list.append(6) # add's at the end of the List.
print(my_list)

# printing elements of a list using their index
print(my_list[0])
print(my_list[1])

# it can allow duplicate values
print(len(my_list)) # prints length of the list

# Initiating an empty list
list_1=[]
print(list_1)

# deletion of an element in a List by index
del(my_list[0])
print(my_list)

# join two List's
list_3=[1,2,3]
list_4=[4,5,6]

list_5=list_3+list_4
print(list_5)


# Tuple : it should be enclosed in ().


tuple_1=(1,2,3,4)
type(tuple_1) # tuple
print(tuple_1)

# It can allow multiple Data types

tuple_1=(1,2.2,1+2j,"Praveen",True)
print(tuple_1)

# converting list to a tuple
my_list=[1,2,3,4,5]
my_tuple=tuple(my_list)
print(my_tuple)

# printing elements of a tuple using their index
print(my_tuple[0])
print(my_tuple[1])

# we cannot perform .append() on a list.As it is Immutable. Eg : my_tuple.append(4).
print(len(my_tuple)) # => prints the length of the tuple




# Set : it should be enclosed in {}.


my_set={1,2,3,4}
type(my_set)
print(my_set)

# set does not support indexing.Eg : set[0].

# converting list to a set

list_1=[1,2,3,4,4,5]
my_set=set(list_1)
print(my_set) # => {1,2,3,4,5}

# set does not duplicate values



# Dictionary : It contains a key, value pair.


my_dictionary={
    'Name':"Praveen",
    "Age":20,
    "Country":"India"
}
type(my_dictionary)
print(my_dictionary)
print(my_dictionary["Name"])

# dictionary does not allow duplicate values.


