class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def setNext(self, next):
        self.next = next
        
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
        
    def getData(self):
        return self.data
    
    def __str__(self):
        return f"N{self.data}-S{str(self.next.data)}"
    