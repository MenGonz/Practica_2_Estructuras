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
from datetime import datetime



now = datetime.now()

def mostrar_bandeja_entrada(empleado: Empleado):
    """Esta funcionalidad se encarga de mostrar la bandeja de entrada del empleado en cuestión."""
    
    while True:
        empleado.to_string_bandeja()
        op: int = int(input("Digite el número del mensaje que desea leer: "))
        empleado.leer_mensaje(op)
        Almacenamiento.actualizar_bandeja_BD(empleado)
        continuar: str = input("¿Desea leer otro mensaje? (si/no): ")
        if continuar == "si":
            print()
            continue
        elif continuar == "no":
            print()
            break
        else:
            print("Opción no válida")
            break
    
    
    
    
    
    


def revisar_mensajes_leidos():
    """Esta funcionalidad se encarga de mostrar los mensajes leidos del empleado en cuestión."""
    
    while True:
        empleado.to_string_leidos()
        op:int = int(input("Digite el número del mensaje que desea leer: "))
        empleado.leer_mensaje_leido(op)
        continuar: str = input("¿Desea leer otro mensaje? (si/no): ")
        if continuar == "si":
            print()
            continue
        elif continuar == "no":
            print()
            break
        else:
            print("Opción no válida")
            break
        
        
        
        
        
        
        
        
def sacar_borrador_guardado(empleado:Empleado):
    """Esta funcionalidad se encarga de mostrar los borradores guardados del empleado en cuestión."""
    borr: Mensaje = empleado.get_borrador()
    print("El borrador guardado es:\n ")
    print(borr,"\n")
    op:str = input("""Seleccione la acción que desea realizar:\n
                   1. Enviar mensaje
                   2. Descartar mensaje
                   """)
    if op == '1':
        emisor: Empleado = Almacenamiento.search_by_email(borr.get_correo_emisor())
        destinatario: Empleado = Almacenamiento.search_by_email(borr.get_correo_receptor())
        destinatario.recibir_mensaje(borr)
        Almacenamiento.agregar_mensaje_BD(destinatario,borr)
        
        print("Su mensaje ha sido enviado con éxito")
    elif op == '2':
        Almacenamiento.borrar_borrador_BD(emisor)
        print("Mensaje descartado")
    else:
        print("Opción no válida")
        
    
    
    
    
    
    
    
def enviar_mensaje(empleado: Empleado):
    '''Envia un mensaje a un empleado.
    Recibe como parámetro el emisor del mensaje.'''
    
    email:str = input("Ingrese el email del destinatario: ")
    destinatario: Empleado = Almacenamiento.search_by_email(email)
    titulo: str = input("Ingrese el titulo del mensaje: ")
    cuerpo: str = input("Cuerpo del mensaje: ")
    mensaje: Mensaje = Mensaje(destinatario.get_email(),titulo,cuerpo,empleado.get_email(),f"{now.day}/{now.month}/{now.year}",f"{now.hour}:{now.minute}")
    
    op: str = input("""Presione el número de la acción que desea realizar:
                    1. Enviar mensaje
                    2. Guardar como borrador
                    3. Descartar mensaje
                    """)
    if op == '1':
        Almacenamiento.agregar_mensaje_BD(destinatario,mensaje)
        destinatario.recibir_mensaje(mensaje)
    elif op == '2':
        Almacenamiento.agregar_borrador_BD(empleado,mensaje)
        empleado.guardar_borrador(mensaje)
    elif op == '3':
        mensaje = None
        print("Mensaje descartado")
    else:
        print("Opción no válida")
        
    
    print("El mensaje ha sido enviado con éxito")
    
    
    
    
    
    
    
