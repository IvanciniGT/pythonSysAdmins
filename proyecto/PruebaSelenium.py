                   # Quiero la clase Prueba
from Prueba import Prueba
     # Del fichero Prueba.py
from subprocess import run, PIPE


class PruebaSelenium(Prueba):
        
    def __init__(self, nombre=None, timeout=0, intervalo=0, numero_fallos_permitidos_consecutivos=0 ):
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        
    def ejecutar(self, servidor):
       