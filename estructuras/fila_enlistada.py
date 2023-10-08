
class fila_enlistada():
    def __init__(self, dato_inicial=None, limite=-1):
        self.primero = 0
        self.ultimo = 0
        if limite > 0:
            self.fila = tuple(dato_inicial*limite) 
        else:
            self.fila = [dato_inicial]
            
    def enqueue(self, data):
        self.fila[(self.ultimo +1) % len(self.fila)] = data
        self.ultimo = (self.ultimo + 1) % len(self.fila)
        
    def dequeue(self):
        data = self.fila[self.primero]
        self.primero = (self.primero + 1) % len(self.fila)
        return data
    
    def peek(self):
        return self.fila[self.primero]
    
    def is_empty(self):
        return self.primero == self.ultimo
    
    def is_full(self):
        return (self.ultimo + 1) % len(self.fila) == self.primero
    
    def get_size(self):
        return (self.ultimo - self.primero) % len(self.fila) + 1
    
    def __str__(self):
        res = ""
        for i in range(len(self.fila)):
            res += str((self.primero + i) % len(self.fila)) + " "
        return res
    
    