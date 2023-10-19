
class Mensaje:
    
    cedula_receptor: str
    cedula_emisor: str
    titulo: str
    contenido: str
    id: int
    
    def __init__(self, cedula_receptor: str, titulo: str, contenido: str, cedula_emisor: str, id: int = None):
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
        
    def get_id(self) -> int:
        return self.id