class nodo_simple():
    
    def __init__(self, dato):
        self.dato = dato
        self.sig = None
        
    def set_sig(self, sig):
        self.sig = sig
        
    def get_sig(self):
        return self.sig
    
    def set_dato(self, dato):
        self.dato = dato
        
    def get_dato(self):
        return self.dato
    
    def __str__(self):
        return f"N{self.dato}-S{str(self.sig.dato)}"
    