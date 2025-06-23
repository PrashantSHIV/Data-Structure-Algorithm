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



if __name__ == "__main__":
    arr = [2,1,6,3,8,5,9]
    print('Before sorting: ',arr)
    # selection_sort(arr)
    bubble_sort(arr)
    print('After sorting: ',arr)





