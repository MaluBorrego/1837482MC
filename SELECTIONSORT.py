def selection (A):
    for i in range (0,len(A)-1):
        valor=i
        for j in range(i+1, len(A)):
            if A[j]<A[valor]:
                val=j
        if valor !=i:
            aux=A[i]
            A[i]=A[valor]
            A[valor]=aux
    return A

A = [54,26,93,17,77,31,44,55,20]
selection(A)	
print(A)

