import sys
from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui import Ui_MainWindow
from axistracker import Update
from tracker import TRK
import time
import subprocess
import Leap
import os
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusTcpClient
import thread
#from axistracker import Update

#==========================================================================================================#
#==========================================================================================================#
GRVR = 0
speed = 0
p = 0
q = 0
x = 0
ip = "0.0.0.0"
client = ModbusTcpClient(ip)
#global Declaration Area
stop_flag = 0
start_flag = 0
start_leap = 0
speed = 0
con_flg = 0
boxflag = 0
controlv1 = 1
controlv2 = 1
controlv3 = 1
controlv4 = 1


#==========================================================================================================#
#==========================================================================================================#
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


def slg(threadname,a):
    global ip
    global start_leap
    global q
    q = subprocess.Popen(["python","feature_ext.py","-i",ip])

def checkthr(threadname,a):
    global ip
    global start_leap
    global q
    #q = subprocess.Popen(["python","feature_ext.py","-i",ip])
    client2 = ModbusTcpClient(str(ip))
    client2.connect()
    while 1:
    #for i in range(0,16):
    	time.sleep(2)
        client.write_register(3909,1)

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):

    def ConnectionError(self):
       #global controlv4
       #controlv4 = 0
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Information)
       msg.setText("Communication Error")
       msg.setInformativeText("Unable to find controller")
       msg.setWindowTitle("COMMUNICATION ERROR")
       msg.setDetailedText("Unable to ffind the controller, Kindly check the connection and the IP address entered in the IP box")
       msg.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)
       retval = msg.exec_()
       print "value of pressed message box button:", retval

    def EmergencyStop(self):
       global controlv4
       controlv4 = 0
       self.disconet()
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText("The System is in Emergency Stop state")
       msg.setInformativeText("The Emergency Stop switch was pressed")
       msg.setWindowTitle("EMERGENCY STOP")
       msg.setDetailedText("EMERGENCY STOP button is pressed, Release the switch and reset the controller by pressing the enable Controller button, followed by the reset buttton")
       msg.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)
       retval = msg.exec_()
       print "value of pressed message box button:", retval

    def SystemFault(self):
       global controlv3
       controlv3 = 0
       self.disconet()
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText("The controller has faulted")
       msg.setInformativeText("The Robot has faulted due to internal errors")
       msg.setWindowTitle("System Fault")
       msg.setDetailedText("The Robot has faulted due to internal reasons, Kindly reset the controller by first pressing the enable controller button followed by the reset button")
       msg.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)
       retval = msg.exec_()
       print "value of pressed message box button:", retval

    def LimitReach(self):
       global controlv2
       controlv2 = 0
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)
       msg.setText("Robot Limits Reached")
       msg.setInformativeText("Robot Soft-Limit Reached!!,Robot Motion in Linear Mode arrested to avoid ccomplications")
       msg.setWindowTitle("Limit Reached")
       msg.setDetailedText("The Robot has reached its limits, To reset the robot, switch to Joint mode and jog back to PRE-HOMING position")
       msg.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)
       retval = msg.exec_()
       print "value of pressed message box button:", retval

    def LimitApproach(self):
       global controlv1
       controlv1 = 0
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Information)
       msg.setText("Robot Limits Approaching")
       msg.setInformativeText("Robot Speed reduced to avoid complications")
       msg.setWindowTitle("Limit Approach")
       msg.setDetailedText("The Robot is approaching its physical limits, Robot velocity has been reduced to avoid compliactions at boundary conditions")
       msg.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)
       retval = msg.exec_()
       print "value of pressed message box button:", retval

    def trackthread(self,threadname,e):
        global ip
        global x
        x = 1
        client3 = ModbusTcpClient("192.168.0.250")
        a = client3.connect
        print a
        if a:
            while x == 1:
                reg = client3.read_holding_registers(3935,4)
                if reg.registers[0] == 1:
                    #self.disconet()
                    print reg.registers
                    self.LimitApproach()
                if reg.registers[1] == 1:
                    self.disconet()
                    self.LimitReach()
                if reg.registers[2] == 1:
                    self.disconet()
                    self.SystemFault()
                if reg.registers[3] == 1:
                    self.disconet()
                    self.EmergencyStop()

    def showdialog(self):
       msg = QMessageBox()
       msg.setIcon(QMessageBox.Warning)

       msg.setText("Robot Limits Reached")
       msg.setInformativeText("This is additional information")
       msg.setWindowTitle("LIMIT REACHED")
       msg.setDetailedText("You have reached the limits pvadsjclshdi jmfciuhm aiucnhihb hbcsduhb coab ihbc ou bcfou bcoubsdou bsduv k")
       msg.setStandardButtons(QMessageBox.Ok)# | QMessageBox.Cancel)
       msg.buttonClicked.connect(self.msgbtn)

       retval = msg.exec_()
       print "value of pressed message box button:", retval
    def msgbtn(self,i):
        print "Button pressed is:",i.text()

    def GRclamp(self):
        global GRVR
        client.write_register(GRVR,1)
        self.clamp.setEnabled(0)
        self.dclamp.setEnabled(1)

    def GRdclamp(self):
        global GRVR
        client.write_register(GRVR,0)
        self.dclamp.setEnabled(0)
        self.clamp.setEnabled(1)

    def conq(self):
        thread.start_new_thread(self.VRresolver,("thread-4",1))
        #thread.start_new_thread(self.trackthread,("thread-5",1))
        thread.start_new_thread(checkthr,("thread-3",1))
        thread.start_new_thread(self.TRKthr,("thread-5",1))
        #self.axistracker.revive()
        #self.tracker.revive()

    def TRKthr(self,threadname,a):
        self.mySLT()
    def VRresolver(self,threadname,a):
        self.myButtonSlot()

    def conet(self,ipa):

        #global x
        #x = 1
        global controlv1
        global controlv2
        global controlv3
        global controlv4

        global ip
        global con_flg
        ip = ipa
        print ip
        global client
        client = ModbusTcpClient(str(ip))
        #client.connect()
        a =client.connect()


        if a != False:
            print "Connected Succesfully"
            con_flg = 1
            self.conp()
            controlv1 = 1
            controlv2 = 1
            controlv3 = 1
            controlv4 = 1
        elif a == False:
            con_flg = 0
            print "Unable to Connect"
            self.ConnectionError()
        print a


    def conp(self):
        global con_flg
        if con_flg == 1:
            self.ip.setEnabled(0)
            self.clamp.setEnabled(1)
            self.connect.setEnabled(0)
            self.disconnect.setEnabled(1)
            self.ecx.setEnabled(1)
            #self.ecx_2.setEnabled(1)
            self.clamp.setEnabled(1)
            client.write_register(3601,0)
        else:
            print "Please check connection and try again"
    def disconp(self):
        self.disconnect.setEnabled(0)
        self.connect.setEnabled(1)
        self.ecx.setEnabled(0)
        self.dcx.setEnabled(0)
        self.ip.setEnabled(1)
        #self.

    def disconet(self):
        global x
        global window
        x = 0
        #self.LimitApproach()
        print "here"
        if p != 0:
            self.dbs()
        if q != 0:
            self.dbl()
        if client.connect() != False:
            self.disconp()
            client.write_register(3601,1)
            client.write_register(3605,0)
            self.clamp.setEnabled(0)
            self.dclamp.setEnabled(0)


    def ext(self):
        self.disconet()
        global window
        self.axistracker.kill()
        """if p != 0:
            self.dbs()
        if q != 0:
            self.dbl()
	    client.write_register(3601,1)"""
        print "EXITING APP"
        self.axistracker.kill()
        self.tracker.kill()
        window.close()

    def ens(self):
        global start_flag
        print "ens"
        start_flag = 1
        print start_flag
        client.write_register(3605,2)
        thread.start_new_thread(ssp, ("thread-1",start_flag))
        #start_speech("th4",start_flag)

    def dbs(self):
        global start_flag
        print "dns"
        start_flag = 0
        print start_flag
        global p
        p.kill()
        client.write_register(3605,0)

    def enl(self):
        global start_leap
        print "enl"
        start_leap = 1
        print start_leap
        client.write_register(3605,1)
        thread.start_new_thread(slg,("thread-2",start_leap))

    def dbl(self):
        global start_leap
        print "dbl"
        start_leap = 0
        print start_leap
        global q
        q.kill()
        client.write_register(3605,0)

    def slider_set(self,slv):
        global speed
        speed = slv
        print str(speed)
        client.write_register(3602,speed)

    def r_leap(self):
        print "starting"
        os.system("service leapd restart")

    def r_lcp(self):
        print "stopping"
        os.system("service leapd stop")

    def setl(self):
        print "setting linear"
        #self.labela1.setText("X Axis")
        self.labelmode.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Linear Mode</p></body></html>", None))
        client.write_register(3600,1)

    def setj(self):
        print "seting joint"

        self.lcdNumbera2.display("1234.567")
        self.labelmode.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Joint Mode</p></body></html>", None))
        client.write_register(3600,2)

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        #self.myButtonSlot()
        #self.axistracker.method1()
        self.connect.clicked.connect(self.conq)
        self.axistracker = Update(self)
        self.axistracker.valueUpdated.connect(self.handleValueUpdated)
        self.axistracker.valueUpdatedv1.connect(self.handleValueUpdated1)
        self.axistracker.valueUpdatedv2.connect(self.handleValueUpdated2)
        self.axistracker.valueUpdatedv3.connect(self.handleValueUpdated3)
        self.axistracker.valueUpdatedv4.connect(self.handleValueUpdated4)
        self.axistracker.valueUpdatedv5.connect(self.handleValueUpdated5)
        self.axistracker.valueUpdatedff.connect(self.handleValueUpdatedff)

        self.tracker = TRK(self)
        self.tracker.valueTRKv1.connect(self.handleTRLv1)
        self.tracker.valueTRKv2.connect(self.handleTRLv2)
        self.tracker.valueTRKv3.connect(self.handleTRLv3)
        self.tracker.valueTRKv4.connect(self.handleTRLv4)


