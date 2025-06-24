#Importacion de Modulo config.json
import json
import math
import time
from Sensores.Sensor_Temp.Temp import SensorTemperatura
from Comunicacion.ModbusRTU import ComunicacionModbusRTU
#Importacion de la Clase ModbusSeriealClient
#Importamos el modulo funciones
import Funciones

#Cargar configuracion como dicc a variable "config"
with open("config.json") as f:
    config=json.load(f)["modbus"]

#Invocacion de funcion para crear un cliente Modbus
cliente_Modbus=Funciones.make_client_modbus(config)
#Creacion de objeto Comunicacion Modbus
Com1= ComunicacionModbusRTU(cliente=cliente_Modbus,address=0,count=1,slave=1)
Com2= ComunicacionModbusRTU(cliente=cliente_Modbus,address=1,count=1,slave=1)

#Creacion de objeto SensorTemp
SensorTemp1=SensorTemperatura("Largo","°C",(0,100),ubicacion="Superior",modelo="PT100-Largo",comunicacion=Com1)
SensorTemp2=SensorTemperatura("Corto","°C",(0,100),ubicacion="Inferior",modelo="PT100-Corto",comunicacion=Com2)
#Conectar cliente
if Funciones.conectar_cliente(cliente_Modbus):
    try:
        while True:
            Escalamiento1=math.ceil(SensorTemp1.leer_valor()*(15/1000))
            print(SensorTemp1,Escalamiento1,"°C")
            Escalamiento2=math.ceil(SensorTemp2.leer_valor()*(10/1000))
            print(SensorTemp2,Escalamiento2,"°C")
            time.sleep(3)

    except KeyboardInterrupt:
            print("El usuario a terminado el programa")
    finally:
        print("Cliente desconectado...")
        cliente_Modbus.close()
else:
        print("Intentando conectar...")




























