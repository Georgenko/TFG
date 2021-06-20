#encoding:utf-8

import queue

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class MonitorHebras:
    def __init__(self):
        self.busquedas_pendientes=queue.Queue()
        self.resultados_pendientes=queue.Queue()
        self.contador=queue.Queue()
    
    
    
    #crear búsqueda
    def activar_busqueda(self,busqueda):
        self.busquedas_pendientes.put(busqueda)
        
        logger.info(f"Activación de búsqueda {busqueda.indice}.")
        
        
         
    def obtener_busqueda(self):      
        busqueda=self.busquedas_pendientes.get(block=False)
        self.busquedas_pendientes.task_done()
        self.contador.get()
        self.contador.task_done()
        
        logger.info(f"Búsqueda {busqueda.indice} obtenida.")
        return busqueda
    
    
 
    def notificar_resultado(self,resultado,id_hebra):
        self.resultados_pendientes.put(resultado)

        logger.info(f"Hebra {id_hebra} ha notificado el resultado de búsqueda {resultado.indice}.")
    
    
    
    def obtener_resultado(self):
        resultado_quitado=self.resultados_pendientes.get()
        self.resultados_pendientes.task_done()
        
        logger.info(f"Se ha obtenido el resultado de búsqueda {resultado_quitado.indice}.")
        return resultado_quitado
        
        
        