#==========================================================================================================#

        self.connect.clicked.connect(lambda: self.conet(self.ip.text()))
        self.exitB.clicked.connect(lambda: self.ext())
        self.disconnect.clicked.connect(lambda: self.disconet())
        #self.exitB.clicked.connect(lambda: self.ext())
        #>>self.ecx_2.clicked.connect(lambda: self.ens())
        #>>self.dcx_2.clicked.connect(lambda:self.dbs())
        self.ecx.clicked.connect(lambda: self.enl())
        self.dcx.clicked.connect(lambda:self.dbl())
        self.sl.valueChanged.connect(lambda: self.slider_set(self.sl.value()))
        self.rld.clicked.connect(lambda: self.r_leap())
        self.slcp.clicked.connect(lambda: self.r_lcp())
        self.lb.pressed.connect(lambda: self.setl())
        self.jb.pressed.connect(lambda: self.setj())
        self.clamp.clicked.connect(lambda: self.GRclamp())
        self.dclamp.clicked.connect(lambda: self.GRdclamp())
        self.lcdNumbera2m.setDigitCount(8);
        self.lcdNumbera1.setDigitCount(8);
        self.lcdNumbera2.setDigitCount(8);
        self.lcdNumbera3.setDigitCount(8);
        self.lcdNumbera4.setDigitCount(8);
        self.lcdNumbera5.setDigitCount(8);
        self.lcdNumbera2m.setSegmentStyle(2)
        self.lcdNumbera1.setSegmentStyle(2)
        self.lcdNumbera2.setSegmentStyle(2)
        self.lcdNumbera3.setSegmentStyle(2)
        self.lcdNumbera4.setSegmentStyle(2)
        self.lcdNumbera5.setSegmentStyle(2)

    def myButtonSlot(self):
        self.axistracker.method()
    def mySLT(self):
        self.tracker.method()
    def handleTRLv2(self,value):
        x = [value]
        global controlv2
        #print x
        if controlv2 == 1 and x[0] == 1:
            self.LimitReach()
            controlv2= 0
        if x[0] == 0 and controlv2 == 0:
            print "LOLOLOLOLOLOLOLOLOL"
            controlv2 = 1
        #if value == 1and controlv2 == 1:
    def handleTRLv3(self,value):
        if value == 1and controlv3 == 1:
            self.SystemFault()
    def handleTRLv4(self,value):
        if value == 1 and controlv4 == 1:
            self.EmergencyStop()
    def handleTRLv1(self, value):
        x = [value]
        global controlv1
        #print x
        if controlv1 == 1 and x[0] == 1:
            self.LimitApproach()
            controlv1= 0
        if x[0] == 0 and controlv1 == 0:
            controlv1 = 1
    def handleValueUpdated(self, value):
        x = [value]
        self.lcdNumbera2.display(value)
        QtGui.qApp.processEvents()
    def handleValueUpdated1(self, value):
        x = [value]
        self.lcdNumbera1.display(value)
        QtGui.qApp.processEvents()
    def handleValueUpdated2(self, value):
        x = [value]
        self.lcdNumbera2.display(value)
        QtGui.qApp.processEvents()
    def handleValueUpdated3(self, value):
        x = [value]
        self.lcdNumbera3.display(value)
        QtGui.qApp.processEvents()
    def handleValueUpdated4(self, value):
        x = [value]
        self.lcdNumbera4.display(value)
        QtGui.qApp.processEvents()
    def handleValueUpdated5(self, value):
        x = [value]
        self.lcdNumbera5.display(value)
        QtGui.qApp.processEvents()
    def handleValueUpdatedff(self, value):
        x = [value]
        self.lcdNumbera2m.display(value)
        QtGui.qApp.processEvents()
def main():
    global window
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == '__main__':

    main()
