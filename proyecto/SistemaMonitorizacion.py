from Monitorizador import Monitorizador
from threading import Thread

class SistemaMonitorizacion(Thread):
    
    INTERVALO_COMPROBACION_SERVICIOS_A_MONITORIZAR = 2
    
    def __init__(self)
        super().__init__()
        self.servicios={}    #< Estado de los servicios
        self.__monitorizadores={}    
        self.__monitorizar=True
            
            
    def alta_servicio(self, servicio):
        self.servicios[servicio.nombre]=servicio
        #########################################################################################################
        #  nombre   #   SERVICIO                                                                                #
        #########################################################################################################
        #  google   #   Objeto de tipo Servicio, con TODOS los datos del servicio de GOOGLE, pruebas incluidas  #
        #########################################################################################################
        
    def baja_servicio(self, servicio):
        del self.servicios[servicio.nombre]
        #self.servicios.pop(servicio.nombre)
        
    def monitorizar(self):
        self.__monitorizar=True
        self.start()
    
    def run(self):
        # Crear Monitorizadores para cada Servicio con monitorizacion Activada
        # Meter un hilo que segun se activen / desactiven monitorizaciones sobre servicios, cree o borre Monitorizadores
        while self.__monitorizar:
            for nombre, servicio in self.servicios.items():
                
                # Si el servicio debe monitorizarse y no tengo AUN un monitorizador => lo creo
                if self.__monitorizadores.get(nombre) is None and servicio.monitorizar:
                    monitorizador=Monitorizador(servicio)
                    self.__monitorizadores[nombre]=monitorizador
                    monitorizador.start()
                # Si existe el monitorizador pero el servicio no debe monitorizarse, borro el monitorizador
                elif not servicio.monitorizar:
                    #self.__monitorizadores.get(nombre).parar_de_monitorizar()
                    #del self.__monitorizadores[nombre]
                    self.__borrar_monitorizador(nombre)
                        
            for nombre in self.__monitorizadores:
                if self.servicios.get(nombre) is None:
                    self.__borrar_monitorizador(nombre)
                    

            time.sleep(SistemaMonitorizacion.INTERVALO_COMPROBACION_SERVICIOS_A_MONITORIZAR)

    def __borrar_monitorizador(self, nombre_a_borrar):
        self.__monitorizadores.pop(nombre_a_borrar).parar_de_monitorizar()
    
    def parar_de_monitorizar(self):
        self.__monitorizar=False
        # Parar todas las monitorizaciones que se esten ejecutando
        Monitorizador.parar_todos_los_monitorizadores()
        self.__monitorizadores.clear()

# 1º Crear un sistema de Monitorizacion
# 2º Definir una serie de servicios con sus correspondientes pruebas
# 3º Iniciar la monitorizacion
# 4º Desactivar la monitorizacion para un servicio
# 5º Alta de un nuevo servicio
# 6º Baja de un servicio