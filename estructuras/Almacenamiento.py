from Empleado import Empleado
import csv
import os
from Stack import Stack

class Almacenamiento:
    
    #Empleados: list[Empleado] = []
    #Passwords:list[str] = []
    Empleados = []
    Passwords = []
    with open("empleados.csv") as datos:
        lector = csv.reader(datos)
        for row in lector:
            empleado: Empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            Empleados.append(empleado)
    
    with open("password.csv") as datos:
        lector = csv.reader(datos)
        for row in lector:
            Passwords.append([row[0], row[1], row[2]])  
      
      
      
    @staticmethod
    def search_by_email(email:str) -> Empleado:
        '''Busca un empleado por su email y lo retorna, si no lo encuentra lanza una excepcion'''
        for emp in Almacenamiento.Empleados:
            if emp.get_email() == email:
                return emp
        else:
            raise Exception("Email incorrecto")



    @staticmethod
    def search_by_id(cedula:str) -> Empleado:
        """Busca a un empleado por su cedula y lo retorna, si no lo encuentra lanza una excepcion"""
        for emp in Almacenamiento.Empleados:
            if emp.get_id() == cedula:
                return emp
                break
        else:
            raise Exception("Email incorrecto")
                

    @staticmethod
    def crear_empleado(nombre,id,fecha_nac,ciudad_nac,tel,email,dir, rol, pwd):
        #print(Almacenamiento.Passwords)
         #Genera el empleado
        nuevo_empleado = Empleado(nombre,id,fecha_nac,ciudad_nac,tel,email,dir, rol, pwd)
        
        Almacenamiento.Empleados.append(nuevo_empleado)
        Almacenamiento.Passwords.append([id, pwd, rol])
        #listas para añadir a los archivos de texto
        vec_empleados = [Almacenamiento.Empleados[0].get_nombre(), Almacenamiento.Empleados[0].get_id(), Almacenamiento.Empleados[0].get_fecha_nac(),
                        Almacenamiento.Empleados[0].get_ciudad_nac(), Almacenamiento.Empleados[0].get_tel(), Almacenamiento.Empleados[0].get_email(), Almacenamiento.Empleados[0].get_dir()]
        vec_password = [Almacenamiento.Passwords[0][0], Almacenamiento.Passwords[0][1], Almacenamiento.Passwords[0][2]]
        #añade en ambos archivos en la primera posicion
        with open('empleados.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(vec_empleados)
        
        with open('password.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(vec_password)
        #Añade el resto de posiciones
        for i in range(1, len(Almacenamiento.Empleados)):
            vec_empleados = [Almacenamiento.Empleados[i].get_nombre(), Almacenamiento.Empleados[i].get_id(), Almacenamiento.Empleados[i].get_fecha_nac(),
                            Almacenamiento.Empleados[i].get_ciudad_nac(), Almacenamiento.Empleados[i].get_tel(), Almacenamiento.Empleados[i].get_email(), Almacenamiento.Empleados[i].get_dir()]
            vec_password = [Almacenamiento.Passwords[i][0], Almacenamiento.Passwords[i][1], Almacenamiento.Passwords[i][2]]
            #añade en ambos archivos en la primera posicion
            with open('empleados.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(vec_empleados)
            
            with open('password.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(vec_password)
        
        os.chdir("BD_Mensajes")
        BA = open(id + "_BA.csv", "w")
        ML = open(id + "_ML.csv", "w")
        B = open(id + "_B.csv", "w")
        BA.close(), ML.close(), B.close()
        os.chdir("\\estructuras")
            
            
            
    
            
    @staticmethod    
    def cambiar_contraseña(id, contra):
        """Este método recibe un id y una contraseña y cambia la contraseña del empleado con ese id."""
        for i in range(len(Almacenamiento.Empleados)):
            if Almacenamiento.Empleados[i].get_id() == id:
                Almacenamiento.Passwords[i][1] = contra
                break
        vec_password = [Almacenamiento.Passwords[0][0], Almacenamiento.Passwords[0][1], Almacenamiento.Passwords[0][2]]
        with open('password.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(vec_password)
        for i in range(1, len(Almacenamiento.Empleados)):
            vec_password = [Almacenamiento.Passwords[i][0], Almacenamiento.Passwords[i][1], Almacenamiento.Passwords[i][2]]
            #print(vec_password)
            #añade en ambos archivos en la primera posicion  
            with open('password.csv', 'a', encoding='UTF8', newline='') as f:
                writer = csv.writer(f)

                writer.writerow(vec_password)
       
    @staticmethod 
    def borrar_borrador_BD(emisor:Empleado):
        """Este método recibe un emisor y borra de la BD 
        el último borrador guardado de la pila de borradores."""
        os.chdir("BD_Mensajes")
        with open(emisor.get_id() + "_B.csv", 'a', encoding='UTF8', newline='') as f:
            s: Stack = Stack()
            emisor.borradores.pop()
            s.push(emisor.borradores.pop())
            while s.getSize() > 0:
                mensaje = s.pop()
                writer = csv.writer(f)
                writer.writerow([mensaje.get_correo_receptor(), mensaje.get_titulo(), f"{mensaje.get_contenido()}",
                             mensaje.get_correo_emisor(), mensaje.get_fecha_envío(), mensaje.get_hora_envío()])
        os.chdir("\\estructuras")
                
            
                
        
        
        
    @staticmethod
    def agregar_mensaje_BD(destinatario,mensaje):
        """Este método recibe un destinatario y un mensaje ya éste lo guarda en la
        bandeja de entrada (BD) del destinatario."""
        os.chdir("BD_Mensajes")
        with open(destinatario.get_id() + "_BA", "a", encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([mensaje.get_correo_receptor(), mensaje.get_titulo(), f"{mensaje.get_contenido()}",
                             mensaje.get_correo_emisor(), mensaje.get_fecha_envío(), mensaje.get_hora_envío()])
        os.chdir("\\estructuras")
        
    @staticmethod
    def agregar_borrador_BD(emisor: Empleado,mensaje):
        """Este método recibe un emisor y un mensaje. Éste mensaje se guarda en
        la pila de borradores (BD) del emisor."""
        os.chdir("BD_Mensajes")
        with open(emisor.get_id() + "_B.csv", 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([mensaje.get_correo_receptor(), mensaje.get_titulo(), f"{mensaje.get_contenido()}",
                             mensaje.get_correo_emisor(), mensaje.get_fecha_envío(), mensaje.get_hora_envío()])
        os.chdir("\\estructuras")
        
    @staticmethod
    def actualizar_bandeja_BD(empleado: Empleado):
        """Este método recibe un empleado y actualiza su bandeja de entrada (BD)
        en base al atributo bandeja de entrada del empleado en cuestión."""
        os.chdir("BD_Mensajes")
        with open(empleado.get_id()+"_BA.csv", 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            curr = empleado.bandeja_entrada.head
            for i in range(empleado.bandeja_entrada.getSize()):
                writer.writerow([curr.getData().get_correo_receptor(), curr.getData().get_titulo(), f"{curr.getData().get_contenido()}", curr.getData().get_correo_emisor(), curr.getData().get_fecha_envío(), curr.getData().get_hora_envío()])
                curr = curr.next
        os.chdir("\\estructuras")
        
        
    def get_Empleados():
        return Almacenamiento.Empleados
    
    def get_Passwords():
        return Almacenamiento.Passwords