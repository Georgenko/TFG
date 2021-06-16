#encoding:utf-8

import multiprocessing

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class MonitorProcesos:
    def __init__(self):
        self.busquedas_pendientes=multiprocessing.Queue()
        self.resultados_pendientes=multiprocessing.Queue()
        self.counter=multiprocessing.Queue()
        
        
        
    #inicializar búsqueda
    def obtener_busqueda(self):
        busqueda=self.busquedas_pendientes.get()
        self.counter.get()
        
        logger.info(f"Búsqueda {busqueda.indice} solicitada.")
        return busqueda
    
    
 
    #crear búsqueda
    def activar_busqueda(self,busqueda):
        logger.info(f"Creación de búsqueda {busqueda.indice}.")
        
        self.busquedas_pendientes.put(busqueda)
        
        
        
    def obtener_resultado(self):
        resultado_quitado=self.resultados_pendientes.get()
        
        logger.info(f"Resultado de búsqueda {resultado_quitado.indice} obtenido.")
        return resultado_quitado
        
        
        
    def notificar_busqueda(self,resultado,id_proceso):
        self.resultados_pendientes.put(resultado)

        logger.info(f"Finalización de búsqueda {resultado.indice} por proceso {id_proceso}.")
    
    
