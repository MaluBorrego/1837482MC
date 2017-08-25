Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
p = [] 
for i in range(100):
	p.append(i)

def minimo(array):
	aux=array   # creo un arreglo auxiliar
	for n1 in array:   # para cada elemento n1 del arreglo/conjunto
		aux.pop(n1)   # remuevo n1 del conjunto auxiliar
		for n2 in aux:   # para cada elemento n2 del conjunto auxiliar
			print (n1,n2)
			if(n1 > n2):   # comparo si n1 es mayor que n2
				break   # si lo es, salgo para probar el siguiente n1, si no, comparo nl con el siguiente n2
		if resultado
			resultado = n1
			break # ahi muere, salgámonos de aqui
		return resultado
	
