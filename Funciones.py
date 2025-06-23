import time
import pymodbus.client.serial

#FUNCION CREACION DE UN CLIENTE MODBUS
def make_client_modbus(config):
    cliente=pymodbus.client.serial.ModbusSerialClient(port=config["port"],baudrate=config["baudrate"],
                                                      bytesize=config["bytesize"],parity=config["parity"],
                                                      stopbits=config["stopbits"],timeout=config["timeout"])
    return cliente


#FUNCION CONECTAR CLIENTE
def conectar_cliente(cliente):
        if cliente.connect():
            print("Conectado al plc...")
            return True
        else:
            print("No se ha podido conectar al PLC")
            return False


#FUNCION LECTURA DE REGISTROS
def lectura_registros(cliente):
    result = cliente.read_input_registers(address=0, count=2, slave=1)
    return result





