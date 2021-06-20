#encoding:utf-8

import multiprocessing
import queue
from buscador import Buscador
from resultado import Resultado

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class Proceso(multiprocessing.Process):
    def __init__(self,id_proceso,monitor):
        multiprocessing.Process.__init__(self)
        
        self.id_proceso=id_proceso
        self.monitor=monitor
        
        
        
    def run(self):
        while not self.monitor.contador.empty():
            try:
                busqueda=self.monitor.obtener_busqueda()
            except queue.Empty:
                continue
            logger.info(f"Proceso {self.id_proceso} ha obtenido búsqueda {busqueda.indice}.")

            buscador=Buscador(busqueda.contenido,len(busqueda.contenido))
            lista=buscador.buscar(busqueda.patron)
        
            resultado=Resultado(lista,busqueda.indice)
            self.monitor.notificar_resultado(resultado,self.id_proceso)
            
            
            