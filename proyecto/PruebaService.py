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

    def ejecutar(self, servidor):
        
        with open("services.jinja") as archivo_plantilla:
            texto_de_la_plantilla=archivo_plantilla.read()
        self.plantilla=Template( texto_de_la_plantilla )
        
        resultado=self.plantilla.render( self.__dict__ )

        os.environ['use_ssh_config']="True"
        os.environ['key_filename']="~/.ssh/id_rsa"
        remoto=Connection(host= self.usuario"@"+servidor)
        # Vamos a guardar la plantilla en un fichero temporal.. que vamos a copiar dentro del remoto
        
        respuesta=remoto.run( resultado )
        return respuesta.return_code == 0
        
        #if subproceso.resturncode == 0:
        #    return True
        #else
        #    return False