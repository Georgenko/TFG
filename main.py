

import sys
import datetime as d


from lector_fasta import LectorFASTA


if len(sys.argv)==1:
    
    print("No se han proporcionado los parámetros.")
    
    sys.exit()
    
elif len(sys.argv)==2:
    
    print("No se ha proporcionado el patrón.")
    
    sys.exit()
    
else:
    
    try:
        
        t1=d.datetime.now()
        lf=LectorFASTA(sys.argv[1])
        t2=d.datetime.now()
        t_cargar_fichero=t2-t1
        print("El fichero se ha cargado en",t_cargar_fichero.microseconds/1000,"milisegundos.")
        
        # Comprobar que los bytes que guardamos son los que nos interesan:
        # print(lf.contenido)
        # print(lf.bytes_validos)
        
        #p=patrón
        p=sys.argv[2]
        
        #pos=lista con posiciones
        t1=d.datetime.now()
        pos=lf.buscar(p)
        t2=d.datetime.now()
        t_buscar_patron=t2-t1
        print("La busqueda del patrón ha tardado",t_buscar_patron.microseconds/1000,"milisegundos.")

        if len(pos)==0:
            print("El patrón",p,"no se ha encontrado en el fichero proporcionado.")
        else:
            for i in range(len(pos)):
                print("Encontrado",p,"en",pos[i],":",lf.get_secuencia(pos[i],len(p)))
        
    except OSError as e:
        print(e)