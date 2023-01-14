def bubblesort(arr):
	i=0
	s=False
	while i<len(arr) and s==False:
		s=True 
		for j in range(len(arr)-1,0,-1):
			if arr[j]<arr[j-1]:
				#swap
				tmp=arr[j]
				arr[j]=arr[j-1]
				arr[j-1]=tmp
				s=False
		i+=1
	return arr
