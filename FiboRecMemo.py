A = {}
def Fibo3(n):
	global A
	if n==0 or n==1:
		return 1
	if n in A:
		return A[n]
	else:
		A[n] = Fibo3(n-2) + Fibo3(n-1)
		return A[n]
print(Fibo3(13))
print(Fibo3(22))