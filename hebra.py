#encoding:utf-8

import threading
import queue
from buscador import Buscador
from resultado import Resultado

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class Hebra(threading.Thread):
    def __init__(self,id_hebra,monitor):
        threading.Thread.__init__(self)
        
        self.id_hebra=id_hebra
        self.monitor=monitor
        
        
        
    def run(self):
        while not self.monitor.contador.empty():
            try:
                busqueda=self.monitor.obtener_busqueda()
            except queue.Empty:
                continue
            logger.info(f"Hebra {self.id_hebra} ha obtenido búsqueda {busqueda.indice}.")
            
            buscador=Buscador(busqueda.contenido,len(busqueda.contenido))
            lista=buscador.buscar(busqueda.patron)
            
            resultado=Resultado(lista,busqueda.indice)
            self.monitor.notificar_resultado(resultado,self.id_hebra)   
            
            
            