#encoding:utf-8
"""
module documentation
"""

from bytes_leidos import BytesLeidos
import sys

class LectorFASTA:
    """Cada instancia representa un fichero FASTA cargado en memoria.
    
    Los genomas en ficheros FASTA se representan en bytearray.
    Los nuevas líneas se quitan.
    Los bytes correspondientes a los nucleótidos A, C, G, N o T son los que
    nos interesan y son por lo tanto los válidos.
    
    Attributes:
        contenido: bytearray con los caracteres del fichero en bytes.
        bytes_validos: Cantidad de bytes válidos en contenido.
    """
    
    def __init__(self,filename):
        """Constructor de instancias LectorFASTA.
        
        Se llama a leer_fichero para obtener contenido y bytes_validos
        y construir una instancia LectorFASTA.
        
        Args:
            filename: El path del fichero FASTA a cargar.
        """
        
        bl=self.leer_fichero(filename)
        
        self.contenido=bl.contenido
        self.bytes_validos=bl.bytes_validos
        
        
    def leer_fichero(self,filename):
        """Carga en memoria los nucleótidos y su cantidad.
        
        f=file
        l=line
        b=byte
        
        El fichero se "abre" con open en modo read.
        
        Primero se comprueba si el fichero caberá en memoria.
        Esto se consigue posicionándose al final del fichero con seek,
        y ver cuántos bytes ocupa. Luego se compara con el máximo posible
        del sistema en el que se ejecuta el código.
        Nota: se tienen en cuenta también los caracteres de nueva línea.
        
        Luego creamos un bytearray vacío y un contador de bytes leídos nulo.
        A continuación se "lee" cada línea del fichero en bucle.
        A cada una se le quita la nueva línea con rstrip.
        Las letras se convierten en mayúsculas con upper.
        Si la línea es vacía, se pasa a la siguiente.
        Se coge la longitud de esa línea con len.
        Los caracteres se convierten en sus códigos numéricos/bytes con encode.
        Cada uno de estos se añade al final de contenido.
        El contador de bytes leídos se actualiza en cada iteración de línea
        procesada.
        
        Args:
            filename: El path del fichero FASTA a cargar.
        
        Returns:
            Una instancia BytesLeidos con el contenido del fichero y los
            bytes leídos que representan los bytes válidos.
        """
    
        with open(filename) as f:

            # Nos posicionamos al final del fichero
            #     para contar los bytes que contiene.
            f.seek(0,2)
            len_f=f.tell()
            # print("Bytes en el fichero contando newline/line feed:",len_f)
            if len_f>sys.maxsize:
                f.close()
                print("El fichero",filename,"es demasiado grande.")
                print("No se puede representar con bytearray.")
                sys.exit()
            # Volvemos al principio del fichero
            #     para poder continuar con el resto del programa.
            f.seek(0)

            contenido=bytearray()
            bytes_read=0

            for l1 in f:                

                l2=l1.rstrip("\n").upper()
                if not l2:
                    continue
                
                len_line=len(l2)
                
                l3=l2.encode()
                # print("l3 =",l3)
                # print("l2[0] =",l2[0],"->","l3[0] =",l3[0])
                # print("l2[1] =",l2[1],"->","l3[1] =",l3[1])
                
                for b in l3:
                    
                    contenido.append(b)
                
                bytes_read+=len_line
    
        # comprobar que se ha cerrado el fichero correctamente con with:
        # print(f.closed)
        
        return BytesLeidos(contenido,bytes_read)
    

    def comparar(self,patron,posicion):
        """Comprueba si el patrón coincide con un trozo del genoma.
        
        El trozo de genoma empieza en la posición posicion.
        Se comparan byte por byte el patrón y el trozo y si no coinciden,
        se devuelve false.
        Si coinciden, se devuelve true.
        
        Args:
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
    