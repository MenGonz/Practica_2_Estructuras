from List import List

class Stack(List):
    def __init__(self, dato_inicial=None):
        super().__init__(dato_inicial)
        
    def push(self, datos):
        self.addLast(datos)
        
    def pop(self):
        if self.size != 0:
            ret = self.tail.getData()
            self.removeLast()
            return ret
        else:
            return None
        
    def top(self):
        if self.size != 0: 
            return self.tail.getData()
        else:
            return None