#encoding:utf-8

import sys
# import time
from monitor import Monitor
from pool import Pool
from map_reduce import MapReduce

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



def main():
    if len(sys.argv)==1:
        logger.info("No se han proporcionado los parámetros.")
        sys.exit()
    elif len(sys.argv)==2:
        logger.info("No se ha proporcionado el patrón.")
        sys.exit()
    else:
        monitor=Monitor()
        Pool(5,monitor)
        mr=MapReduce(sys.argv[1],monitor,10)
        patron=sys.argv[2]
        posiciones=mr.buscar(patron)
        
        #imprimir resultados
        if len(posiciones)==0:
            logger.info(f"El patrón {patron} no se ha encontrado en el fichero proporcionado.")
        else:
            for i in range(len(posiciones)):
                logger.info(f"Encontrado {patron} en {posiciones[i]}: {mr.get_secuencia(posiciones[i],len(patron))}")

        logger.info(f"Número de posiciones donde aparece el patrón: {len(posiciones)}.")



if __name__=="__main__":
    main()
    