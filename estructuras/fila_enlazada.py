from lista_doble_enlazada import *

class fila_enlazada(lista_doble_enlazada):
    def __init__(self, dato_inicial=None):
        super().__init__(dato_inicial)
        
    def enqueue(self, datos):
        self.add_final(datos)
    
    def dequeue(self):
        if self.size != 0:
            ret = self.cabeza.dato
            self.remove_inicio()
            return ret
        else:
            return None
        
    def peek(self):
        if self.size != 0: 
            return self.cabeza.dato
        else:
            return None