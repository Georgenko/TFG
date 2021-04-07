

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
    # esto invoca el método __str__ de la clase LectorFasta:
    # print(lf)
    # esto te imprime el atributo filename de la instancia lf:
    # print(lf.filename)
    
        print(lf.contenido)
        
        #p=patrón
        p=sys.argv[2]
        
        #pos=lista con posiciones
        pos=lf.buscar(p)
        lf.get_secuencia(0,2)
        for i in range(len(pos)):
            print("Encontrado",p,"en",pos[i],":",lf.get_secuencia(pos[i],len(p)))
        
    except OSError as e:
        print(e)
        
        
        
        