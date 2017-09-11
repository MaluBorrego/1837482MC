def insertionSort (A):
	for index in range (1,len(A)):
		valor = A[i]
		posicion = i
	while posicion > 0 and A[posicion-1]>valor:
		A [posicion] = A[posicion-1]
		posicion = posicion-1		
	A[posicion] = valor

A = [54,26,93,17,77,31,44,55,20]
insertionSort(A)	
print(A)

