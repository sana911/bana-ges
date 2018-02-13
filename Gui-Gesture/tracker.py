from PyQt4 import QtCore
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusTcpClient
import thread

valueUpdated2 = 0
braker = 0
class TRK(QtCore.QObject):
    #print "ssssssssssssssssswwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
    #global valueUpdated2
    #valueUpdated2 = QtCore.pyqtSignal(int)
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

    #valueUpdated = QtCore.pyqtSignal(float)
    valueTRKv1 = QtCore.pyqtSignal(int)
    valueTRKv2 = QtCore.pyqtSignal(int)
    valueTRKv3 = QtCore.pyqtSignal(int)
    valueTRKv4 = QtCore.pyqtSignal(int)
    #valueUpdatedv5 = QtCore.pyqtSignal(float)
    #valueUpdatedff = QtCore.pyqtSignal(float)
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
        temp = 0
        while braker == 0:
            i = self.client.read_holding_registers(3935,4)
            #print i.registers
            v1 = i.registers[0]
            v2 = i.registers[1]
            v3 = i.registers[2]
            v4 = i.registers[3]
            ##v5 = i.registers[4]
            #temp = v1
            if v1 == 1 or v1 ==0:# and temp == 1:
                self.valueTRKv1.emit(v1)
            #    temp = 0
                #self.valueTRLv1.emit(0)
            #if v1 == 0:
            #    temp = 1
            if v2 == 1 or v2 ==0:
                self.valueTRKv2.emit(v2)
            if v3 == 1:
                self.valueTRKv3.emit(v3)
            if v4 == 1:
                self.valueTRKv4.emit(v4)
            for j in range(10000):
                pass
        print "Something in tracker"

    def kill(self):
            global braker
            braker = 1
    def revive(self):
            global braker
            braker = 1
