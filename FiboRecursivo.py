def FiboRecursivo(n):
	if n==1 or n==2:
		return 1
	return FiboRecursivo(n-1) + FiboRecursivo(n-2)

print(FiboRecursivo(13))
print(FiboRecursivo(22))

