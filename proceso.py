#encoding:utf-8

import multiprocessing
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
        while True:
            busqueda=self.monitor.obtener_busqueda()
            logger.info(f"El proceso {self.id_proceso} ha obtenido la búsqueda {busqueda.indice}.")

            buscador=Buscador(busqueda.contenido,len(busqueda.contenido))
            lista=buscador.buscar(busqueda.patron)
        
            resultado=Resultado(lista,busqueda.indice)
            self.monitor.notificar_busqueda(resultado,self.id_proceso)   
        
        