#encoding:utf-8

"""
Módulo para la clase Genoma.
"""

class Genoma:
    """Un fichero FASTA o una parte de él cargado en memoria.
    
    Los genomas en el código se representan como bytearray.
    Los caracteres de nuevas líneas se quitan.
    Los caracteres correspondientes a los nucleótidos A, C, G, N o T
    son los que nos interesan y son por lo tanto los "válidos".
    
    Si ejecutamos el programa en modo secuencial se crea solo un objeto Genoma.
    Si ejecutamos el programa en modo "concurrente" inicialmente se creará
    un objeto Genoma. Luego se crearán tantos objetos Genoma
    como procesos/hebras se especifiquen.
    
    Attributes:
        contenido: bytearray con los caracteres del fichero en bytes.
        bytes_validos: Cantidad de bytes válidos en contenido.
    """
    
    def __init__(self,contenido,bytes_validos):
        """Constructor de instancias Genoma.
        
        Léase la documentación sobre la clase Genoma.
        """
        
        self.contenido=contenido
        
        self.bytes_validos=bytes_validos
        
    def comparar(self,patron,posicion):
        """Comprueba si el patrón coincide con un trozo específico del genoma.
        
        El trozo de genoma empieza en la posición posicion.
        Se comparan byte por byte el patrón y el trozo y si no coinciden,
        se devuelve false.
        Si coinciden, se devuelve true.
        
        Args:
            patron: El patrón proporcionado que se comparará con el trozo.
            posicion: La posición inicial del trozo.
            
        Returns:
            True o False dependiendo de si el patrón coincide con el trozo.
        """
        
        for i in range(len(patron)):
            
            # print("contenido ? patron en",posicion,i,":\t",self.contenido[posicion+i],"?",patron[i])
            if patron[i]!=self.contenido[posicion+i] and patron[i]!="N".encode()[0]:
                
                return False
                
        return True
    
    
    def buscar(self,patron):
        """Obtiene las posiciones en el genoma donde aparece el patrón.
        
        Primero creamos la lista vacía posiciones.
        Luego, el patrón se convierte en letras mayúsculas
        por si ha sido pasado con letras minúsculas.
        Los caracteres del patrón se convierten en su código numérico.
        A continuación empieza un bucle for sobre todos los caracteres del
        genoma menos los últimos len(patron) para que no se salga del "array".
        En cada iteración se llama a comparar para comprobar
        si el patrón coincide en alguna posición del genoma.
        Si es el caso, se agrega esta posición a la lista posiciones.
        
        Args:
            patron: El patrón que buscamos en el fichero de genoma.
        
        Returns:
            La lista con las posiciones donde el patrón aparece en el genoma.
        """
        
        posiciones=list()

        p=patron.upper().encode()
        
        try:
            
            for i in range(self.bytes_validos-len(patron)+1):
                
                if self.comparar(p,i):
                    
                    posiciones.append(i)
                    
        except:
            
            print("Algo ha fallado en buscar.")
        
        return posiciones
    
    
    def get_secuencia(self,posicion,tamano):
        """Obtiene un trozo específico del genoma entero.
        
        El genoma se carga en memoria como un "array".
        Con este método se obtiene el trozo de ese array que empieza en posicion
        y es de longitud tamano.
        
        Se utiliza en la parte final de main.py para imprimir qué trozos y
        dónde han coincidido con el patrón.
        Es útil, si el patrón buscado tiene N, por ejemplo GATNACA.
        En este caso se imprimirán todos los trozos GATAACA, GATCACA, GATGACA
        y GATTACA que hay en el genoma.
        
        Args:
            posicion: La posición a partir de la cual extraer el trozo.
            tamano: Tamaño del trozo que se quiere extraer.
        
        Returns:
            El trozo de longitud tamano que empieza en posicion.
        """

        s=""
        
        for i in range(tamano):
            
            s+=chr(self.contenido[posicion+i])
            
        return s
    