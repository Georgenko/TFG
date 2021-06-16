#encoding:utf-8

import sys

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



#quitar primera línea del fichero
def leer_FASTA(filename):

    with open(filename) as f:

        f.seek(0,2)
        len_f=f.tell()
        if len_f>sys.maxsize:
            f.close()
            logger.error(f"El fichero {filename} es demasiado grande.")
            logger.error("No se puede representar con bytearray.")
            sys.exit()
        f.seek(0)



        contenido=bytearray()
        bytes_read=0

        for l1 in f:                

            l2=l1.rstrip("\n").upper()
            if not l2:
                continue
            len_line=len(l2)
            l3=l2.encode()
            
            for b in l3:
                contenido.append(b)

            bytes_read+=len_line



    return (contenido,bytes_read)