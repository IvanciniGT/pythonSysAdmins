                   # Quiero la clase Prueba
from Prueba import Prueba
     # Del fichero Prueba.py
from subprocess import run, PIPE
from jinja2 import Template
from fabric import Connection
import os

class PruebaService(Prueba):
        
    def __init__(self, nombre=None, timeout=0, intervalo=0, numero_fallos_permitidos_consecutivos=0, servicios=() ):
        super().__init__(nombre, timeout, intervalo, numero_fallos_permitidos_consecutivos)
        self.servicios=servicios
        with open("services.jinja") as archivo_plantilla:
            texto_de_la_plantilla=archivo_plantilla.read()
        self.plantilla=Template( texto_de_la_plantilla )
        
    def ejecutar(self, servidor):
        resultado=self.plantilla.render( self.__dict__ )

        os.environ['use_ssh_config']="True"
        os.environ['key_filename']="~/.ssh/id_rsa"
        remoto=Connection(host= "root@servidor")
        # Vamos a guardar la plantilla en un fichero temporal.. que vamos a copiar dentro del remoto
        
        subproceso=remoto.run( resultado , stdout=PIPE, stderr=PIPE)
        return subproceso.returncode == 0
        
        #if subproceso.resturncode == 0:
        #    return True
        #else
        #    return False