# Searching Algorithms

'''
In Array: Two commonly used algorithms 
    linear search: O(n)
    binary search: O(log n)
'''

# Linear Search

def L_search(arr, N, x):

    for i in range(0,N):
        if x == arr[i]:
            return i
    
    return -1

# Binary Search : ---- Two Implementations

# Iterative Binary Search Algo: using loops 
def B_search(arr,N,x):
    
    i = 0
    j = N-1

    t = 0
    while i <= j:
        t += 1
        mid = i + (j - i)//2

        if arr[mid] == x:
            return mid,t
        elif x < arr[mid]:
            j = mid - 1 
        else:
            i = mid + 1
    
    return -1

# Recursive Binary Search Algo: using recursive function
def RB_search(arr,i,j,x):

    # base case
    if j >= i:
    
    # search mid
        mid = i + (j - i)//2

        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return RB_search(arr,i,mid-1,x)
        else:
            return RB_search(arr,mid+1,j,x)
    
    return -1
'''
Auxiliary Space: O(1), If the recursive call stack is considered then the auxiliary space will be O(log N).'''

# Two Pointer Techniquete
"""
Two-pointer technique uses two variables (pointers) that move through the data structure (like array or string) to solve a problem efficiently.
"""

def Two_sum(arr,N,x):

    i = 0
    j = N-1

    while i != j:
        sum = arr[i] + arr[j]
        
        if sum == x:
            return arr[i],arr[j]
        elif sum < x:
            i += 1
        else:
            j -= 1
    
    return -1


if __name__ == "__main__":
    # arr = [2,4,1,6,3,9,0]
    arr = [1,2,4,5,6,7,8,9]
    N = len(arr)
    x = int(input('Enter the value: '))

    # Function Call
    # result = L_search(arr,N,x)
    # result = RB_search(arr,0,N-1,x)
    result = Two_sum(arr,N,x)
    
    if result == -1:
        print('No pair is present in array')
        # print('Element is not present in array')
    else:
        print(f'Sum is present with pair {result}')
        # print(f'Element is present at index {result[0]} with time {result[1]}')
        # print(f'Element is present at index {result}')
