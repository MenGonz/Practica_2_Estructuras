class Empleado: #Se define la clase usuario
    def __init__(self,nombre,id,fecha_nac=None,ciudad_nac=None,tel=None,dir=None,email=None):
        self.id = id
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.ciudad_nac = ciudad_nac
        self.dir = dir
        self.tel = tel
        self.email = email
        
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
    #Tostring  
    def __str__(self):
        
        return f"""El empleado {self.get_nombre()} con id {self.get_id()} tiene la siguiente información: 
                   Fecha de nacimiento: {self.get_fecha_nac()}
                   Ciudad de nacimiento: {self.get_ciudad_nac()}
                   Dirección: {self.get_dir()}
                   Teléfono: {self.get_tel()}
                   Email: {self.get_email()}"""