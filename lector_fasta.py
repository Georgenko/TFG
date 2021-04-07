#encoding:utf-8


from bytes_leidos import BytesLeidos


class LectorFASTA:
    
    
    def __init__(self,filename):
        
        bl=self.leer_fichero(filename)
        
        self.contenido=bl.contenido
        self.bytes_validos=bl.bytes_validos
        
        
    def leer_fichero(self,filename):
    
        # f=file
        with open(filename) as f:
            
            contenido=bytearray()
            # print(contenido)
            
            bytes_read=0
     
            # l=line
            for l1 in f:
                # print(l1)
                # print(type(l1))
                
                l2=l1.rstrip("\n").upper()
                # print(l2)
                
                len_line=len(l2)
                print(len_line)
                
                l3=l2.encode()
                # print("l3 =",l3)
                # print("l2[0] =",l2[0],"->","l3[0] =",l3[0])
                # print("l2[1] =",l2[1],"->","l3[1] =",l3[1])
                
                # b=byte
                for b in l3:
                    # print(b)
                    # print(type(b))
                    
                    contenido.append(b)
                    
                bytes_read+=len_line
    
        # print(contenido)
        # print(bytes_read)
    
        # comprobar que se ha cerrado el fichero correctamente con with:
        # print(f.closed)
        
        return BytesLeidos(contenido,bytes_read)
    

    def comparar(self,patron,posicion):
        # print("patron:",patron)
        # print("Longitud de patron:",len(patron))
        # print("posicion:",posicion)
        # print("comparar se ha invocado.")
        
        for i in range(len(patron)):
            # print("contenido ? patron en",posicion,i,":\t",self.contenido[posicion+i],"?",patron[i])
            
            if patron[i]!=self.contenido[posicion+i] and patron[i]!="N".encode()[0]:
                return False
                
        return True
    
    
    def buscar(self,patron):
        # print("patron:",patron)
        # print("Longitud de patron:",len(patron))
        # print("bytes_validos:",self.bytes_validos)
        
        posiciones=[]

        p=patron.upper().encode()
        
        try:
            
            print("Número de comparaciones que se realizarán:",self.bytes_validos-len(patron)+1)
            for i in range(self.bytes_validos-len(patron)+1):
                
                if self.comparar(p,i):
                    
                    posiciones.append(i)
                    
        except:
            
            print("Algo ha fallado en buscar.")
        
        return posiciones
    
    
    def get_secuencia(self,posicion,tamano):

        s=""
        
        for i in range(tamano):
            
            s+=chr(self.contenido[posicion+i])
            
        return s
    
    
    
    
    
    
    
    
    
    

    