def quicksort(A):
    valor=0
    if A==[] :
        return []
    m=A[0]
    left=[]
    right=[]
    for k in A[1:]:
        if k<m:
            left.append(k)
        else:
            right.append(k)
        valor+=1
    return quicksort(left)+[m]+quicksort(right)

A = [54,26,93,17,77,31,44,55,20]
quicksort(A)	
print(A)
