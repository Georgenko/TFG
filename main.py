#encoding:utf-8

"""main.py es el punto de entrada del programa.

Aquí se crea una o varias instancia Genoma sobre las que buscar patrones.
Se mide el rendimiento de cargar el fichero en memoria.
y también la búsqueda del patrón en el genoma
utilizando una o varias procesos/hebras.
"""

import sys
#import timeit
import time
import math
import concurrent.futures

from leer_fichero import leer_fichero
from genoma import Genoma

def main():
    
    if len(sys.argv)==1:
        print("No se han proporcionado los parámetros.")
        sys.exit()
        
    elif len(sys.argv)==2:
        print("No se ha proporcionado el patrón.")
        sys.exit()
        
    else:
        try:
            
            t1=time.time()
            genoma=leer_fichero(sys.argv[1])
            t2=time.time()
            print("El fichero se cargó en memoria en",t2-t1,"[s]")
            
        except OSError as e:
            print(e)
            sys.exit()
        
        # bv=bytes válidos
        bv=genoma.bytes_validos
        
        # aquí es donde digo el número de procesos/hebras
        num_procesos=8
        
        #p=patrón
        p=sys.argv[2]
        
        if num_procesos==1:
            t=time.time()
            #pos=posiciones donde aparece el patrón en el genoma
            pos=genoma.buscar(p)
            t_buscar_patron=time.time()-t
            
        else:
            t=time.time()
            
            parte_igual=math.floor(bv/num_procesos)
            print(bv,"bytes entre",num_procesos,"procesos =",bv/num_procesos,"~",parte_igual,"bytes por genoma.")
            
            # obtener los índices de cada subgenoma
            ind_subgen={}
            contador=0
            for i in range(num_procesos):
                if i==num_procesos-1:
                    aux=num_procesos*parte_igual
                    # división no exacta y quedan caracteres al final
                    if aux!=bv:
                        ind_subgen[i]=(contador,contador+parte_igual+(bv-aux)-1)
                    else:
                        ind_subgen[i]=(contador,contador+parte_igual-1)
                else:
                    ind_subgen[i]=(contador,contador+parte_igual-1)
                    contador+=parte_igual
            # print("ind_subgen:",ind_subgen)
            
            # crear los subgenomas
            subgenomas=list()
            for i in range(len(ind_subgen)):
                contenido=genoma.contenido[ind_subgen[i][0]:ind_subgen[i][1]]
                bytes_validos=1+ind_subgen[i][1]-ind_subgen[i][0]
                subgenomas.append(Genoma(contenido,bytes_validos))
            # print("subgenomas:",subgenomas)

            # arrancar procesos/hebras
            with concurrent.futures.ProcessPoolExecutor(max_workers=num_procesos) as executor:
                futures=[executor.submit(subgenomas[i].buscar,p) for i in range(num_procesos)]
            
            # obtener resultados parciales y juntarlos en una lista global
            results=[future.result() for future in futures]
            pos=list()
            for i in range(num_procesos):
                for j in range(len(results[i])):
                    pos.append(results[i][j]+i*parte_igual)
            
            t_buscar_patron=time.time()-t
            
            """
            # comprobar listas con y sin trocear
            # OJO CUANDO TROCEAS PUEDES PERDER ÍNDICES AL FINAL DE CADA TROZO!!!
            print(len(pos))
            t=time.time()
            test=genoma.buscar(p)
            t_buscar_patron=time.time()-t
            print("(time) La búsqueda del patrón en el genoma tardó",t_buscar_patron,"[s]")
            print(len(test))
            print("Con y sin trocear sacan listas con la misma longitud:",len(pos)==len(test))
            print("Con y sin trocear sacan las mismas listas:",pos==test)
            """
            
        # esto es para hacer tests
        # 3 veces medir con time y comparar con timeit:
        # print("(timeit) La búsqueda del patrón en el genoma tardó",timeit.timeit(lambda:genoma.buscar(p),number=3)/3,"[s]")
        
        if len(pos)==0:
            print("El patrón",p,"no se ha encontrado en el fichero proporcionado.")
        else:
            for i in range(len(pos)):
                print("Encontrado",p,"en",pos[i],":",genoma.get_secuencia(pos[i],len(p)))

        print("(time) La búsqueda del patrón en el genoma tardó",t_buscar_patron,"[s]")
        
        """
        # datetime.datetime.now() malos resultados o mala implementación?
        # comprobar que time da resultados consistentes:
        for i in range(30):
            print(time.time())
            time.sleep(1)
        """
        
if __name__=="__main__":
    main()
    