def registrar_nuevo_usuario():
    """Esta funcionalidad se encarga de registrar un nuevo usuario en el sistema."""
    
    #Obtiene la informacion
    nombre = input("Ingrese el nombre del usuario: ")
    id = input("Ingrese el id del usuario: ")
    fecha_nac = input("Ingrese la fecha de nacimiento del usuario: ")
    ciudad_nac = input("Ingrese la ciudad de nacimiento del usuario: ")
    dir = input("Ingrese la dirección del usuario: ")
    tel = input("Ingrese el teléfono del usuario: ")
    email = input("Ingrese el email del usuario: ")
    pwd = input("Ingrese la contraseña del usuario: ")
    rol = input("Ingrese el rol del usuario: ")
    
    
    Almacenamiento.crear_empleado(nombre,id,fecha_nac,ciudad_nac,tel,dir,email, rol, pwd)
   








def cambiar_contraseña():
    """Esta funcionalidad se encarga de cambiar la contraseña de un usuario."""
    
    #Obtenemos la información
    id = input("Ingrese el Id del empleado al que se le hara el cambio de contraseña")
    contra = input("Ingrese la nueva contraseña: ")
    
    
    """
    Es mejor dejar que la clase Almacenamiento se encargue de todo lo relacionado con el csv
    por cuestiones de organización y mantenibilidad.
    Por ese motivo se llama al método cambiar_contraseña de la clase Almacenamiento
    """
    Almacenamiento.cambiar_contraseña(id, contra)    
    
    
    
    
    
    
    
    
def menu(empleado: Empleado):
    """Este método permite mostrar el menú de opciones del sistema de mensajería pa un usuario dado.
    Recibe como parámetro el empleado que está haciendo uso del sistema.
    Se llama cuantas veces el usuario lo desee."""

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
            mostrar_bandeja_entrada(empleado)
         elif op == "2":
            revisar_mensajes_leidos()
         elif op == "3":
            sacar_borrador_guardado()
         elif op == "4":
            enviar_mensaje(empleado)
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
            revisar_mensajes_leidos(empleado)
        elif op == "3":
            sacar_borrador_guardado()
        elif op == "4":
            enviar_mensaje(empleado)
        elif op == "5":
            registrar_nuevo_usuario()
        elif op == "6":
            cambiar_contraseña()
        else:
            print("Opción no válida")
            
        
            
            
            
            
            
            
#Variables globales del main
Empleados = Almacenamiento.get_Empleados()
Pwd = Almacenamiento.get_Passwords()





#Este código da errores, además es mejor meterlo en un método en Almacenamiento y llamarlo desde aquí
#Para ejemplo, revísese la funcionalidad de registrar_nuevo_usuario
"""
with open("data.txt", "r+") as datos:
    correo = DoubleList()
    for row in datos:
        sep = row.split(" ")
        id = sep[0]
        correo.addLast(id)

    identificaciones = DoubleList()
    Bandeja_Entrada = DoubleList()
    Mensajes_leidos = Queue()
    Borradores = Stack()
    contador=0

    iterador = correo.head
    while iterador is not None:
        info = correo.getValue(contador)
        informacion = info.split("_")
        identificaciones.addLast(informacion[0])
        
        mensajes_bandeja = informacion[1].split("-")
        for i in mensajes_bandeja:
            Bandeja_Entrada.addLast(i)
            
        Mensajes_leidos = informacion[2].split("-")
        for j in Mensajes_leidos:
            Mensajes_leidos.enqueue(j)
            
        mensajes_borradores = informacion[3].split("-")
        for k in mensajes_borradores:
            Borradores.push(k)
        contador+=1
        iterador = iterador.getNext()

    print("Identificaciones:", identificaciones)
    print("Bandeja de Entrada:", Bandeja_Entrada)
    print("Mensajes Leídos:", Mensajes_leidos)
    print("Borradores:", Borradores)
    
"""#<<<------Este código daba errores, por eso lo comenté
#Además es mejor meterlo en un Método en Almacenamiento y llamarlo desde aquí,
#tal como hemos hecho con la funcionalidad de registrar_nuevo_usuario.



if __name__ == "__main__":
    
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
                    
                    
        vermenu: bool = True
        while vermenu:
            menu(empleado)
            vermenu = input("Desea volver al menu? (si/no): ") == "si"
            
            
        continuar = input("¿Desea volver a hacer uso del sistema de mensajería? (si/no): ") == "si" 
            