#encoding:utf-8

import sys
import re

#Si cumple, continua después del else.
if len(sys.argv)==3:
    ruta_fichero=sys.argv[1]
    patron_entrada=sys.argv[2]
#Si no cumple, sale del script.
else:
    print("\nSintaxis del programa:\nbuscar_patron.py [ruta_fichero] [patron]\n")
    sys.exit()

#Cambio las n y N por . para la búsqueda regexp.
patron=re.sub("[nN]",".",patron_entrada)

#Cargo el fichero en contenido, y quito las líneas nuevas para que sea un string continuo.
contenido=re.sub("\n","",open(ruta_fichero).read())

print("\nEl patrón",patron,"aperece en el genoma en las siguientes posiciones:\n")

#Utilizo finditer para buscar todas las ocurrencias del patrón en contenido, y especifico que la búsqueda sea case insensitive.
lista_ocurrencias=[]
for i in re.finditer(patron,contenido,flags=re.IGNORECASE):
    lista_ocurrencias.append(i.start())

print(*lista_ocurrencias,sep=", ")

print()
