from PyQt4 import QtCore
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusTcpClient
import thread

valueUpdated2 = 0
braker = 0
class Update(QtCore.QObject):
    #global valueUpdated2
    valueUpdated2 = QtCore.pyqtSignal(int)
    def threadVRresolver(threadname,a,self,valueUpdated2):
        #global valueUpdated2
        #valueUpdated = QtCore.pyqtSignal(int)
        k = 0
        while 1:
            ##i = self.client.read_holding_registers(85,1)
            #print i
            ##k = i.registers[0]
            k = k+1.0
            #print k
            valueUpdated2.emit(k)
            for j in range(10000):
                pass


    #client = ModbusTcpClient('192.168.0.250')
    client = ModbusTcpClient("192.168.0.250")
    client.connect()

    valueUpdated = QtCore.pyqtSignal(float)
    valueUpdatedv1 = QtCore.pyqtSignal(float)
    valueUpdatedv2 = QtCore.pyqtSignal(float)
    valueUpdatedv3 = QtCore.pyqtSignal(float)
    valueUpdatedv4 = QtCore.pyqtSignal(float)
    valueUpdatedv5 = QtCore.pyqtSignal(float)
    valueUpdatedff = QtCore.pyqtSignal(float)
    #def checkthr(threadname,a):
    def method1(self):
        thread.start_new_thread(self.threadVRresolver,("thread-5",1,self.valueUpdated))
    def method2(self):
        global braker
        k = 0
        p = 0
        while p == 0:
            ##i = self.client.read_holding_registers(85,1)
            #print i
            ##k = i.registers[0]
            k = k-0.0000123
            #print k
            self.valueUpdated.emit(k)
            if braker == 1:
                p = 999
            for j in range(10000):
                pass
    def method(self):
        # i want to connect variable i to progress bar value
        global braker

        while braker == 0:
            i = self.client.read_holding_registers(3800,15)
            j = self.client.read_holding_registers(3903,1)
            #print i.registers[1]
            p = j.registers[0]
            #print float(p)/1000
            v10  =(i.registers[0]+(p%1000))

            v1 = (i.registers[0]+(float(i.registers[1])/1000)) - (2*(i.registers[0]+float(i.registers[1])/1000)*i.registers[2])
            v2 = (i.registers[3]+(float(i.registers[4])/1000)) - 2*(i.registers[3]+float(i.registers[4])/1000)*i.registers[5]
            v3 = (i.registers[6]+float(i.registers[7])/1000) - 2*(i.registers[6]+float(i.registers[7])/1000)*i.registers[8]
            v4 = (i.registers[9]+float(i.registers[10])/1000) - 2*(i.registers[9]+float(i.registers[10])/1000)*i.registers[11]
            v5 = (i.registers[12]+float(i.registers[13])/1000) - 2*(i.registers[12]+float(i.registers[13])/1000)*i.registers[14]
            #print v1
            #print i.registers[0]
            finger = j.registers[0]
            self.valueUpdatedv1.emit(v1)
            self.valueUpdatedv2.emit(v2)
            self.valueUpdatedv3.emit(v3)
            self.valueUpdatedv4.emit(v4)
            self.valueUpdatedv5.emit(v5)
            self.valueUpdatedff.emit(finger+1)
            for j in range(10000):
                pass
    def kill(self):
            global braker
            braker = 1
    def revive(self):
            global braker
            braker = 1
