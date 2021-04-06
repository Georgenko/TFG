#coding=utf-8
import sys
from lector_fasta import LectorFASTA


if(len(sys.argv)==1):
    print("No se han proporcionado los parámetros.")
    sys.exit()


"""
if(len(sys.argv)==2):
    print("No se ha proporcionado el patrón.")
    sys.exit()
"""


lf=LectorFASTA(sys.argv[1])
print(lf)
#print(lf.filename)