# Sorting Algorithms:
'''
A sorting algos is used to arrange a given array or list of elements in an order.
'''

# Sorting Basics
'''
* In-place sorting: taking constant space to solve problem. Ex- Selection, Bubble, Insertion, Heap sort.
* Internal sorting: when all the data is placed in main memory or internal memory. and those memory is fixed size.
* External sorting: is when all the data needs to be sorted need not to be placed in memory at a time. Ex- Merge sort
* Stable sorting: Merge sort, insertion, bubble sort.
* Hybrid Sorting: Intro sort uses Insertion and Quick sort.
'''

# Types of Sorting Techniques:
'''
* Comparison-based
* Non-comparison-based: Counting, Radix sort
'''

# SELECTION SORT
'''
comparison-based sorting algorithm. It sorts the array by repeatedly selecting the smallest(or largest) element from the unsorted portion and swapping it with the first unsorted element.
'''


def selection_sort(arr):

    n = len(arr)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
            
        arr[i],arr[min_idx] = arr[min_idx],arr[i]


# Bubble Sort
'''
simplest algo that works by repeatedly swapping the adjacent elements if they are in wrong order.
'''

def bubble_sort(ar):
    
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped: break


# Insertion Sort
'''
Insertion sort is simple sorting algorithm that works by iteratively inserting each element from unsorted list into its correct postion in a sorted portion or list.
'''

def swap(arr,i,j):
    arr[i],arr[j] = arr[j],arr[i]


def insertion_sort(arr):

    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Merge Sort
'''
Merge sort is popular sorting algorithm known for its efficiency and stability. It follows the divide and conquer approach. It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merge them back together to obtain the sorted array.
'''

def merge(arr,beg,mid,end):
    
    n1 = mid - beg + 1
    n2 = end - mid
    sub1 = [0]*n1
    sub2 = [0]*n2

    p = beg
    for i in range(n1):
        sub1[i] = arr[p]
        p += 1
    
    for j in range(n2):
        sub2[j] = arr[p]
        p += 1

    print(sub1,sub2,n1,n2,beg,mid,end,p)

    i = 0
    j = 0
    p = beg

    while i < n1 and j < n2:
        if sub1[i] > sub2[j]:
            arr[p] = sub2[j]
            j += 1
            p += 1

        elif sub1[i] < sub2[j]:
            arr[p] = sub1[i]
            i += 1
            p += 1

    if i < n1:
        arr[p] = sub1[i]
        i += 1
        p += 1

    if j < n2:
        arr[p] = sub2[j]
        j += 1
        p += 1
    
    print(arr[beg:end+1])

def mergesort(arr,i,j):
    if i < j:
        mid = i + (j-i)//2
        mergesort(arr,i,mid)
        mergesort(arr,mid+1,j)
        merge(arr,i,mid,j)
    

                

if __name__ == "__main__":
    arr = [2,1,6,3,8,5,9]
    print('Before sorting: ',arr)
    # selection_sort(arr)
    # bubble_sort(arr)
    # insertion_sort(arr)
    mergesort(arr,0,len(arr)-1)
    print('After sorting: ',arr)





