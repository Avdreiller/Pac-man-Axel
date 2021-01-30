import sys
class Dijkstra(object):
    peso = []
    ruta = []
    def minDistance(self, nodosVisit, grafo):
        min = sys.maxsize
        min_index=0
        for v in range(len(grafo)):
            if (nodosVisit[v] == False and self.peso[v] < min):
                min = self.peso[v]
                min_index = v
        return min_index
    def calcular_pesos(self,grafo):
        self.peso = []
        self.ruta = []
        nodosVisit = [] 

        for i in range(len(grafo)):
            self.peso.append(sys.maxsize)
            nodosVisit.append(False)
            self.ruta.append(-1)

        self.peso[0] = 0
        #self.ruta[ini.id] = ini.id 
        
        for count in range(len(grafo)):
            u = self.minDistance(self, nodosVisit, grafo) 
            nodosVisit[u] = True
            for v in range(len(grafo)):
                if nodosVisit[v] != True and grafo[u][v]!=0 and self.peso[u] != sys.maxsize and self.peso[u] + grafo[u][v] < self.peso[v]:
                    self.peso[v] = self.peso[u] + grafo[u][v]
                    self.ruta[v] = u
        for x in range(len(self.peso)):
            if(self.peso[x] == sys.maxsize):
                return False
        return True
    def getCamino(self, ini, fin , grafo ,nodos):
        self.peso = []
        self.ruta = []
        nodosVisit = [] 

        for i in range(len(grafo)):
            self.peso.append(sys.maxsize)
            nodosVisit.append(False)
            self.ruta.append(-1)

        self.peso[ini.id] = 0
        self.ruta[ini.id] = ini.id 
        
        for count in range(len(nodos)):
            u = self.minDistance(self, nodosVisit, grafo) 
            nodosVisit[u] = True
            for v in range(len(nodos)):
                if nodosVisit[v] != True and grafo[u][v]!=0 and self.peso[u] != sys.maxsize and self.peso[u] + grafo[u][v] < self.peso[v]:
                    self.peso[v] = self.peso[u] + grafo[u][v]
                    self.ruta[v] = u
        camino = []
        mien = True
        aux2 = fin.id
        camino.append(fin)
        while(mien == True):
            if self.ruta[aux2]!=-1:
                camino.append(nodos[self.ruta[aux2]])
                if self.ruta[aux2] == ini.id:
                    mien = False
                aux2 = self.ruta[aux2]
            else:
                mien = False
                #return new Respuesta(null,-1)
                return None
        #return new Respuesta(camino,self.peso[fin.getId()])
        return camino

