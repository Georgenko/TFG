class BytesLeidos:
    
    
    def __init__(self,contenido,bytes_validos):
        self.contenido=contenido
        self.bytes_validos=bytes_validos
        
    #tienen sentido los getters? o simplemente uso bl.contenido o bl.bytes_validos?
    def get_contenido(self):
        return self.contenido
    
    
    def get_bytes_validos(self):
        return self.bytes_validos