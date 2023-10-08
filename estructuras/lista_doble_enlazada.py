from lista_enlazada import *
from nodo import *

class lista_doble_enlazada(lista_enlazada):
    
    def __init__(self, datos=None):
        if datos != None:
            self.size = 1
            self.cabeza = nodo_simple(datos)
            self.cola = self.cabeza
        else:
            self.size = 0
            
    def add_final(self, datos):
        if self.size == 0:
            self.cabeza = nodo(datos)
            self.cola = self.cabeza
        else:
            nod = nodo(datos)
            nod.prev = self.cola
            self.cola.sig = nod
            self.cola = nod
        self.size += 1
        
    def add_inicio(self, datos):
        if self.size == 0:
            self.cabeza = nodo(datos)
            self.cola = self.cabeza
        else:
            nod = nodo(datos)
            nod.sig = self.cabeza
            self.cabeza.prev = nod
            self.cabeza = nod
        self.size += 1
        
    def remove_inicio(self):
        if self.size != 0:
            self.cabeza = self.cabeza.sig
            self.cabeza.prev = None
            self.size -= 1
    
    def remove_final(self):
        if self.size != 0:
            self.cola = self.cola.prev
            self.cola.sig = None
            self.size -= 1
    
    def get_size(self) -> int:
        return self.size
    
    def buscar_der(self, data) -> bool:
        curr = self.cabeza
        while curr.dato != data and curr.sig != None:
            curr = curr.sig
        if curr.dato == data:
            return True
        else:
            return False
        
    def buscar_izq(self, data) -> bool:
        curr = self.cola
        while curr.dato != data and curr.prev != None:
            curr = curr.prev
        if curr.dato == data:
            return True
        else:
            return False
        
    def buscar_bin(self,data) -> bool:
        
        def mid(nod_inicial, nod_final):
            tortuga = nod_inicial
            liebre = tortuga
            while liebre != nod_final and liebre.sig != nod_final:
                tortuga = tortuga.sig
                liebre = liebre.sig.sig
            return tortuga
        
        right = self.cola
        left = self.cabeza
        while right != left:
            med = mid(left, right)
            if med.dato == data or  right.dato == data:
                return True
            elif med.dato < data:
                left = med.sig
            else:
                right = med
        return False
        
    
    def __str__(self):
        curr = self.cabeza
        s = ""
        while curr != None:
            s += f"{curr.dato} <-> "
            curr = curr.sig
        return s[:-5]