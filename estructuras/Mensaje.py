
class Mensaje:
    
    cedula_receptor: str
    cedula_emisor: str
    titulo: str
    contenido: str
    
    def __init__(self, cedula_receptor, titulo, contenido, cedula_emisor):
        self.cedula_receptor = cedula_receptor
        self.titulo = titulo
        self.contenido = contenido
        self.cedula_emisor = cedula_emisor
        
    def get_cedula_receptor(self) -> str:
        return self.cedula_receptor
    
    def get_contenido(self) -> str:
        return self.contenido
    
    def get_titulo(self) -> str:
        return self.titulo
    
    def get_cedula_emisor(self) -> str:
        return self.cedula_emisor
    
    def set_contenido(self, contenido: str):
        self.contenido = contenido
        
    def set_titulo(self, titulo: str):
        self.titulo = titulo