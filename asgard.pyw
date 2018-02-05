import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from gui import Ui_MainWindow
import serial_port_finder as spf
import serial, time

s0 = serial.Serial()


class AsgardGUI(Ui_MainWindow):
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)

		self.SerialThreadClass = SerialThreadClass()
		self.SerialThreadClass.start()
		self.SerialThreadClass.serialSignal.connect(self.updateConsole)



		self.FKSliderArt1.valueChanged.connect(self.FKSliderUpdateArt1)
		self.SpinBoxArt1.valueChanged.connect(self.FKSpinBoxUpdateArt1)
		self.FKDec10ButtonArt1.pressed.connect(self.FKDec10Art1)
		self.FKDec1ButtonArt1.pressed.connect(self.FKDec1Art1)
		self.FKDec0_1ButtonArt1.pressed.connect(self.FKDec0_1Art1)
		self.FKInc0_1ButtonArt1.pressed.connect(self.FKInc0_1Art1)
		self.FKInc1ButtonArt1.pressed.connect(self.FKInc1Art1)
		self.FKInc10ButtonArt1.pressed.connect(self.FKInc10Art1)

		self.FKSliderArt2.valueChanged.connect(self.FKSliderUpdateArt2)
		self.SpinBoxArt2.valueChanged.connect(self.FKSpinBoxUpdateArt2)
		self.FKDec10ButtonArt2.pressed.connect(self.FKDec10Art2)
		self.FKDec1ButtonArt2.pressed.connect(self.FKDec1Art2)
		self.FKDec0_1ButtonArt2.pressed.connect(self.FKDec0_1Art2)
		self.FKInc0_1ButtonArt2.pressed.connect(self.FKInc0_1Art2)
		self.FKInc1ButtonArt2.pressed.connect(self.FKInc1Art2)
		self.FKInc10ButtonArt2.pressed.connect(self.FKInc10Art2)

		self.FKSliderArt3.valueChanged.connect(self.FKSliderUpdateArt3)
		self.SpinBoxArt3.valueChanged.connect(self.FKSpinBoxUpdateArt3)
		self.FKDec10ButtonArt3.pressed.connect(self.FKDec10Art3)
		self.FKDec1ButtonArt3.pressed.connect(self.FKDec1Art3)
		self.FKDec0_1ButtonArt3.pressed.connect(self.FKDec0_1Art3)
		self.FKInc0_1ButtonArt3.pressed.connect(self.FKInc0_1Art3)
		self.FKInc1ButtonArt3.pressed.connect(self.FKInc1Art3)
		self.FKInc10ButtonArt3.pressed.connect(self.FKInc10Art3)

		self.FKSliderArt4.valueChanged.connect(self.FKSliderUpdateArt4)
		self.SpinBoxArt4.valueChanged.connect(self.FKSpinBoxUpdateArt4)
		self.FKDec10ButtonArt4.pressed.connect(self.FKDec10Art4)
		self.FKDec1ButtonArt4.pressed.connect(self.FKDec1Art4)
		self.FKDec0_1ButtonArt4.pressed.connect(self.FKDec0_1Art4)
		self.FKInc0_1ButtonArt4.pressed.connect(self.FKInc0_1Art4)
		self.FKInc1ButtonArt4.pressed.connect(self.FKInc1Art4)
		self.FKInc10ButtonArt4.pressed.connect(self.FKInc10Art4)

		self.FKSliderArt5.valueChanged.connect(self.FKSliderUpdateArt5)
		self.SpinBoxArt5.valueChanged.connect(self.FKSpinBoxUpdateArt5)
		self.FKDec10ButtonArt5.pressed.connect(self.FKDec10Art5)
		self.FKDec1ButtonArt5.pressed.connect(self.FKDec1Art5)
		self.FKDec0_1ButtonArt5.pressed.connect(self.FKDec0_1Art5)
		self.FKInc0_1ButtonArt5.pressed.connect(self.FKInc0_1Art5)
		self.FKInc1ButtonArt5.pressed.connect(self.FKInc1Art5)
		self.FKInc10ButtonArt5.pressed.connect(self.FKInc10Art5)

		self.FKSliderArt6.valueChanged.connect(self.FKSliderUpdateArt6)
		self.SpinBoxArt6.valueChanged.connect(self.FKSpinBoxUpdateArt6)
		self.FKDec10ButtonArt6.pressed.connect(self.FKDec10Art6)
		self.FKDec1ButtonArt6.pressed.connect(self.FKDec1Art6)
		self.FKDec0_1ButtonArt6.pressed.connect(self.FKDec0_1Art6)
		self.FKInc0_1ButtonArt6.pressed.connect(self.FKInc0_1Art6)
		self.FKInc1ButtonArt6.pressed.connect(self.FKInc1Art6)
		self.FKInc10ButtonArt6.pressed.connect(self.FKInc10Art6)

		self.SliderGripper.valueChanged.connect(self.SliderUpdateGripper)
		self.SpinBoxGripper.valueChanged.connect(self.SpinBoxUpdateGripper)
		self.Dec10ButtonGripper.pressed.connect(self.Dec10Gripper)
		self.Dec1ButtonGripper.pressed.connect(self.Dec1Gripper)
		self.Inc1ButtonGripper.pressed.connect(self.Inc1Gripper)
		self.Inc10ButtonGripper.pressed.connect(self.Inc10Gripper)

		self.SerialPortRefreshButton.pressed.connect(self.getSerialPorts)
		self.ConnectButton.pressed.connect(self.connectSerial)

		self.HomeButton.pressed.connect(self.homeRobot)

	def homeRobot(self):
		self.ConsoleOutput.appendPlainText("home!")


	def FKSliderUpdateArt1(self):
		val=self.FKSliderArt1.value()/10
		self.SpinBoxArt1.setValue(val)
	def FKSpinBoxUpdateArt1(self):
		val=int(self.SpinBoxArt1.value()*10)
		self.FKSliderArt1.setValue(val)
	def FKDec10Art1(self):
		val=self.SpinBoxArt1.value()-10
		self.SpinBoxArt1.setValue(val)
	def FKDec1Art1(self):
		val=self.SpinBoxArt1.value()-1
		self.SpinBoxArt1.setValue(val)
	def FKDec0_1Art1(self):
		val=self.SpinBoxArt1.value()-0.1
		self.SpinBoxArt1.setValue(val)
	def FKInc0_1Art1(self):
		val=self.SpinBoxArt1.value()+0.1
		self.SpinBoxArt1.setValue(val)
	def FKInc1Art1(self):
		val=self.SpinBoxArt1.value()+1
		self.SpinBoxArt1.setValue(val)
	def FKInc10Art1(self):
		val=self.SpinBoxArt1.value()+10
		self.SpinBoxArt1.setValue(val)

