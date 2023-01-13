def insertionsort(arr):
	for i in range(1,len(arr)):
		keyval=arr[i]
		j=i-1
		while j>=0 and arr[j]>keyval:
			#shift the elements
			arr[j+1]=arr[j]
			j-=1
		#insert keyval in the right position
		arr[j+1]=keyval
	return arr
