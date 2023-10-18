import csv
from Empleado import *
Empleados = []
pwd = []

with open("empleados.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        Empleados.append(empleado)

with open("password.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        pwd.append([row[0], row[1], row[2]])

print(Empleados)
 