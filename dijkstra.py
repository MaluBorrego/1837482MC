class Heap(object):
    def __init__(self):
        self.hp=[0]

    def empty(self):
        return len(self.hp)==1

    def top(self):
        if len(self.hp)>1:
            return self.hp[1]
        else:
            return None

    def push(self,x):
        tam=len(self.hp)
        w=tam
        self.hp.append(x)
        while w>0:
            ww=int(w/2)
            if ww>0:
                if self.hp[ww]>self.hp[w]:
                    self.hp[ww],self.hp[w],w=self.hp[w],self.hp[ww],ww
                else:
                    break
            else:
                break

    def pop(self):
        tam=len(self.hp)-1
        self.hp[1],self.hp[tam]=self.hp[tam],self.hp[1]
        tam-=1
        w=1
        while w<=tam:
            i,d=self.hp[w],self.hp[w]
            if 2*w<=tam:
                i=self.hp[2*w]
            if 2*w+1<=tam:
                d=self.hp[2*w+1]
            if self.hp[w]>i or self.hp[w]>d:
                if i<d:
                    self.hp[w],self.hp[2*w]=self.hp[2*w],self.hp[w]
                    w=2*w
                else:
                    self.hp[w],self.hp[2*w+1]=self.hp[2*w+1],self.hp[w]
                    w=2*w+1
            else:
                break
        return self.hp.pop()

def descomponer(w):
    if w==():
        return []
    (x,y)=w
    return descomponer(y)+[x]

class Grafo(object):
    def __init__(self):
        self.vertices=set()
        self.aristas=dict()
        self.vecinos=dict()
    
    def agrega(self,v):
        self.vertices.add(v)
        if not v in self.vecinos:
            self.vecinos[v]=set()
            
    def conecta(self,u,v,peso=1):
        self.agrega(u)
        self.agrega(v)
        self.aristas[(u,v)]=self.aristas[(v,u)]=peso
        self.vecinos[u].add(v)
        self.vecinos[v].add(u)
        
    @property
    def complemento(self):
        comp=Grafo()
        for a in self.vertices:
            for b in self.vertices:
                if a!=b and (a,b) not in self.aristas:
                    comp.conecta(a,b,1)

    def dijkstra(self,ini):
        bsq=Heap()
        bsq.push((0,ini,()))
        visitados=set()
        respuesta=dict()
        while not bsq.empty():
            (dist,nodo,path)=bsq.pop()
            if nodo in visitados:
                continue
            visitados.add(nodo)
            respuesta[nodo]=(dist,descomponer((nodo,path)))
            for w in self.vecinos[nodo]:
                if w in visitados:
                    continue
                d=self.aristas[(nodo,w)]
                bsq.push((d+dist,w,(nodo,path)))
        return respuesta

    def __str__(self):
        nodos="Vertices:\n"
        for w in self.vertices:
            nodos+=" "+str(w)+" "
        vis=set()
        edges="Aristas:\n"
        for w in self.aristas:
            (x,y)=w
            if w in vis:
                continue
            if (y,x) in vis:
                continue
            vis.add(w)
            edges+=" "+str(w)+":\t"+str(self.aristas[w])+"\n"
        return nodos+"\n"+edges

G1=Grafo()
G1.conecta(1,4,18)
G1.conecta(1,2,11)
G1.conecta(1,3,0)
G1.conecta(1,5,10)
G1.conecta(2,20,8)
G1.conecta(2,6,3)
G1.conecta(2,25,15)
G1.conecta(2,8,13)
G1.conecta(3,4,3)
G1.conecta(4,10,9)
G1.conecta(4,9,14)
G1.conecta(4,5,17)
G1.conecta(5,7,20)
G1.conecta(6,7,5)
G1.conecta(6,8,16)
G1.conecta(6,10,4)
G1.conecta(7,9,8)
G1.conecta(7,10,3)
G1.conecta(8,25,12)
G1.conecta(9,10,6)
G1.conecta(10,4,7)
G1.conecta(11,5,15)
G1.conecta(12,11,9)
G1.conecta(13,2,14)
G1.conecta(14,15,18)
G1.conecta(11,25,1)
G1.conecta(11,7,10)
G1.conecta(13,10,4)
G1.conecta(14,1,3)
G1.conecta(14,8,10)
G1.conecta(14,5,11)
G1.conecta(15,1,2)
G1.conecta(15,5,5)
G1.conecta(15,19,18)
G1.conecta(16,13,20)
G1.conecta(17,3,1)
G1.conecta(18,9,6)
G1.conecta(19,17,13)
G1.conecta(19,11,19)
G1.conecta(18,15,15)
G1.conecta(19,14,8)
G1.conecta(20,1,2)
G1.conecta(20,5,5)
G1.conecta(20,11,18)
G1.conecta(21,6,20)
G1.conecta(22,7,1)
G1.conecta(23,18,6)
G1.conecta(23,3,13)
G1.conecta(24,7,19)
G1.conecta(24,7,15)
G1.conecta(24,15,8)
G1.conecta(21,8,8)

print(G1)
print (G1.dijkstra(7))
