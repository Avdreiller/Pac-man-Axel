import threading
import time
TOTAL = 0

MY_LOCK = threading.Lock()
class HiloGeneral(threading.Thread):
    def __init__(self, delay, posicion, lista_Tiempo, lista_Validaciones, validacion_Fin, pausa):
        threading.Thread.__init__(self)
        self.delay = delay
        self.lista_Tiempo = lista_Tiempo
        self.lista_Validaciones = lista_Validaciones
        self.posicion = posicion
        self.validacion_Fin = validacion_Fin
        self.pausa = pausa

    def run(self):
        global TOTAL
        contador = 0
        while self.validacion_Fin[0] == True:
            MY_LOCK.acquire()
            if self.pausa[0] == False:
            
                contador = self.lista_Tiempo[self.posicion]
                if contador == self.delay:
                    self.lista_Validaciones[self.posicion] = True
                else:
                
                    contador += 1
                    self.lista_Tiempo[self.posicion]= contador

                TOTAL = TOTAL + 1
            
            MY_LOCK.release()
            time.sleep(1)
            
