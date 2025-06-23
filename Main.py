#Importacion de Modulo config.json
import json
import math
import time

#Importacion de la Clase ModbusSeriealClient
import pymodbus.client.serial
#Importamos el modulo funciones
import Funciones

#Cargar configuracion como dicc a variable "config"
with open("config.json") as f:
    config=json.load(f)["modbus"]


#Invocacion de funcion para crear un cliente Modbus
cliente_Modbus=Funciones.make_client_modbus(config)

if Funciones.conectar_cliente(cliente_Modbus):
    try:
        while True:
            Lectura=Funciones.lectura_registros(cliente_Modbus)
            if Lectura.isError():
                print("Error en la lectura", Lectura)
            else:
                print(math.ceil(Lectura.registers[0]*15/1000))
                print(math.ceil(Lectura.registers[1]*10/1000))
            time.sleep(3)

    except KeyboardInterrupt():
        print("El usuario a interrumpido la lectura...")
    finally:
        cliente_Modbus.close()
        print("Conexion cerrada...")










