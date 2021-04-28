#encoding:utf-8
"""main.py es el punto de entrada del programa.

Aquí se crea una instancia LectorFASTA sobre la que se pueden buscar patrones.
Se mide el rendimiento de cargar el fichero en memoria.
y también la búsqueda del patrón en el genoma utilizando una o varias hebras.
"""

import sys
#bruh
import datetime
import timeit
import time
import math

from lector_fasta import LectorFASTA

if len(sys.argv)==1:
    print("No se han proporcionado los parámetros.")
    sys.exit()
    
elif len(sys.argv)==2:
    print("No se ha proporcionado el patrón.")
    sys.exit()
    
else:
    try:
        
        """
        # datetime.datetime.now() malos resultados o mala implementación?
        # comprobar que time da resultados consistentes:
        for i in range(30):
            print(time.time())
            time.sleep(1)
        """
        
        t1=time.time()
        lf=LectorFASTA(sys.argv[1])
        t2=time.time()
        print("El fichero se cargó en memoria en",t2-t1,"[s]")
        
        num_procesos=2;
        print(lf.bytes_validos)
        
        lista1=lf.contenido[:math.floor(lf.bytes_validos/2)]
        lista2=lf.contenido[math.floor(lf.bytes_validos/2):]
        print(len(lista1))
        print(len(lista2))
        
        #p=patrón
        p=sys.argv[2]
        t=time.time()
        #pos=lista con posiciones
        pos=lf.buscar(p)
        t_buscar_patron=time.time()-t
        print("(time) La búsqueda del patrón en el genoma tardó",t_buscar_patron,"[s]")
        
        """
        t=time.time()
        pos=lf.buscar(p)
        t_buscar_patron=time.time()-t
        print("(time) La búsqueda del patrón en el genoma tardó",t_buscar_patron,"[s]")
        
        t=time.time()
        pos=lf.buscar(p)
        t_buscar_patron=time.time()-t
        print("(time) La búsqueda del patrón en el genoma tardó",t_buscar_patron,"[s]")
        """
        
        #print("(timeit) La búsqueda del patrón en el genoma tardó",timeit.timeit(lambda:lf.buscar(p),number=3)/3,"[s]")

        if len(pos)==0:
            print("El patrón",p,"no se ha encontrado en el fichero proporcionado.")
        else:
            for i in range(len(pos)):
                print("Encontrado",p,"en",pos[i],":",lf.get_secuencia(pos[i],len(p)))
        
        print()
        
        print("(time) La búsqueda del patrón en el genoma tardó",t_buscar_patron,"[s]")
        
    except OSError as e:
        print(e)