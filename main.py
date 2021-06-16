#encoding:utf-8

import sys
import time
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
        # elegir entre "hebras" o "procesos":
        trabajadores="procesos"
        num_trabajadores=4
        num_fragmentos=10
        
        if trabajadores=="procesos":
            monitor=MonitorProcesos()
            [monitor.counter.put("dummy") for _ in range(num_fragmentos)]
            pool=PoolProcesos(num_trabajadores,monitor)
            mr=MapReduce(sys.argv[1],monitor,num_fragmentos)
        
        elif trabajadores=="hebras":
            monitor=MonitorHebras()
            pool=PoolHebras(num_trabajadores,monitor)
            mr=MapReduce(sys.argv[1],monitor,num_fragmentos)
        
        patron=sys.argv[2]
        
        t1=time.time()
        posiciones=mr.buscar(patron)
        t2=time.time()
        
        [proceso.terminate() for proceso in pool.procesos]
        [proceso.join() for proceso in pool.procesos]
            
        #imprimir resultados
        for i in range(len(posiciones)):
            logger.info(f"Encontrado {patron} en {posiciones[i]}: {mr.get_secuencia(posiciones[i],len(patron))}")
        logger.info(f"El patrón aparece {len(posiciones)} veces.")
        logger.info(f"Tiempo de buscar el patrón: {t2-t1} segundos.")
        
        
        
if __name__=="__main__":
    main()
    