#FK Art2 Functions
	def FKSliderUpdateArt2(self):
		val=self.FKSliderArt2.value()/10
		self.SpinBoxArt2.setValue(val)
	def FKSpinBoxUpdateArt2(self):
		val=int(self.SpinBoxArt2.value()*10)
		self.FKSliderArt2.setValue(val)
	def FKDec10Art2(self):
		val=self.SpinBoxArt2.value()-10
		self.SpinBoxArt2.setValue(val)
	def FKDec1Art2(self):
		val=self.SpinBoxArt2.value()-1
		self.SpinBoxArt2.setValue(val)
	def FKDec0_1Art2(self):
		val=self.SpinBoxArt2.value()-0.1
		self.SpinBoxArt2.setValue(val)
	def FKInc0_1Art2(self):
		val=self.SpinBoxArt2.value()+0.1
		self.SpinBoxArt2.setValue(val)
	def FKInc1Art2(self):
		val=self.SpinBoxArt2.value()+1
		self.SpinBoxArt2.setValue(val)
	def FKInc10Art2(self):
		val=self.SpinBoxArt2.value()+10
		self.SpinBoxArt2.setValue(val)

#FK Art3 Functions
	def FKSliderUpdateArt3(self):
		val=self.FKSliderArt3.value()/10
		self.SpinBoxArt3.setValue(val)
	def FKSpinBoxUpdateArt3(self):
		val=int(self.SpinBoxArt3.value()*10)
		self.FKSliderArt3.setValue(val)
	def FKDec10Art3(self):
		val=self.SpinBoxArt3.value()-10
		self.SpinBoxArt3.setValue(val)
	def FKDec1Art3(self):
		val=self.SpinBoxArt3.value()-1
		self.SpinBoxArt3.setValue(val)
	def FKDec0_1Art3(self):
		val=self.SpinBoxArt3.value()-0.1
		self.SpinBoxArt3.setValue(val)
	def FKInc0_1Art3(self):
		val=self.SpinBoxArt3.value()+0.1
		self.SpinBoxArt3.setValue(val)
	def FKInc1Art3(self):
		val=self.SpinBoxArt3.value()+1
		self.SpinBoxArt3.setValue(val)
	def FKInc10Art3(self):
		val=self.SpinBoxArt3.value()+10
		self.SpinBoxArt3.setValue(val)

#FK Art4 Functions
	def FKSliderUpdateArt4(self):
		val=self.FKSliderArt4.value()/10
		self.SpinBoxArt4.setValue(val)
	def FKSpinBoxUpdateArt4(self):
		val=int(self.SpinBoxArt4.value()*10)
		self.FKSliderArt4.setValue(val)
	def FKDec10Art4(self):
		val=self.SpinBoxArt4.value()-10
		self.SpinBoxArt4.setValue(val)
	def FKDec1Art4(self):
		val=self.SpinBoxArt4.value()-1
		self.SpinBoxArt4.setValue(val)
	def FKDec0_1Art4(self):
		val=self.SpinBoxArt4.value()-0.1
		self.SpinBoxArt4.setValue(val)
	def FKInc0_1Art4(self):
		val=self.SpinBoxArt4.value()+0.1
		self.SpinBoxArt4.setValue(val)
	def FKInc1Art4(self):
		val=self.SpinBoxArt4.value()+1
		self.SpinBoxArt4.setValue(val)
	def FKInc10Art4(self):
		val=self.SpinBoxArt4.value()+10
		self.SpinBoxArt4.setValue(val)

