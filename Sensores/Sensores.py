#CLASE ABSTRACTA DEL SENSOR
from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self,nombre,
                    unidad,
                    rango,
                 ubicacion=None,
                 fabricante=None,
                 modelo=None,
                 tipo=None,
                 transmisor=None,
                 id_hardware=None,
                 frecuencia_lectura=None,
                 resolucion=None,
                 calibracion=None,
                 es_simulado=False
                 ):
#Atributos de objetos o instancias
        self.nombre=nombre               #Nombre lógico del sensor
        self.unidad=unidad               #Unidad de medida
        self.rango=rango                 #Rango permitido
        self.ubicacion=ubicacion         #Donde está instalado
        self.fabricante=fabricante       #Nombre del fabricante
        self.modelo=modelo               #Modelo del sensor
        self.tipo=tipo                   #Tipo.Temp,Presión
        self.transmisor=transmisor       #Dict con datos del transmisor
        self.id_hardware=id_hardware     #Dirección y identificador físico
        self.frecuencia_lectura=frecuencia_lectura   #Hz o Intervalo
        self.resolucion=resolucion       #Precision o numeros decimales
        self.calibracion=calibracion     #Datos de calibración
        self.es_simulado=es_simulado     #Indica si es un sensor virtual o fisico
#Valores que se actualizaran con el tiempo de ejecución
        self.ultimo_valor=None           #Ultima lectura
        self.timestamp=None              #Fecha y hora de lectura
        self.estado="INICIALIZADO"       #Estado Inicial del sensor

    @abstractmethod
    def leer_valor(self):
        """Método obligatorio que deben implementar las subclases"""
        pass

    def __str__(self):
        return (f"Sensor(Nombre={self.nombre},"
                f"Ubicacion={self.ubicacion},Modelo={self.modelo},"
                f"Estado={self.estado})")




