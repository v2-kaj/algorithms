def mergesort(arr):
    if len(arr) <= 1:
        return arr 
    
    # Create start A[start..mid] and end A[mid+1..end]
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    # Sort the two halves
    mergesort(left)
    mergesort(right)

    i = j = k = 0

    # Until we reach the end of either left or right, pick larger among
    # elements start and end and place them in the correct position in the sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # When all elements are traversed in either left or right,
    # pick up the remaining elements and put in sorted array
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr
 
