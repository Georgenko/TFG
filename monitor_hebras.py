#encoding:utf-8

import queue

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class MonitorHebras:
    def __init__(self):
        self.busquedas_pendientes=queue.Queue()
        self.resultados_pendientes=queue.Queue()
    
    
    
        #inicializar búsqueda
    def obtener_busqueda(self):      
        busqueda=self.busquedas_pendientes.get()
        self.busquedas_pendientes.task_done()
        
        logger.info(f"La búsqueda {busqueda.indice} se ha solicitado.")
        return busqueda
    
    
 
    #crear búsqueda
    def activar_busqueda(self,busqueda):
        logger.info(f"Se ha creado la búsqueda {busqueda.indice}.")
        
        self.busquedas_pendientes.put(busqueda)
        
        
        
    def obtener_resultado(self):
        resultado_quitado=self.resultados_pendientes.get()
        self.resultados_pendientes.task_done()
        
        logger.info(f"Se ha obtenido el resultado {resultado_quitado.indice}.")
        return resultado_quitado
        
        
        
    def notificar_busqueda(self,resultado,id_hebra):
        self.resultados_pendientes.put(resultado)

        logger.info(f"La hebra {id_hebra} ha completado la búsqueda {resultado.indice}.")
    
    
