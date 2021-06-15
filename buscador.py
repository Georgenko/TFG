#encoding:utf-8

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class Buscador:
    def __init__(self,contenido,bytes_validos):
        self.contenido=contenido
        self.bytes_validos=bytes_validos



    def comparar(self,patron,posicion):
        for i in range(len(patron)):
            if patron[i]!=self.contenido[posicion+i] and patron[i]!="N".encode()[0]:
                return False
        return True



    def buscar(self,patron):
        posiciones=list()
        p=patron.upper().encode()
        try:
            for i in range(self.bytes_validos-len(patron)+1):
                if self.comparar(p,i):
                    posiciones.append(i)
        except:
            logger.info("Algo falla en buscar.")
        return posiciones
    
    
    