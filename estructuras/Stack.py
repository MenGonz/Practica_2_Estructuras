from List import List

class Stack(List):
    def __init__(self, dato_inicial=None):
        super().__init__(dato_inicial)
        
    def push(self, datos):
        self.addLast(datos)
        
    def pop(self):
        if self.size != 0:
            ret = self.cola.dato
            self.removeLast()
            return ret
        else:
            return None
        
    def top(self):
        if self.size != 0: 
            return self.cola.dato
        else:
            return None