from lista_doble_enlazada import *
from lista_enlazada import *

l = list(map(int, input().split()))
le = lista_enlazada()
lde = lista_doble_enlazada()
for x in l:
    le.add_final(x)
    lde.add_final(x)
    
for x in l:
    print(le.buscar_bin(x+3),end=" ")
print("\n")
for x in l:
    print(lde.buscar_bin(x+3),end=" ")
print("\n")

print(le.get_size())
print(lde.get_size())