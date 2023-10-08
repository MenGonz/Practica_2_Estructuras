
class fila_enlistada(list):
    def __init__(self, dato_inicial=None):
        if dato_inicial is not None:
            self.append(dato_inicial)
    
    def enqueue(self, datos):
        self.append(datos)
    
    def dequeue(self):
        if len(self) != 0:
            return self.pop(0)
        else:
            return None
        
    def peek(self):
        if len(self) != 0: 
            return self[0]
        else:
            return None