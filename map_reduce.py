#encoding:utf-8

import math
from leer_FASTA import leer_FASTA
from busqueda import Busqueda

import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger()



class MapReduce:
    def __init__(self,filename,monitor,num_fragmentos):
        buscador=leer_FASTA(filename)
        self.contenido=buscador.contenido
        self.bytes_validos=buscador.bytes_validos
        self.monitor=monitor
        self.num_fragmentos=num_fragmentos
        
        
        
    def buscar(self,patron):
        self.map(patron)
        return self.reduce()
        
        
        
    def map(self,patron):
        longitud_base=math.floor(self.bytes_validos/self.num_fragmentos)
        for i in range(self.num_fragmentos):
            subgenoma=self.obtener_subgenoma(i,patron,longitud_base)
            
            busqueda=Busqueda(subgenoma,patron,i)
            self.monitor.activar_busqueda(busqueda)
            
            
            
    def obtener_subgenoma(self,indice,patron,longitud_base):
        inicio=indice*longitud_base
        if indice+1!=self.num_fragmentos:
            #para no perder secuencias entre subgenomas se suma len(patron):
            fin=inicio+longitud_base-1+len(patron)
            logger.info(f"Subgenoma {inicio}-{fin}.")
            return self.contenido[inicio:fin]
        else:
            logger.info(f"Subgenoma {inicio}-final.")
            return self.contenido[inicio:]
        
        
        
    def reduce(self):
        lista_global=list()
        longitud_base=math.floor(self.bytes_validos/self.num_fragmentos)
        for _ in range(self.num_fragmentos):
            resultado=self.monitor.obtener_resultado()
            lista_parcial=[(i+(longitud_base*resultado.indice)) for i in resultado.lista]
            lista_global.extend(lista_parcial)
        lista_global.sort()
        return lista_global
        
        
        
    def get_secuencia(self,posicion,tamano):
        s=""
        for i in range(tamano):
            s+=chr(self.contenido[posicion+i])
        return s
    
    
    