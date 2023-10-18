from Node import Node

class DoubleNode(Node):
    
    def __init__(self, data):
        super().__init__(data)
        self.prev = None
    
    def setPrev(self, prev):
        self.prev = prev
        
    def getPrev(self):
        return self.prev
    