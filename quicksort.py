#quicksort.py
# sort an array, leetcode 912, medium

def quickSort(arr, lo, hi):
    if lo < hi:
        # pi is the partitioning index, arr[p]
        pi = partition(arr, lo, hi)

        quickSort(arr, lo  , pi-1)
        quickSort(arr, pi + 1, hi)

def partition(arr, lo, hi):
    i = lo - 1
    pivot = arr[hi] # use last as pivot

    for j in range(lo, hi):
        # if current element is smaller than pivot
        if arr[j] < pivot:
            # increase index
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[hi] = arr[hi], arr[i+1]

    return i+1


array = [10,7,8,9,1,5]
n = len(array)
quickSort(array, 0, n-1)
print(array)