import sys
class Floyd(object):
    """description of class"""
    peso = []
    recorrido = []

    def pasarPesos(self, m):
        for x in range(len(m)):
            self.peso.append([])
            self.recorrido.append([])
            for j in range(len(m)):
                self.peso[x].append(0)
                self.recorrido[x].append(0)

        for i in range(len(m)):
            for j in range(len(m)):
                if i==j :
                    self.peso[i][j] = 0
                elif m[i][j] == 1:
                    self.peso[i][j] = 1
                else:
                    self.peso[i][j]=sys.maxsize

        for i in range(len(m)):
            for j in range(len(m)):
                if i==j:
                    self.recorrido[j][i] = 0
                else:
                    self.recorrido[j][i] = j
        sum = 0
        for c in range(len(m)):
            for i in range(len(m)):
                if i!=c:
                    for j in range(len(m)):
                        if j!=c and self.peso[i][c]!=sys.maxsize and self.peso[c][j]!=sys.maxsize:
                            sum = self.peso[i][c] + self.peso[c][j]
                            if sum <= self.peso[i][j]:
                                self.peso[i][j] = sum
                                self.recorrido[i][j] = self.recorrido[c][j]


    def getCamino(self, a, b, ca, n):
        camino = []
        
        #self.pasarPesos(self, ca)
        
        
        eva = True
        aux2 = b.id
        aux=0
        camino.append(n[aux2])
        while(eva == True):
            if self.peso[a.id][aux2] != 0 and self.peso[a.id][aux2] != sys.maxsize:
                aux = aux2
                aux2 = self.recorrido[a.id][aux2]
                if aux2 == aux:
                    camino.append(n[a.id])
                    eva = False
                else:
                    camino.append(n[aux2])
            else:
                eva = False
                if self.peso[a.id][aux2] == sys.maxsize:
                    #return new Respuesta(null, -1);
                    return None
        #return new Respuesta(camino, self.peso[a.id][b.id]);
        return camino
