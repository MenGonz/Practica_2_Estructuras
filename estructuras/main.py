import csv
from Empleado import Empleado
Empleados: list[Empleado] = []
pwd = []

with open("empleados.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        empleado: Empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        Empleados.append(empleado)

with open("password.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        pwd.append([row[0], row[1], row[2]])

user = input("Ingrese su id")
pwd = input("Ingrese la contraseña")
empleado = None
for i in range(len(Empleados)):
    if Empleados[i].get_id() == user:
        if pwd[i][1] == pwd:
            empleado = Empleados[i]
        else:
            print("Contraseña incorrecta")
    else:
        print("Este usuario no existe")

        
        
    
    