class LectorFASTA:
    
    
    def __init__(self,filename):
        self.filename=filename
        try:
            leer_fichero(self.filename)
        except:
            print("fallo leer_fichero")
        else:
            print("suceso leer_fichero")


    #es necesario, o simplemente uso lf.filename?
    def __str__(self):
        return f"El fichero seleccionado es {self.filename}"


def leer_fichero(filename):
    print("leer_fichero invocado")

