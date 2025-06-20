# [------------------------ CORE CONCEPT ------------------------]:

''' Array is a linear data structure that store the similar types of data in contiguous memory location.
    Contiguous memory means the elements stored one after another in memory, like a chain.

    Why use arrays?
    To store multiple values of the same type using a single variable.
    Makes accessing and modifying value easier using indexing. '''

''' Declaring an Array in python.
        Two ways- through python list (but can hold different types of data) and numpy array.

    Go with list:
    
    arr = [] or arr = list()
    where arr - name of array and [] represents empty list object
'''

''' Initialize an Array

    arr = [1,2,3,4] or arr = list((1,2,3,4)) => arr = [1,2,3,4]
        Through len() you can get array size means no. of elements in array
        Syntax: len(arr) = 4
'''

''' Accessing Elements

    arr = [1,2,3,4]

    To access elements of array you can use index no that starts from 0 indicates first element position then index 1 indicates second element position and so on.
    arr[0], arr[1],...,.. arr[size - 1]

    Last index = size of array - 1 = 4 - 1 = 3.
'''

''' Memory Concept

    Arrays are stored in contiguous memory, so each element is right after the previous one.
    If arr[0] is at address 1000 and each int takes 4 bytes, then 
        arr[1] = 1004
        arr[2] = 1008
    
    So arr works like pointer to the first element.
'''

''' Pass Array to Function (Pass by reference)

    def display(arr):
     { Body }

    When we pass the array to a function, we pass the address of the first element (Not a copy).
    So any changes inside the function affect the original array(bcoz it refers to the same memory).
    Array are always passed by reference by default.
'''

''' Null Terminator (\0)

    In C/C++, In character array(String), \0 is used to mark the end of the string.
        Ex- char str[] = {'R','A','M','\0'}
'''

##################### [------------------------ Practice Start ------------------------] #####################

# Creating Array
arr = [1,2,3,4,5,'_']

# Accessing Elements
# print(arr[0],arr[1])

# Insert Element at Beginning by taking input
def InsertBegin(arr):
    value = int(input('Enter the value: '))
    print('Before adding element: ',arr)

    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = value
    print('After adding element: ',arr)

# Insert Element at last by taking input
def InsertLast(arr):
    value = int(input('Enter the value: '))
    print('Before adding element: ',arr)
    arr[len(arr)-1] = value
    print('After adding element: ',arr)

# Insert at Specified index
def InsertSpecified(arr):
    key = int(input('Enter the index position: '))
    value = int(input('Enter the value to place: '))
    print('Before adding element: ',arr)

    i = len(arr) -1
    while(i != key):
        arr[i] = arr[i-1]
        i -= 1
    
    arr[key] = value

    print('After adding element: ',arr)

# Delete element at specified index
def DeleteSpecified(arr):
    key = int(input('Enter key index: '))
    print('Before deleting: ',arr)

    i = key
    while i!=len(arr)-2:
        arr[i] = arr[i+1]
        i += 1
    arr[i] = '_'

    print('After deleting element: ',arr)