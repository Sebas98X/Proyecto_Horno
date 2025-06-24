#Creacion de la Clase Modbus RTU
class ComunicacionModbusRTU:
    def __init__(self,cliente,address,count,slave):
        self.cliente=cliente
        self.address=address
        self.count=count
        self.slave=slave

    def leer(self):
        resultado = self.cliente.read_input_registers(address=self.address,count=self.count, slave=self.slave)
        return resultado.registers[0]








