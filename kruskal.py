from heapq import heappop, heappush
>>> from copy import deepcopy
>>> import random
>>> import time
>>> def permutation(lst):
	if len(lst) == 0:
		return []
	if len(lst) == 1:
		return [lst]
	l = [] #empty list that will store current permutation
	for i in range(len(lst)):
		m= lst[i]
		remLst = lst[:i] + lst[i+1:]
		for p in permutation(remLst):
			l.append([m] + p)
	return l
	class Fila:
		def __init__(self):
			self.fila= []
		def obtener(self):
			return self.fila.pop()
		def meter(self,e):
			self.fila.insert(0,e)
			return len(self.fila)
		@property
		def longitud(self):
			return len(self.fila)
	class Pila:
		def __init__(self):
			self.pila= []
		def obtener(self):
			return self.pila.pop()
		def meter(self,e):
			self.pila.append(e)
			return len(self.pila)
		@property
		def longitud(self):
			return len(self.pila)
	def flatten(L):
		while len(L) > 0:
			yield L[0]
			L = L[1]
	class Grafo:
		def __init__(self):
			self.V = set() #un conjunto
			self.E = dict() #un mapeo de pesos de aristas
			self.vecinos = dict() #un mapeo
		def agrega(self, v):
			self.V.add(v)
			if not v in self.vecinos: #vecindad de v
				self.vecinos[v] = set() #inicialmente no tiene nada
		def conecta(self, v, u, peso=1):
			self.agrega(v)
			self.agrega(u)
			self.E[(v,u)] = self.E[(u,v)] = peso #en ambos sentidos
			self.vecinos[v].add(u)
			self.vecinos[u].add(v)
		def complemento(self):
			comp= Grafo()
			for v in self.V:
				for w in self.V:
					if v != w and (v, w) not in self.E:
						comp.conecta(v, w, 1)
			return comp
		def BFS(self,ni):
			visitados =[]
			f=Fila()
			f.meter(ni)
			while(f.longitud>0):
				na = f.obtener()
				visitados.append(na)
				ln = self.vecinos[na]
				for nodo in ln:
					if nodo not in visitados:
						f.meter(nodo)
			return visitados
		def DFS(self,ni):
			visitados =[]
			f=Pila()
			f.meter(ni)
			while(f.longitud>0):
				na = f.obtener()
				visitados.append(na)
				ln = self.vecinos[na]
				for nodo in ln:
					if nodo not in visitados:
						f.meter(nodo)
			return visitados
		def shortest(self, v): #Dijkstra´s algorithm
			q = [(0, v, ())] #arreglo "q" de las "Tuplas" de lo que se va a almacenar donde 0 es la distancia, v el nodo y () el "camino" hacia
			dist = dict() #diccionario de distancias
			visited = set() #conjunto de visitados
			while len(q) > 0: #mientras exista un nodo pendiente
				(l, u, p) = heappop(q) #se toma la tupla con la distancia menor
				if u not in visited: #si no lo hemos visitado
					visited.add(u) #se agrega a visitado
					dist[u] = (l,u,list(flatten(p))[::-1] + [u]) #agrega al diccionario
				p = (u, p) #Tupla del nodo y el camino
				for n in self.vecino[u]: #Para cada hijo del nodo actual
					if n not in visited: #si no lo hemos visitado
						el = self.E[(u,n)] #se toma la distancia del nodo actual hacia el nodo hijo
						heappush(q, (l + el, n, p)) #se agrega al arreglo "q" la distancia actual mas la distancia hacia el nodo hijo, el nodo
			return dist #regresa el diccionario de distancias
		def kruskal(self):
			e = deepcopy(self.E)
			arbol = Grafo()
			peso = 0
			comp = dict()
			t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
			nuevo = set()
			while len(t) > 0 and len(nuevo) < len(self.V):
				#print(len(t))
				arista = t.pop()
				w = e[arista]
				del e[arista]
				(u,v) = arista
				c = comp.get(v, {v})
				if u not in c:
					#print('u ',u, 'v ',v , 'c ', c)
					arbol.conecta(u,v,w)
					peso += w
					nuevo = c.union(comp.get(u,{u}))
					for i in nuevo:
						comp[i]= nuevo
			print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
			return arbol
		def vecinoMasCercano(self):
			ni = random.choice(list(self.V))
			result=[ni]
			while len(result) < len(self.V):
				ln = set(self.vecinos[ni])
				le = dict()
				res =(ln-set(result))
				for nv in res:
					le[nv]=self.E[(ni,nv)]
				menor = min(le, key=le.get)
				result.append(menor)
				ni=menor
			return result
	g= Grafo()
	g.conecta(1,2,10.1)
	g.conecta(1,3,9.2)
	g.conecta(1,4,11.8)
	g.conecta(1,5,14.4)
	g.conecta(1,6,10.9)
	g.conecta(1,7,8.7)
	g.conecta(1,8,14.6)
	g.conecta(1,9,12.9)
	g.conecta(1,10,9.1)
	g.conecta(2,3,0.95)
	g.conecta(2,4,1.9)
	g.conecta(2,5,14.3)
	g.conecta(2,6,0.84)
	g.conecta(2,7,1.78)
	g.conecta(2,8,8.1)
	g.conecta(2,9,9.69)
	g.conecta(2,10,2.1)
	g.conecta(3,4,2.8)
	g.conecta(3,5,15.2)
	g.conecta(3,6,1.78)
	g.conecta(3,7,1.2)
	g.conecta(3,8,8.75)
	g.conecta(3,9,10.1)
	g.conecta(3,10,1.79)
	g.conecta(4,5,12.4)
	g.conecta(4,6,1.16)
	g.conecta(4,7,3.71)
	g.conecta(4,8,7.8)
	g.conecta(4,9,8.04)
	g.conecta(4,10,3.89)
	g.conecta(5,6,12.6)
	g.conecta(5,7,16.1)
	g.conecta(5,8,10.4)
	g.conecta(5,9,5.59)
	g.conecta(5,10,16.2)
	g.conecta(6,7,2.58)
	g.conecta(6,8,7.71)
	g.conecta(6,9,9.12)
	g.conecta(6,10,2.73)
	g.conecta(7,8,8.39)
	g.conecta(7,9,11.3)
	g.conecta(7,10,0.85)
	g.conecta(8,9,12.1)
	g.conecta(8,10,7.59)
	g.conecta(9,10,11.7)
	
	print(g.kruskal())
	#print(g.shortest('c'))
	print(g)
	k = g.kruskal()
	print([print(x, k.E[x]) for x in k.E])
	for r in range(10):
		ni = random.choice(list(k.V))
		dfs = k.DFS(ni)
		c = 0
		#print(dfs)
		#print(len(dffs))
		for f in range(len(dfs) -1):
			c += g.E[(dfs[f],dfs[f+1])]
			print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])])
		c += g.E[(dfs[-1],dfs[0])]
		print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
		print('costo',c)
	dfs = g.vecinoMasCercano()
	print(dfs)
	c=0
	for f in range(len(dfs) -1):
		c += g.E[(dfs[f],dfs[f+1])]
		print(dfs[f], dfs[f+1], g.E[(dfs[f],dfs[f+1])])
	c += g.E[(dfs[-1],dfs[0])]
	print(dfs[-1], dfs[0], g.E[(dfs[-1],dfs[0])])
	print('costo',c)
	data = list('MCMGVCSAMZZMO')
	#data = ['mty','saltillo','chi']
	tim=time.clock()
	per = permutation(data)
	print(time.clock()-tim)