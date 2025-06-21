# Declaration of Array ----
arr = []

# Initialization of Array ----
arr = [1,2,3,4] # integer value
arr = ['a','b','c','d'] # (String in Python)
arr = [1.2,3.8,5.8,7.7] # float values

# Types of Array --------

# Types of array on the basis of size --

# Fixed Sized Array
arr = [1,2,3,4]

# Dynamic Sized Array: (In python array(list) is dynamic)
arr = []

arr.append(5)
print(len(arr)) 
arr.remove(5)
print(len(arr)) 

# Types of array on the basis of dimensions --

# One-dimensional array: like row, elements are stored one after another
arr = [1,2,3,4]
print(arr)

# Multi-dimensional array:
    # Two-dimensional array:  like table, matrix, array of arrays or matrix consisting rows and columns

arr = [[1,2,3],[4,5,6]]
print(arr)
print(arr[0][1])

    # Three-dimensional array: array of two-dimensional arrays, think like building with floors and each floor has rooms
arr = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
print(arr)

# Operations on Array --------

# 1. Array Tranversal
'''Process of accessing and processing each element of an array sequentially'''

# 2. Insertion 
'''
- Identify the position
- Shift Elements
- Insert the New Element
- Updated Size(if applicable): If using a dynamic array, its size is increased.

    Types of Insertion
    1. Insertion at the Beginning
    2. Insertion at the specific index
    3. Insertion at the End

'''

# 3. Deletion
'''
- Identify the Position
- Shift Elements
- Update the Size(if applicable): if using dynamic array, the size might be reduced.
'''

# 4. Searching
    # 1. Linear Search
    # 2. Binary Search