#FK Art5 Functions
	def FKSliderUpdateArt5(self):
		val=self.FKSliderArt5.value()/10
		self.SpinBoxArt5.setValue(val)
	def FKSpinBoxUpdateArt5(self):
		val=int(self.SpinBoxArt5.value()*10)
		self.FKSliderArt5.setValue(val)
	def FKDec10Art5(self):
		val=self.SpinBoxArt5.value()-10
		self.SpinBoxArt5.setValue(val)
	def FKDec1Art5(self):
		val=self.SpinBoxArt5.value()-1
		self.SpinBoxArt5.setValue(val)
	def FKDec0_1Art5(self):
		val=self.SpinBoxArt5.value()-0.1
		self.SpinBoxArt5.setValue(val)
	def FKInc0_1Art5(self):
		val=self.SpinBoxArt5.value()+0.1
		self.SpinBoxArt5.setValue(val)
	def FKInc1Art5(self):
		val=self.SpinBoxArt5.value()+1
		self.SpinBoxArt5.setValue(val)
	def FKInc10Art5(self):
		val=self.SpinBoxArt5.value()+10
		self.SpinBoxArt5.setValue(val)

#FK Art6 Functions
	def FKSliderUpdateArt6(self):
		val=self.FKSliderArt6.value()/10
		self.SpinBoxArt6.setValue(val)
	def FKSpinBoxUpdateArt6(self):
		val=int(self.SpinBoxArt6.value()*10)
		self.FKSliderArt6.setValue(val)
	def FKDec10Art6(self):
		val=self.SpinBoxArt6.value()-10
		self.SpinBoxArt6.setValue(val)
	def FKDec1Art6(self):
		val=self.SpinBoxArt6.value()-1
		self.SpinBoxArt6.setValue(val)
	def FKDec0_1Art6(self):
		val=self.SpinBoxArt6.value()-0.1
		self.SpinBoxArt6.setValue(val)
	def FKInc0_1Art6(self):
		val=self.SpinBoxArt6.value()+0.1
		self.SpinBoxArt6.setValue(val)
	def FKInc1Art6(self):
		val=self.SpinBoxArt6.value()+1
		self.SpinBoxArt6.setValue(val)
	def FKInc10Art6(self):
		val=self.SpinBoxArt6.value()+10
		self.SpinBoxArt6.setValue(val)

# Gripper Functions
	def SliderUpdateGripper(self):
		val=self.SliderGripper.value()
		self.SpinBoxGripper.setValue(val)
	def SpinBoxUpdateGripper(self):
		val=int(self.SpinBoxGripper.value())
		self.SliderGripper.setValue(val)
	def Dec10Gripper(self):
		val=self.SpinBoxGripper.value()-10
		self.SpinBoxGripper.setValue(val)
	def Dec1Gripper(self):
		val=self.SpinBoxGripper.value()-1
		self.SpinBoxGripper.setValue(val)
	def Inc1Gripper(self):
		val=self.SpinBoxGripper.value()+1
		self.SpinBoxGripper.setValue(val)
	def Inc10Gripper(self):
		val=self.SpinBoxGripper.value()+10
		self.SpinBoxGripper.setValue(val)

# Serial Connection functions
	def getSerialPorts(self):
		self.SerialPortComboBox.clear()
		self.SerialPortComboBox.addItems(spf.serial_ports())

	def connectSerial(self):
		serialPort = self.SerialPortComboBox.currentText()
		if serialPort != "":
			s0.port = serialPort
			s0.baudrate = self.BaudRateComboBox.currentText()
			s0.timeout = 1
			try:
				s0.close()
				s0.open()
				# self.DAQConnected()
			except Exception as e:
				# self.IncorrectSerialErrorPopup()
				print ("error opening serial port: " + str(e))
		else:
			print ("Not serial port available")

	def updateConsole(self, dataRead):
		if dataRead=="SERIAL-DISCONNECTED":
			print ("Serial Connection Lost")
		else:
			self.ConsoleOutput.appendPlainText(dataRead)




############### SERIAL READ THREAD CLASS ###############

class SerialThreadClass(QtCore.QThread):
    serialSignal = pyqtSignal(str)
    def __init__(self, parent=None):
         super(SerialThreadClass,self).__init__(parent)
    def run(self):
        while True:
            time.sleep(0.05)
            if s0.isOpen():
                try:
                    s0.inWaiting()
                except:
                    s0.close()
                    self.serialSignal.emit("SERIAL-DISCONNECTED")
                    print ("Lost Serial connection!")
                try:
                    dataRead = str(s0.readline())
                    self.serialSignal.emit(dataRead)
                except Exception as e:
                    print ("Something failed: " + str(e))

###############  SERIAL READ THREAD CLASS ###############










if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mwindow = QtWidgets.QMainWindow()

	prog = AsgardGUI(mwindow)

	mwindow.show()
	sys.exit(app.exec_())