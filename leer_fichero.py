#encoding:utf-8
"""
vaya
"""

import sys
from genoma import Genoma

def leer_fichero(filename):
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
    
    return Genoma(contenido,bytes_read)