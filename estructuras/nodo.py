from nodo_simple import *

class nodo(nodo_simple):
    
    def __init__(self, dato):
        super().__init__(dato)
        self.prev = None
    
    def set_prev(self, prev):
        self.prev = prev
    def get_prev(self):
        return self.prev
    