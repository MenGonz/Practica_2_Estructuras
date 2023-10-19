from DoubleList import DoubleList
from Mensaje import Mensaje
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
    mensajes_leidos: DoubleList
    
    def __init__(self,nombre,id,fecha_nac=None,ciudad_nac=None,tel=None,dir=None,email=None, rol =  None, pwd = None):
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
        self.bandeja_entrada.addLast(Mensaje)
        
    def leer_mensaje(self,titulo:str):
        curr: Mensaje = self.bandeja_entrada.head
        for i in range(self.bandeja_entrada.size()):
            if curr.titulo == titulo:
                self.mensajes_leidos.addLast()
                print(Mensaje)
                break
        else:
            raise Exception("El correo con el título requerido no existe")
            
        
    #Tostring  
    def __str__(self):
        
        return f"""El empleado {self.get_nombre()} con id {self.get_id()} tiene la siguiente información: 
                   Fecha de nacimiento: {self.get_fecha_nac()}
                   Ciudad de nacimiento: {self.get_ciudad_nac()}
                   Dirección: {self.get_dir()}
                   Teléfono: {self.get_tel()}
                   Email: {self.get_email()}"""
                   
                   
    def to_string_bandeja(self):
        s: str = ""
        curr: Mensaje = self.bandeja_entrada.head
        for i in range(self.bandeja_entrada.size()):
            s += f"{i}. Emisor: {curr.cedula_emisor}\nTítulo: {curr.titulo}\n"
            curr = curr.next
        return s[:-1]