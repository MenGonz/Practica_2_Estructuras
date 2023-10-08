
class pila_enlistada(list):
    def __init__(self, dato_inicial=None):
        if dato_inicial is not None:
            self.append(dato_inicial)
    
    def push(self, datos):
        self.append(datos)
    
    def pop(self):
        if len(self) != 0:
            return self.pop()
        else:
            return None
        
    def peek(self):
        if len(self) != 0: 
            return self[-1]
        else:
            return None