def quicksort(arr):

    n = len(arr)
    
    #Base case
    if n <=1:
        return arr
    
    current_position = 0 #Position of the partitioning element

    for i in range(1,n): #Partitioning loop
         if arr[i] <= arr[0]:
              current_position += 1
              temp = arr[i]
              arr[i] = arr[current_position]
              arr[current_position] = temp

    temp = arr[0]
    arr[0] = arr[current_position] 
    arr[current_position] = temp #Brings pivot to it's appropriate position
    
    left = quicksort(arr[0:current_position]) #Sorts the elements to the left of pivot
    right = quicksort(arr[current_position+1:n]) #sorts the elements to the right of pivot

    arr = left + [arr[current_position]] + right #Merging everything together
    
    return arr

