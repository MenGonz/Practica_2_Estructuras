
from DoubleNode import DoubleNode

class DoubleList():
    
    size: int
    head: DoubleNode
    tail: DoubleNode
    
    def __init__(self, datos=None):
     self.size = 0
     self.head = None
     self.tail = None
     if datos is not None:
        self.addLast(datos)
            
    def addLast(self, datos):
        if self.size == 0:
            self.head = DoubleNode(datos)
            self.tail = self.head
        else:
            nod: DoubleNode = DoubleNode(datos)
            nod.prev = self.tail
            self.tail.next = nod
            self.tail = nod
        self.size += 1
        
    def addFirst(self, datos):
        if self.size == 0:
            self.head = DoubleNode(datos)
            self.tail = self.head
        else:
            nod: DoubleNode = DoubleNode(datos)
            nod.next = self.head
            self.head.prev = nod
            self.head = nod
        self.size += 1
        
    def removeFirst(self):
      if self.size != 0:
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1

    def removeLast(self):
      if self.size != 0:
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        self.size -= 1
    
    def getSize(self) -> int:
        return self.size
    
    def buscar_der(self, data) -> bool:
        curr: DoubleNode = self.head
        while curr.dato != data and curr.next != None:
            curr = curr.next
        if curr.dato == data:
            return True
        else:
            return False
        
    def buscar_izq(self, data) -> bool:
        curr: DoubleNode = self.tail
        while curr.dato != data and curr.prev != None:
            curr = curr.prev
        if curr.dato == data:
            return True
        else:
            return False
        
    def buscar_bin(self,data) -> bool:
        
        def mid(nod_inicial, nod_final):
            tortuga: DoubleNode = nod_inicial
            liebre = tortuga
            while liebre != nod_final and liebre.next != nod_final:
                tortuga = tortuga.next
                liebre = liebre.next.next
            return tortuga
        
        right: DoubleNode = self.tail
        left: DoubleNode = self.head
        while right != left:
            med: DoubleNode = mid(left, right)
            if med.dato == data or  right.dato == data:
                return True
            elif med.dato < data:
                left = med.next
            else:
                right = med
        return False
        
    
    def __str__(self):
        curr: DoubleNode = self.head
        s = ""
        while curr != None:
            s += f"{curr.dato} <-> "
            curr = curr.next
        return s[:-5]