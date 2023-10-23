from DoubleList import DoubleList
from Mensaje import Mensaje
from Queue import Queue
from Stack import Stack
import os
class Empleado: #Se define la clase usuario
    
    id: str
    nombre: str
    fecha_nac: str
    ciudad_nac: str
    dir: str
    tel: str
    email: str
    rol: str
    pwd: str
    bandeja_entrada: DoubleList
    mensajes_leidos: Queue
    borradores = Stack
    
    def __init__(self,nombre,id,fecha_nac=None,ciudad_nac=None,tel=None,email=None, dir=None, rol =  None, pwd = None):
        self.id = id
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.ciudad_nac = ciudad_nac
        self.dir = dir
        self.tel = tel
        self.email = email
        self.rol = rol
        self.pwd = pwd
        self.bandeja_entrada = DoubleList()
        self.mensajes_leidos = Queue()
        self.borradores = Stack()
        
    #Getters
    def get_id(self):
        return self.id
    def get_nombre(self):
        return self.nombre
    def get_fecha_nac(self):
        return self.fecha_nac
    def get_ciudad_nac(self):
        return self.ciudad_nac
    def get_dir(self):
        return self.dir
    def get_tel(self):
        return self.tel
    def get_email(self):
        return self.email
    def get_rol(self):
        return self.rol
    def get_pwd(self):
        return self.pwd
    
    #Setters
    def set_id(self, id):
        self.id = id
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_fecha_nac(self, fecha_nac):
        self.fecha_nac = fecha_nac
    def set_ciudad_nac(self, ciudad_nac):
        self.ciudad_nac = ciudad_nac
    def set_dir(self, dir):
        self.dir = dir
    def set_tel(self, tel):
        self.tel = tel
    def set_email(self, email):
        self.email = email
    def set_pwd(self, pwd):
        self.pwd = pwd
    def set_rol(self, rol):
        self.rol = rol
        

    def recibir_mensaje(self,mensaje:Mensaje):
        self.bandeja_entrada.addLast(mensaje)
        

    
        

    def leer_mensaje_leido(self,id_mensaje:int):
        """Éste método recibe como parámetro el id del mensaje que se desea leer y lo imprime."""
        curr = self.mensajes_leidos.tail
        
        if self.mensajes_leidos.getSize() == 0:

            print("El número ingresado es incorrecto.")

        else:
            
            for i in range(id_mensaje):
                curr = curr.prev
            print(curr.getData())
            

    def guardar_borrador(self,mensaje:Mensaje):
        """Este método recibe como parámetro un mensaje y lo guarda en la pila de borradores."""
        self.borradores.push(mensaje)
        

    def get_borrador(self)-> Mensaje:
        """Este método muestra el último borrador guardado del empleado."""
        if self.borradores.getSize() > 0:
            return self.borradores.pop()
        else:
            print("No hay borradores guardados.")
        
    
    #Tostring  
    def __str__(self):
        
        return f"""El empleado {self.get_nombre()} con id {self.get_id()} tiene la siguiente información: 
                   Fecha de nacimiento: {self.get_fecha_nac()}
                   Ciudad de nacimiento: {self.get_ciudad_nac()}
                   Dirección: {self.get_dir()}
                   Teléfono: {self.get_tel()}
                   Email: {self.get_email()}"""
                   
    
    def to_string_bandeja(self):
        """Éste método muestra los mensajes que tiene el empleado en su bandeja de entrada."""
        
        s: str = "Bandeja de entrada:\n"
        curr = self.bandeja_entrada.head
        for i in range(self.bandeja_entrada.getSize()):
            s += f"{i}. Emisor: {curr.getData().correo_emisor}\nTítulo: {curr.getData().titulo}\n"
            curr = curr.next
        print(s[:-1])
    

    def to_string_leidos(self):
        """Éste método muestra los mensajes leidos que tiene el empleado."""
        
        s: str = "Mensajes leídos:\n"
        curr = self.mensajes_leidos.tail
        for i in range(self.mensajes_leidos.getSize()):

            s += f"{i}. Emisor: {curr.getData().correo_emisor}\nTítulo: {curr.getData().titulo}\n"
            curr = curr.prev
            
        print(s[:-1])
        
        
if __name__ == "__main__":
    for i in range(1):
        print("hola")