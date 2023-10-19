from Empleado import Empleado
import csv

class Almacenamiento:
    
    Empleados: list[Empleado] = []
    Passwords:list[str] = []
      
    @staticmethod
    def search_by_email(email:str) -> Empleado:
        '''Busca un empleado por su email y lo retorna, si no lo encuentra lanza una excepcion'''
        for emp in Almacenamiento.Empleados:
            if emp.get_email() == email:
                return emp
        else:
            raise Exception("Email incorrecto")


    @staticmethod
    def search_by_cedula(cedula:str) -> Empleado:
        ...
        
    def get_Empleados() -> list[Empleado]:
        return Almacenamiento.Empleados
    
    def get_Passwords() -> list[str]:
        return Almacenamiento.Passwords
        
    
    with open("empleados.csv") as datos:
        lector = csv.reader(datos)
        for row in lector:
            empleado: Empleado = Empleado(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
            Empleados.append(empleado)
    
    with open("password.csv") as datos:
        lector = csv.reader(datos)
        for row in lector:
            Passwords.append([row[0], row[1], row[2]])
            
            
    