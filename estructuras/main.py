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
    
def menu(empleado: Empleado):
    
    if empleado.get_rol() == "empleado":
        print("---------------------Bienvenido empleado------------------------")
    
        op : str = input("""Seleccione una opción:
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
        print("---------------------Bienvenido administrador------------------------")
    
        op : str =input("""Seleccione una opción:
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


continuar: bool = True
while continuar:
    print("Bienvenido al sistema de mensajería")
    
    user: str = input("Ingrese su id")
    pwd: str = input("Ingrese la contraseña")
    empleado = None
    confirmacion: bool = False
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
            
    menu(empleado)
    continuar = input("¿Desea volver a hacer uso del sistema de mensajería? (si/no)") == "si"
        