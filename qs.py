def partition (a, start, end):  
    i = (start - 1)  
    pivot = a[end] # pivot element  
      
    for j in range(start, end):  
        # If current element is smaller than or equal to the pivot  
        if (a[j] <= pivot):  
            i = i + 1  
            a[i], a[j] = a[j], a[i]  
      
    a[i+1], a[end] = a[end], a[i+1]  
  
    return (i + 1)  
    

def quick(a, start, end): # a[] = array to be sorted, start = Starting index, end = Ending index      
    if (start < end):  
        p = partition(a, start, end) # p is partitioning index  
        quick(a, start, p - 1)  
        quick(a, p + 1, end)
    return a