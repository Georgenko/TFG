#encoding:utf-8

import queue

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class MonitorHebras:
    def __init__(self):
        self.busquedas_pendientes=queue.Queue()
        self.resultados_pendientes=queue.Queue()
        self.counter=queue.Queue()
    
    
    
    #inicializar búsqueda
    def obtener_busqueda(self):      
        busqueda=self.busquedas_pendientes.get()
        self.busquedas_pendientes.task_done()
        self.counter.get()
        self.counter.task_done()
        
        logger.info(f"Búsqueda {busqueda.indice} solicitada.")
        return busqueda
    
    
 
    #crear búsqueda
    def activar_busqueda(self,busqueda):
        logger.info(f"Creación de búsqueda {busqueda.indice}.")
        
        self.busquedas_pendientes.put(busqueda)
        
        
        
    def obtener_resultado(self):
        resultado_quitado=self.resultados_pendientes.get()
        self.resultados_pendientes.task_done()
        
        logger.info(f"Resultado de búsqueda {resultado_quitado.indice} obtenido.")
        return resultado_quitado
        
        
        
    def notificar_busqueda(self,resultado,id_hebra):
        self.resultados_pendientes.put(resultado)

        logger.info(f"Finalización de búsqueda {resultado.indice} por hebra {id_hebra}.")
    
    
