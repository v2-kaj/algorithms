def binarysearch(arr, num):
	sp=0
	ep=len(arr)-1
	while sp<=ep:
		mp=(sp+ep)//2
		if num==arr[mp]:
			return mp
		elif num<arr[mp]:
			ep=mp-1
		else:
			sp=mp+1
	return -1

