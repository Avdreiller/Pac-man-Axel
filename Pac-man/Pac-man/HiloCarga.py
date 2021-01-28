import threading
import time
import Nodo
import Mapa
import Dijkstra
import Floyd
TOTAL = 0

MY_LOCK = threading.Lock()
class HiloCarga(threading.Thread):
    ruta = []
    nodos = []
    mapa = []
    def __init__(self, lista_Mapas, validacion, numero, accion, ruta2, peso2):
        threading.Thread.__init__(self)
        self.lista_Mapas = lista_Mapas
        self.validacion = validacion
        self.numero = numero
        self.accion = accion
        self.ruta2 = ruta2
        self.peso2 = peso2

    def run(self):
        global TOTAL
            
        
        MY_LOCK.acquire()
        if self.accion == 'J':
            f = Floyd.Floyd()
            self.generar_Ruta(self.obtener_Mapa(self.numero))
            self.ruta2[0], self.peso2[0] = f.pasarPesos(self.ruta)
            self.validacion[0] = True
        elif self.accion == 'C':
            bandera = True
            print("Hilo numero:", self.numero)
            while bandera == True:
                ma = Mapa.Mapa
                m = ma.generar_Mapa(ma)
                self.generar_Ruta(m)
                validar = False
                if self.lista_Mapas is None:
                    validar = True
                else:
                    val = False
                    for x in self.lista_Mapas:
                        if val == False:
                            val = True
                            for i in range(len(x)):
                                for j in range(len(x)):
                                    if self.mapa[i][j] == '#':
                                        if self.mapa[i][j]!=x[i][j]:
                                            val = False
                    if val == False:
                        validar = True
                if validar == True:
                    d = Dijkstra.Dijkstra
                    if d.calcular_pesos(d, self.ruta) == True:
                        bandera = False
            self.lista_Mapas.append(self.mapa)

            self.guardar_Mapa()
            self.validacion[self.numero] = True
            TOTAL = TOTAL + 1
        
        #MY_LOCK.acquire()
        
        #print("Termino:", self.numero)
        
        MY_LOCK.release()
    def obtener_Mapa(self,nivel):
        m =[]
        archivo_texto=open("datos/mapas/Nivel"+str(nivel+1)+".txt","r")
        lineas = []
        for line in archivo_texto:
            lineas.append(line)
        
        for x in range(23):
            m.append([])
            for j in range(23):
                m[x].append(lineas[x][j])
        archivo_texto.close()
        return m
    def generar_Ruta(self, m):
        
        self.mapa = m
        self.mapa_imagenes = []
        contador = 0
        self.nodos = []
        self.ruta = []
        for i in range(len(m)):
            self.mapa_imagenes.append([])
            for j in range(len(m)):
                if m[i][j] != '#' and m[i][j] != ' 'and m[i][j] != '':
                    n = Nodo.Nodo(contador, m[i][j], None, i, j)
                    self.nodos.append(n)
                    id = contador
                    contador += 1

        for x in range(len(self.nodos)):
            self.ruta.append([])
            for j in range(len(self.nodos)):
                self.ruta[x].append(0)

        for i in range(len(self.nodos)):
            for j in range(len(self.nodos)):
                i1,j1 = self.nodos[i].x, self.nodos[i].y
                i2,j2 = self.nodos[j].x, self.nodos[j].y
                if (j1-1 == -1 or j1+1 == len(m)) and (j2-1 == -1 or j2+1 == len(m)):
                    self.ruta[i][j] = 1
                if (i1,j1+1)==(i2,j2) or (i1,j1-1)==(i2,j2) or (i1+1,j1)==(i2,j2) or (i1-1,j1)==(i2,j2):
                    self.ruta[i][j] = 1
    def guardar_Mapa(self):
        n = self.numero
        archivo_texto=open("datos/mapas/Nivel"+str(n+1)+".txt","w")
        cadena = ''
        for i in range(len(self.lista_Mapas[n])):
            cadena = ''
            for j in range(len(self.lista_Mapas[n])):
                cadena += str(self.lista_Mapas[n][i][j])
        
            archivo_texto.write(cadena+"\n")
        archivo_texto.close()
