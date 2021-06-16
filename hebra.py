#encoding:utf-8

import threading
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
        # self.monitor.counter!=0
        while True:
            
            busqueda=self.monitor.obtener_busqueda()
            logger.info(f"La hebra {self.id_hebra} ha obtenido la búsqueda {busqueda.indice}.")
            
            buscador=Buscador(busqueda.contenido,len(busqueda.contenido))
            lista=buscador.buscar(busqueda.patron)
            
            resultado=Resultado(lista,busqueda.indice)
            self.monitor.notificar_busqueda(resultado,self.id_hebra)
            
        
        