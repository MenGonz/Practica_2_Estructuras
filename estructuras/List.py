from Node import Node

class List:
    
    size: int
    head: Node
    tail: Node
    
    def __init__(self, datos=None):
        if datos != None:
            self.size = 1
            self.head = Node(datos)
            self.tail = self.head
        else:
            self.size = 0
            
    def addLast(self, datos):
        if self.size == 0:
            self.head = Node(datos)
            self.tail = self.head
        else:
            nod: Node = Node(datos)
            self.tail.next = nod
            self.tail = nod
        self.size += 1
        
    def addFirst(self, datos):
        nod: Node = Node(datos)
        if self.size == 0:
            self.head = nod
            self.tail = self.head
        else:
            nod.next = self.head
            self.head = nod
        self.size += 1
        
    def removeFirst(self):
        if self.size != 0:
            self.head = self.head.next
            self.size -= 1
    
    def removeLast(self):
        if self.size != 0:
            curr: Node = self.head
            while curr.next != self.tail:
                curr = curr.next
            curr.next = None
            self.tail = curr
            self.size -= 1
            
    def getSize(self) -> int:
        return self.size
    
    def isEmpty(self) -> bool:
        return self.getSize() == 0
    
    def buscar(self, data) -> bool:
        curr: Node = self.head
        while curr.dato != data and curr.next != None:
            curr = curr.next
        if curr.dato == data:
            return True
        else:
            return False
        
    def buscar_bin(self,data) -> bool:
        
        def mid(nod_inicial: Node, nod_final: Node) -> Node:
            tortuga: Node = nod_inicial
            liebre = tortuga
            while liebre != nod_final and liebre.next != nod_final:
                tortuga = tortuga.next
                liebre = liebre.next.next
            return tortuga
        
        right: Node = self.tail
        left: Node = self.head
        while right != left:
            med = mid(left, right)
            if med.dato == data or  right.dato == data:
                return True
            elif med.dato < data:
                left = med.next
            else:
                right = med
        return False
        
    def __str__(self):
        curr: Node = self.head
        s: str = ""
        while curr != None:
            s += f"{curr.dato} -> "
            curr = curr.sig
        return s[:-4]