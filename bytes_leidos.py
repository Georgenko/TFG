#encoding:utf-8

class BytesLeidos:
    """Clase auxiliar para usar como retorno de función.    
    
    Se utiliza como retorno de leer_fichero en lector_fasta.py.
    
    Attributes:
        contenido:
        bytes_validos: Bytes que no corresponden a caracteres nuevas líneas.
    """
    
    def __init__(self,contenido,bytes_validos):
        """Constructor de instancias BytesLeidos.
        
        Léase la documentación del constructor de la clase LectorFASTA.
        
        """
        self.contenido=contenido
        self.bytes_validos=bytes_validos