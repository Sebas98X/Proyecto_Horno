#CLASE SENSOR DE TEMPERATURA
from Sensores.Sensores import Sensor
from Comunicacion import ModbusRTU

class SensorTemperatura(Sensor):
    def __init__(self, nombre,
                 unidad,
                 rango,
                 ubicacion=None,
                 fabricante=None,
                 modelo=None,
                 tipo="Temperatura",
                 transmisor=None,
                 id_hardware=None,
                 frecuencia_lectura=None,
                 resolucion=None,
                 calibracion=None,
                 es_simulado=False,
                 comunicacion=None     #Se debe implementar diccionario con toda la informacion
                 ):
        super().__init__(nombre,unidad,
                    rango,ubicacion,
                    fabricante,modelo,
                    tipo,transmisor,
                    id_hardware,
                    frecuencia_lectura,
                    resolucion,calibracion,
                    es_simulado)
        self.comunicacion=comunicacion


    def leer_valor(self):
        if self.comunicacion:
            self.ultimo_valor=self.comunicacion.leer()
            return self.ultimo_valor
        else:
            raise ValueError("No se ha definido la comunicacion")







