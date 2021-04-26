#encoding:utf-8
"""main.py es el punto de entrada del programa.

Aquí se crea una instancia LectorFASTA sobre la que se pueden buscar patrones.
Se mide el rendimiento de cargar el fichero en memoria.
y también la búsqueda de patrón en el genoma utilizando una o varias hebras.
"""

import sys
import datetime as d
import timeit

from lector_fasta import LectorFASTA

if len(sys.argv)==1:
    print("No se han proporcionado los parámetros.")
    sys.exit()
    
elif len(sys.argv)==2:
    print("No se ha proporcionado el patrón.")
    sys.exit()
    
else:
    try:
        # for i in range(10000000):
            # print(d.datetime.now())
        # microseg?
        
        t=d.datetime.now()
        lf=LectorFASTA(sys.argv[1])

        t_cargar_fichero=d.datetime.now()-t
        print("El fichero se ha cargado en",round(t_cargar_fichero.microseconds/1000),"milisegundos.")
        
        #p=patrón
        p=sys.argv[2]

        #pos=lista con posiciones
    
        t=d.datetime.now()
        pos=lf.buscar(p)
        t_buscar_patron=t-d.datetime.now()
        """
        print("La busqueda del patrón ha tardado",round(t_buscar_patron.microseconds/1000),"milisegundos.")
        t=d.datetime.now()
        pos=lf.buscar(p)
        t_buscar_patron=t-d.datetime.now()
        print("La busqueda del patrón ha tardado",round(t_buscar_patron.microseconds/1000),"milisegundos.")
        t=d.datetime.now()
        pos=lf.buscar(p)
        t_buscar_patron=t-d.datetime.now()
        print("La busqueda del patrón ha tardado",round(t_buscar_patron.microseconds/1000),"milisegundos.")
        t=d.datetime.now()
        pos=lf.buscar(p)
        t_buscar_patron=t-d.datetime.now()
        print("La busqueda del patrón ha tardado",round(t_buscar_patron.microseconds/1000),"milisegundos.")
        t=d.datetime.now()
        pos=lf.buscar(p)
        t_buscar_patron=t-d.datetime.now()
        print("La busqueda del patrón ha tardado",round(t_buscar_patron.microseconds/1000),"milisegundos.")
        """
        
        """
        print("antes de timeit")
        print(timeit.timeit(lambda:lf.buscar(p),number=3))
        print("después de timeit")
        """

        if len(pos)==0:
            print("El patrón",p,"no se ha encontrado en el fichero proporcionado.")
        else:
            for i in range(len(pos)):
                print("Encontrado",p,"en",pos[i],":",lf.get_secuencia(pos[i],len(p)))
        
        print()

        print("El fichero se ha cargado en",round(t_cargar_fichero.microseconds/1000),"milisegundos.")
        print("La búsqueda del patrón ha tardado",round(t_buscar_patron.microseconds/1000),"milisegundos.")
        
    except OSError as e:
        print(e)