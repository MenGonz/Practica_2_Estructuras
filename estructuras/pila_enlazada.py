from lista_enlazada import *

class pila_enlazada(lista_enlazada):
    def __init__(self, dato_inicial=None):
        super().__init__(dato_inicial)
        
    def push(self, datos):
        self.add_final(datos)
        
    def pop(self):
        if self.size != 0:
            ret = self.cola.dato
            self.remove_final()
            return ret
        else:
            return None
        
    def peek(self):
        if self.size != 0: 
            return self.cola.dato
        else:
            return None