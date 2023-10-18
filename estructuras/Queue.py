from List import List

class Queue(List):
    def __init__(self, dato_inicial=None):
        super().__init__(dato_inicial)
        
    def enqueue(self, datos):
        self.addLast(datos)
    
    def dequeue(self):
        if self.size != 0:
            ret = self.cabeza.dato
            self.removeFirst()
            return ret
        else:
            return None
        
    def first(self):
        if self.size != 0: 
            return self.cabeza.dato
        else:
            return None