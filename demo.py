#print ("hellow world!")

#VARIABLES IN PYTHON

# name = "rida"
# age = 19 
# print(name , age) #OUTPUT: rida 19

# DATA TYPES
 
# INT                (numbers_
# X = 10
# Y = 5
# print (X , Y) #OUTPUT: 10 5

#FLOAT              ( decimal )
# pi = 3.14  
# price = 99.99  
# print(pi, price) #OUTPUT: 3.14 99.99

#STR                 (text)
# name = "RIDA"  
# FName = 'KHAN'  
# print(name, FName)  # OUTPUT: RIDA KHAN

#BOOL                (True/False)
# is_adult=True
# is_child=False
# print(is_adult , is_child) # Output: True False

#LIST                (it is more like Array call it with its index number 
#                     .orderd,changable collection can add,remove,Allow duplicates)

# fruits = ["Apple", "Banana", "Mango"]  

# print(fruits[0])  # First item → apple
# print(fruits[1])  # Second item → banana
# print(fruits[-1]) # Last item → mango

# HOW TO CHANGE OR REPLACE?

# fruits = ["Apple", "Banana", "Mango"]
# fruits[0]="cherry"          #OUTPUT: cherry , banana , mango
# fruits[1]="strawberry"      #OUTPUT: cherry , strawberry , mango
# print(fruits)    

#TO ADD AT THE END

# fruits = ["Apple", "Banana", "Mango"]
# fruits.append("orange") 
# print(fruits)  # OUTPUT: ['apple', 'banana', 'mango', 'orange']


#TO REMOVE BY NAME
   
# fruits = ["apple", "banana", "cherry", "mango"]
# fruits.remove("banana")  # Removes "banana" from the list
# print(fruits)

#TUPLE

#A tuple is like a list, but you cannot change it after creating it.
#You cannot, add, or remove items after creating the tuple.
# If you dont want the data to change Tuples are faster than lists.

# fruits = ("apple", "bananna" , "cherry")
# print(fruits[2])

#DICTIONARY (DICT)
#store data in keys-value pairs
#keys must be strings or numbers
#like object , call it with its key word

# person = {
#     "name" : "rida" ,
#     "age" : 19 ,
#     "subject" : "computer" ,
# }

# print(person["name"])

#SET

#unorderd collection of unique items . No duplicates
#A set is a collection of unique items. It does not allow duplicates and is unordered
#Duplicates removed
 
#set = {1,1,2,3,4,5}
# print(set)

#TO ADD 

# set.add(8)
# print(set)

#TO REMOVE 

# set.remove(2)
# print(set)

#TO Checking if an item exists

#print(6 in set)

#SET OPERATORS

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

#print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
#print(set1 & set2)  # Intersection: {3}
#print(set1 - set2)  # Difference: {1, 2}

#FROZENSET

#frozenset is just like a set, but it is unchangeable (immutable).
#Once you create a frozenset, you cannot add or remove items.
#It is useful when you need a fixed set of values that should never change.

# numbers = frozenset(1, 2, 3, 4, 5)
# print(numbers)  # Output: frozenset({1, 2, 3, 4, 5})

