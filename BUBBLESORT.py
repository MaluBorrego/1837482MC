def bubbleSort (A):
	for x in range (len(A) -1, 0, -1):
		for i in range (x):
			if A[i] > A[i+1]:
				temp = A[i]
				A[i] = A[i+1]
				A[i+1] = temp
A = [54,26,93,17,77,31,44,55,20]
bubbleSort(A)	
print(A)
