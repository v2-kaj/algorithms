def selectionsort(arr):
	for i in range(len(arr)):
		imin=i
		for j in range(i,len(arr)):
			if arr[j]<arr[imin]:
				imin=j
		#swap
		tmp=arr[i]
		arr[i]=arr[imin]
		arr[imin]=tmp
	return arr
