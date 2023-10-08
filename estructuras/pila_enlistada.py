
class pila_enlistada():
    def __init__(self, dato_inicial=None, limite=-1):
        self.cola = 0
        self.limit = limite
        self.size = 0
        if limite > 0:
            self.pila = tuple(dato_inicial*limite) 
        else:
            self.pila = [dato_inicial]
    
    def push(self, data):
        if self.cola == len(self.pila):
            if self.limite == -1:
                self.pila.append(data)
                self.size += 1
        else:
            self.pila[self.cola] = data
            self.cola += 1
            self.size += 1
            
    def pop(self):
        if self.cola is not None:
            ind = self.cola
            self.pila[ind] = None
            self.cola -= 1
            self.size -= 1
            return self.pila[self.cola]
        
    def get_size(self):
        return self.cola+1
    
    def peek(self):
        return self.pila[self.cola]
    
    def __str__(self):
        res = ""
        for i in range(self.size):
            res += str(i) + " "
        return res