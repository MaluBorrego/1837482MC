def Primo(a):
	if a<=1:
		return NoPrimo
	b=2
	while(b*b<=a):
		if a%b==0:
			return NoPrimo
		m+=1
	return Primo
