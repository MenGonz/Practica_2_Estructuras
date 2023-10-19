import csv
from Empleado import Empleado





def mostrar_bandeja_entrada():
    ...
def revisar_mensajes_leidos():
    ...
def proyectar_borrador_guardado():
    ...
def enviar_mensaje():
    ...
def registrar_nuevo_usuario():
    ...
def cambiar_contraseña():
    ...
    
Empleados: list[Empleado] = []
Pwd: list[list[str]] = []

with open("empleados.csv") as datos:
    lector = csv.reader(datos)
    for row in lector:
        empleado: Empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
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
            
if empleado.get_rol() == "empleado":
    print("---------------------Bienvenido empleado------------------------")
    op = input("""Seleccione una opción:
          1. Revisar bandeja de entrada
          2. Revisar mensajes leidos
          3. Proyectar Borrador guardado
          4. Enviar mensaje 
             """)
    
    if op == "1":
        mostrar_bandeja_entrada()
    elif op == "2":
        revisar_mensajes_leidos()
    elif op == "3":
        proyectar_borrador_guardado()
    elif op == "4":
        enviar_mensaje()
    else:
        print("Opción no válida")    
        
    
elif empleado.get_rol() == "administrador":
    op =input("""Seleccione una opción:
        1. Revisar bandeja de entrada
        2. Revisar mensajes leidos
        3. Proyectar Borrador guardado
        4. Enviar mensaje
        5. Registrar nuevo usuario
        6. Cambiar contraseña""")    
    
    if op == "1":
        mostrar_bandeja_entrada()
    elif op == "2":
        revisar_mensajes_leidos()
    elif op == "3":
        proyectar_borrador_guardado()
    elif op == "4":
        enviar_mensaje()
    elif op == "5":
        registrar_nuevo_usuario()
    elif op == "6":
        cambiar_contraseña()
    else:
        print("Opción no válida")
        