

import sys


from lector_fasta import LectorFASTA


if len(sys.argv)==1:
    
    print("No se han proporcionado los parámetros.")
    
    sys.exit()
    
elif len(sys.argv)==2:
    
    print("No se ha proporcionado el patrón.")
    
    sys.exit()
    
else:
    
    try:
        
        lf=LectorFASTA(sys.argv[1])
        
        # Comprobar que los bytes que guardamos son los que nos interesan:
        # print(lf.contenido)
        # print(lf.bytes_validos)
        
        #p=patrón
        p=sys.argv[2]
        
        #pos=lista con posiciones
        pos=lf.buscar(p)
        lf.get_secuencia(0,2)
        for i in range(len(pos)):
            print("Encontrado",p,"en",pos[i],":",lf.get_secuencia(pos[i],len(p)))
        
    except OSError as e:
        print(e)
        
        
        
        