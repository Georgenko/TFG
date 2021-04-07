#encoding:utf-8


from bytes_leidos import BytesLeidos
import sys


class LectorFASTA:
    
    # Constructor.
    def __init__(self,filename):
        
        bl=self.leer_fichero(filename)
        
        self.contenido=bl.contenido
        self.bytes_validos=bl.bytes_validos
        

    # Toma como parámetro el fichero del cli.
    # Devuelve una instancia del tipo BytesLeidos.
    def leer_fichero(self,filename):
    
        # f=file
        with open(filename) as f:
            
            # hace falta lanzar excepción?
            # Nos posicionamos al final del fichero
            #     para contar los bytes que contiene.
            f.seek(0,2)
            len_f=f.tell()
            # print("Bytes en el fichero contando newline/line feed:",len_f)
            # print(sys.maxsize)
            if len_f>sys.maxsize:
                f.close()
                print("El fichero",filename,"es demasiado grande.")
                print("No se puede representar con bytearray.")
                sys.exit()
            # Volvemos al principio del fichero
            #     para poder continuar con el resto del programa.
            f.seek(0)


            # bytearray vacío por rellenar.
            contenido=bytearray()
            # print(contenido)
            
            # Contador de bytes metidos en el bytearray.
            bytes_read=0

            # Se procesa cada línea del fichero por separado: l1.
            for l1 in f:
                # print(type(l1))
                # print("l1:",l1)                
                # if not l1:
                    # print("l1 is false")

                
                # l2 es l1 con los caracteres de newline/line feed
                #     al final de cada línea,
                #     y con todos los caracteres pasados a mayúsculas.
                l2=l1.rstrip("\n").upper()
                # print("l2:",l2)
                if not l2:
                    # print("Línea vacía. Continuamos con la siguiente.")
                    continue
                
                len_line=len(l2)
                # print(len_line)
                
                # Se pasan los caracteres a enteros.
                l3=l2.encode()
                # print("l3 =",l3)
                # print("l2[0] =",l2[0],"->","l3[0] =",l3[0])
                # print("l2[1] =",l2[1],"->","l3[1] =",l3[1])
                
                # Se va rellenando el bytearray con
                #     todos los bytes del fichero
                #     excepto los de newline/line feed.
                # b=byte
                for b in l3:
                    # print(b)
                    # print(type(b))
                    
                    contenido.append(b)
                
                # Los bytes leído se van actualizando por cada línea.    
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
        
        posiciones=list()

        p=patron.upper().encode()
        
        try:
            
            # print("Número de comparaciones que se realizarán:",self.bytes_validos-len(patron)+1)
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
    
    
    
    
    
    
    
    
    
    

    