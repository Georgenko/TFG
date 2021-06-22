#encoding:utf-8

import sys
import time
from leer_FASTA import leer_FASTA
from monitor_hebras import MonitorHebras
from monitor_procesos import MonitorProcesos
from pool_hebras import PoolHebras
from pool_procesos import PoolProcesos
from map_reduce import MapReduce

import logging

logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



def main():
    if len(sys.argv)==1:
        logger.error("No se han proporcionado los parámetros.")
        sys.exit()
    elif len(sys.argv)==2:
        logger.error("No se ha proporcionado el patrón.")
        sys.exit()
    else:
        # elegir entre "secuencial" o "concurrente"
        modo="concurrente"
        
        if modo=="concurrente":
            # elegir entre "hebras" o "procesos":
            trabajadores="procesos"
            num_trabajadores=4
            num_fragmentos=4
            
            if trabajadores=="procesos":
                monitor=MonitorProcesos()
                [monitor.contador.put("dummy") for _ in range(num_fragmentos)]
                pool=PoolProcesos(num_trabajadores,monitor)
            
            elif trabajadores=="hebras":
                monitor=MonitorHebras()
                [monitor.contador.put("dummy") for _ in range(num_fragmentos)]
                PoolHebras(num_trabajadores,monitor)
                
            mr=MapReduce(sys.argv[1],monitor,num_fragmentos)
            patron=sys.argv[2]
            
            t1=time.time()
            posiciones=mr.buscar(patron)
            t2=time.time()
                
            #imprimir resultados
            for i in range(len(posiciones)):
                logger.info(f"Encontrado {patron} en {posiciones[i]}: {mr.get_secuencia(posiciones[i],len(patron))}")
            logger.info(f"El patrón aparece {len(posiciones)} veces.")
            logger.info(f"Tiempo de buscar el patrón: {t2-t1} segundos.")
            
            if trabajadores=="procesos":
                [p.join() for p in pool.procesos]
                # [logger.info(f"{p}") for p in pool.procesos]
                [p.close() for p in pool.procesos]
                # [logger.info(f"{p}") for p in pool.procesos]
                
        
        
        
        
        elif modo=="secuencial":
            buscador=leer_FASTA(sys.argv[1])
            patron=sys.argv[2]
            t1=time.time()
            posiciones=buscador.buscar(patron)
            t2=time.time()
            
            #imprimir resultados
            for i in range(len(posiciones)):
                logger.info(f"Encontrado {patron} en {posiciones[i]}: {buscador.get_secuencia(posiciones[i],len(patron))}")
            logger.info(f"El patrón aparece {len(posiciones)} veces.")
            logger.info(f"Tiempo de buscar el patrón: {t2-t1} segundos.")
        
        
        
if __name__=="__main__":
    main()
    