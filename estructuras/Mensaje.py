"""from Empleado import Empleado"""
class Mensaje:
    
    correo_receptor: str
    correo_emisor: str
    titulo: str
    contenido: str
    
    def __init__(self, cedula_receptor: str, titulo: str, contenido: str, cedula_emisor: str):
        self.correo_receptor = cedula_receptor
        self.titulo = titulo
        self.contenido = contenido
        self.correo_emisor = cedula_emisor
        
    def get_correo_receptor(self) -> str:
        return self.correo_receptor
    
    def get_contenido(self) -> str:
        return self.contenido
    
    def get_titulo(self) -> str:
        return self.titulo
    
    def get_correo_emisor(self) -> str:
        return self.correo_emisor
    
    def set_contenido(self, contenido: str):
        self.contenido = contenido
        
    def set_titulo(self, titulo: str):
        self.titulo = titulo
        
    def get_id(self) -> int:
        return self.id
    
    def __str__(self) -> str:
        return f"""De: {self.correo_emisor}
                Para: {self.correo_receptor}
                Título: {self.titulo}
                Cuerpo:
                {self.contenido}"""