#encoding:utf-8

import multiprocessing

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class MonitorProcesos:
    def __init__(self):
        self.busquedas_pendientes=multiprocessing.Queue()
        self.resultados_pendientes=multiprocessing.Queue()
        self.contador=multiprocessing.Queue()
        
        
        
    #crear búsqueda
    def activar_busqueda(self,busqueda):        
        self.busquedas_pendientes.put(busqueda)
        
        logger.info(f"Activación de búsqueda {busqueda.indice}.")
        
        
        
    def obtener_busqueda(self):
        busqueda=self.busquedas_pendientes.get(block=False)
        self.contador.get()
        
        logger.info(f"Búsqueda {busqueda.indice} obtenida.")
        return busqueda
    
    
    
    def notificar_resultado(self,resultado,id_proceso):
        self.resultados_pendientes.put(resultado)

        logger.info(f"Proceso {id_proceso} ha notificado el resultado de búsqueda {resultado.indice}.")
    
    

    def obtener_resultado(self):
        resultado_quitado=self.resultados_pendientes.get()
        
        logger.info(f"Se ha obtenido el resultado de búsqueda {resultado_quitado.indice}.")
        return resultado_quitado
        
        
        