import csv
from Queue import Queue
from Node import Node
from DoubleNode import DoubleNode
from List import List
from Stack import Stack
from DoubleList import DoubleList
from Empleado import Empleado
from Mensaje import Mensaje
from Almacenamiento import Almacenamiento



def mostrar_bandeja_entrada(empleado: Empleado):
    node = empleado.bandeja_entrada.head
    print(node.to_string_bandeja())
    
def mentsaje_leido():
    ...
def revisar_mensajes_leidos():
    ...
def proyectar_borrador_guardado():
    ...
    
def enviar_mensaje(empleado: Empleado):
    '''Envia un mensaje a un empleado.
    Recibe como parámetro el emisor del mensaje.'''
    email:str = input("Ingrese el email del destinatario: ")
    destinatario: Empleado = Almacenamiento.search_by_email(email)
    titulo: str = input("Ingrese el titulo del mensaje: ")
    cuerpo: str = input("Cuerpo del mensaje: ")
    mensaje: Mensaje = Mensaje(destinatario.get_id(),titulo,cuerpo,empleado.get_id)
    destinatario.recibir_mensaje(mensaje)
    print("El mensaje ha sido enviado con éxito")
    
    
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
    id = input("Ingrese el Id del empleado al que se le hara el cambio de contraseña")
    contra = input("Ingrese la nueva contraseña: ")
    for i in range(len(Empleados)):
        if Empleados[i].get_id() == id:
            Pwd[i][1] = contra
            break
    vec_password = [Pwd[0][0], Pwd[0][1], Pwd[0][2]]
    with open('password.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(vec_password)
    for i in range(1, len(Empleados)):
        vec_password = [Pwd[i][0], Pwd[i][1], Pwd[i][2]]
        #añade en ambos archivos en la primera posicion  
        with open('password.csv', 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(vec_password)
    
def menu(empleado: Empleado):

    if empleado==None:
        print("El usuario no se encuentra registrado")  
    
    elif empleado.get_rol() == "empleado":
         print("---------------------Bienvenido empleado------------------------")
    
         op : str = input(
        """Seleccione una opción:
                          
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
        6. Cambiar contraseña
        """)    
    
        if op == "1":
            mostrar_bandeja_entrada(empleado)
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
    
Empleados = Almacenamiento.get_Empleados()
Pwd = Almacenamiento.get_Passwords()


with open("data.txt","r+") as datos:
    correo = DoubleList()
    print(iden)
    for row in datos:
        sep=row.split(" ")
        id=sep[0]
        correo.addLast(id)
    identificaciones= DoubleList()
    Bandeja_Entrada=DoubleList()
    Mensajes_leidos=Queue()
    Borradores=Stack()
    iterador=correo.head
    contador=0
    while iterador!=None:
        info=correo.getValue(contador)
        informacion=info.split("_")
        identificaciones.addLast(informacion[0])
        mensajes=informacion[1].split("-")
        for i in mensajes:
           Bandeja_Entrada.addFirst(i)
        mensajes=informacion[2].split("-")
        for j in mensajes:
           Mensajes_leidos.enqueue(j)
        mensajes=informacion[1].split("-")
        for k in mensajes:
           Borradores.push(k)
        iterador=iterador.getNext
    print(identificaciones)
    print(Bandeja_Entrada)
    print(Mensajes_leidos)
    print(Borradores)


continuar: bool = True
while continuar:
    print("Bienvenido al sistema de mensajería")
    
    user: str = input("Ingrese su id: ")
    pwd: str = input("Ingrese la contraseña: ")
    empleado = None
    confirmacion: bool = False
    for i in range(len(Empleados)):
        if Empleados[i].get_id() == user:
            if Pwd[i][1] == pwd: 
                empleado = Empleados[i]
                confirmacion = True
                empleado.set_pwd(pwd)
                empleado.set_rol(Pwd[i][2])
                print(empleado.get_rol())
                break
            else:
                print("Contraseña incorrecta")
            
    menu(empleado)
    continuar = input("¿Desea volver a hacer uso del sistema de mensajería? (si/no): ") == "si" 
        