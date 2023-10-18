from Empleado import *
Empleados = []
with open("datos.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        Empleados.append(empleado)

