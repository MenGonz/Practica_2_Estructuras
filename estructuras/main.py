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
    #Obtiene la informacion
    nombre = input("Ingrese el nombre del usuario: ")
    id = input("Ingrese el id del usuario: ")
    fecha_nac = input("Ingrese la fecha de nacimiento del usuario: ")
    ciudad_nac = input("Ingrese la ciudad de nacimiento del usuario: ")
    dir = input("Ingrese la dirección del usuario: ")
    tel = input("Ingrese el teléfono del usuario: ")
    email = input("Ingrese el email del usuario: ")
    pwd = input("Ingrese la contraseña del usuario: ")
    rol = input("Ingrese el rol del usuario")
    #Genera el empleado
    nuevo_empleado = Empleado(nombre,id,fecha_nac,ciudad_nac,tel,dir,email, rol, pwd)
    Empleados.append(nuevo_empleado)
    #listas para añadir a los archivos de texto
    vec_empleados = [Empleados[0].get_nombre(), Empleados[0].get_id(), Empleados[0].get_fecha_nac(),
                     Empleados[0].get_ciudad_nac(), Empleados[0].get_tel(), Empleados[0].get_email(), Empleados[0].get_dir()]
    vec_password = [Empleados[0].get_id(), Empleados[0].get_pwd(), Empleados[0].get_rol()]
    #añade en ambos archivos en la primera posicion
    with open('empleados.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(vec_empleados)
    
    with open('password.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(vec_password)
    #Añade el resto de posiciones
    for i in range(1, len(Empleados)):
        vec_empleados = [Empleados[i].get_nombre(), Empleados[i].get_id(), Empleados[i].get_fecha_nac(),
                        Empleados[i].get_ciudad_nac(), Empleados[i].get_tel(), Empleados[i].get_email(), Empleados[i].get_dir()]
        vec_password = [Empleados[i].get_id(), Empleados[i].get_pwd(), Empleados[i].get_rol()]
        #añade en ambos archivos en la primera posicion
        with open('empleados.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(vec_empleados)
        
        with open('password.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(vec_password)
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
        