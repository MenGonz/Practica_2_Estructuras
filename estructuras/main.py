import csv
from Empleado import *
Empleados: list[Empleado] = []
Pwd = []

with open("empleados.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        Empleados.append(empleado)

with open("password.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        Pwd.append([row[0], row[1], row[2]])

user = input("Ingrese su id")
pwd = input("Ingrese la contraseña")
empleado = None
confirmacion = False
for i in range(len(Empleados)):
    if Empleados[i].get_id() == user:
        if Pwd[i][1] == pwd:
            empleado = Empleados[i]
            confirmacion = True
            empleado.set_pwd(pwd)
            empleado.set_rol(Pwd[i][2])
            break
        else:
            print("Contraseña incorrecta")
        
    
    