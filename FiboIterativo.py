def FiboIterativo(n):
	f=[1,1]
	for i in range (2, n+1):
		f.append (f[i-1] + f[i-2])
	return f[n]

print(FiboIterativo(13))
print(FiboIterativo(22))