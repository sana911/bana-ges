#
# AUTHOR: Sanath Arage
# VERSION: 2.1
# LAST CHANGE LOG:  9/10/17 :: 21:45 :: VR's fixed
#                   9/10/17 :: 21:40 :: Code cleaned
#
#
# CHECK: Check without time.sleep
#==========================================================================================================#
#==========================================================================================================#
#==========================================================================================================#

import Leap, sys, time, thread ,threading
from Leap import CircleGesture #, KeyTapGesture #, ScreenTapGesture ,SwipeGesture
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusTcpClient
import argparse

#==============================================================================================#
#==============================================================================================#


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ipad", help = "pass the ip address")
args = vars(ap.parse_args())

#==============================================================================================#
#==============================================================================================#

client = ModbusTcpClient(str(args["ipad"]))
client.connect()

#==============================================================================================#
#==============================================================================================#

print str(args["ipad"])
client.write_register(3601,0)
#####rs = 0
#####ls = 0
#####a = 1
#==============================================================================================#
#==============================================================================================#

def joint_f(x):
	return{
		10000 : 1,
		1000 : 1,
		100 : 1,
		10 : 1,
		1 : 1,
		11000 : 2,
		1100 : 2,
		11 : 2,
		11100 : 3,
		1110 : 3,
		111 : 3,
		11001 : 3,
		1111 : 4,
		11110 : 4,
		11111 : 5
	}.get(x , 0)

#==============================================================================================#
#==============================================================================================#

"""#""class mythread (threading.Thread):
	curn = 0
	prevn = 0
	def __init__ (self , threadID ,name ):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
	def run(self):
		####print "hear1"
		while a==1:
			self.prevn = self.curn
			#self.curn = ls
			if self.prevn != ls:
				print "I sense a change in the force""#"""

#==============================================================================================#
#==============================================================================================#

class SampleListener(Leap.Listener):
	times = 0

	prev = 0
	cur = 0
	prevg = 0
	curg = 0
	sp = 0
	spg = 0
	times = 0
	timesg = 0
	pa = 0
	ca = 0
	pb = 0
	cb = 0
	finger_names = [ 1 , 2 , 3 , 4 , 5 ]
	bone_names = ['metacarpal','proximal','intermediate','distal']
	state_names = ['state_invalid','state_start','state_update','state_end']

#==============================================================================================#
#==============================================================================================#

	def on_init(self , controller):
		print("Listener Initialized")

	def on_connect(self , controller):
		print(" Connected")
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
		#controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
		"""controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);"""

	def on_disconnect(self , controller):
		print("Disconnected")

	def on_exit(self , controller):
		print("Exiting")

#==============================================================================================#
#==============================================================================================#

	def on_frame(self , controller):
		tempa = 0
		#@@@@@print "NEW CYCLE___________________________________"
		frame = controller.frame()
		"""#print "frame-id" + str(frame.id) + "       Time_stamp:" \
		#+ str(frame.timestamp) + "       hands:" + str(len(frame.hands)) \
		#+ "     fingers" + str(len(frame.fingers)) \
		#+ "        no: of gestures detected" + str(len(frame.gestures()))"""
		handType = -1

#==============================================================================================#
#==============================================================================================#

		for hand in frame.hands:

			handType = 1 if hand.is_left else 0
			###	print "NO MOVE"
			if handType == 1:
				op = 00000
				opt1 = 0
				opt2 = 0
				opt3 = 0
				opt4 = 0
				opt5 = 0
				for finger in hand.fingers:
					fingertype = self.finger_names[finger.type]
			###		print 'finger:  ' + str(fingertype) # + 'l=    ' + str(finger.length)
					#for b in range(0,4):
					bne = finger.bone(2)
					if fingertype == 1:
						if (bne.direction[1] * Leap.RAD_TO_DEG) < 0 :
							opt1 = 0
						else:
							opt1 = 0
					elif fingertype == 2:
						if (bne.direction[2] * Leap.RAD_TO_DEG) > 0:
							opt2 = 1
						else:
							opt2 = 0
					elif fingertype == 3:
						if (bne.direction[2] * Leap.RAD_TO_DEG) > 0:
							opt3 = 1
						else:
							opt3 = 0
					elif fingertype == 4:
						if (bne.direction[2] * Leap.RAD_TO_DEG) > 0:
							opt4 = 1
						else:
							opt4 = 0
					elif fingertype == 5:
						if (bne.direction[2] * Leap.RAD_TO_DEG) > 0:
							opt5 = 1
						else:
							opt5 = 0
					else:
						pass
					#op = 10000*opt1 + 1000*opt2 + 100*opt3 + 10*opt4 +opt5
					op = opt1 + opt2 +opt3 + opt4 + opt5
					#bn = self.bone_names[bne.type]
			###	print 'print     :'+str(op)
#==============================================================================================#
#==============================================================================================#

				self.prev = self.cur
				self.cur = op
				if self.prev == self.cur:
					self.times = self.times + 1
				elif self.prev != self.cur:
					self.times = 0
				if self.times == 7:
					self.sp = op
					#####ls = self.sp
#==============================================================================================#

				self.pa = self.ca
				self.ca = self.sp
				if self.pa == self.ca:
					x = 0
				else:
					client.write_register(3603,self.ca)
					print "AXIS/JOINT TO MOVE  ::  " + str(self.ca)
					time.sleep(0.5)

#==============================================================================================#
#==============================================================================================#
		###	print "end of 1 hand"
		#@@@@@clockwiseness = 0
#==============================================================================================#
#==============================================================================================#

		if len(frame.gestures()) == 0:
			clockwiseness = 0
		for gesture in frame.gestures():

			"""if gesture.type != Leap.Gesture.TYPE_CIRCLE and gesture.type != Leap.Gesture.TYPE_KEY_TAP:
				clockwiseness == 0
		 ###print "joint to move: " +str(self.sp) +"dir  :" +str(clockwiseness)"""
			if gesture.type == Leap.Gesture.TYPE_CIRCLE:
				circle = Leap.CircleGesture(gesture)
				#print str(circle.pointable)
				if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
					clockwiseness = 1
 				else:
					clockwiseness = 2
				#print "Circle detected" + str(clockwiseness)+"  no of fingers  :"
				#print str(gesture.handType)
		#3#		if len(circle.pointable) == 1:
			#		tempa = 1
				#else:
					#tempa = 0
	#	if tempa == 1 :
#==============================================================================================#
#==============================================================================================#

		self.prevg = self.curg
		self.curg = clockwiseness
		if self.prevg == self.curg:
			self.timesg = self.timesg + 1
			#print "#-----------------------------------------ignoring state change"
		elif self.prevg != self.curg:
			self.timesg = 0
		if self.timesg == 2:
			self.spg = clockwiseness


		self.pb = self.cb
		self.cb = self.spg
		if self.pb == self.cb:
			y=0
		else:
			print "MOTION DIRECTION  ::  "+ str(self.cb)
			client.write_register(3604,self.cb)

#==============================================================================================#
#==============================================================================================#
			#

			#	if clockwiseness == 1 or clockwiseness == -1:
					#@@@@@joint = joint_f(op)
					#@@@@rs = clockwiseness
			#		print "joint to move: " +str(self.sp) +"dir  :" +str(clockwiseness)
			#	else:
			#		print "no move command"""


			#if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
			#	tap = Leap.KeyTapGesture(gesture)
			#	joint = joint_f(op)
			#	print "++++++++++++++++++++++++++++++++++++++++++++++joint to move:   " + str(op) + " by 1 degrees+++++++++++++++++++++++++++++++++++++++++++++++++++++++"
			#	time.sleep(0.5)"""

#==============================================================================================#
#==============================================================================================#

def main():
	listener = SampleListener()
	controller = Leap.Controller()
	#####th1 = mythread(1,'Asshat')
	#####th1.start()

	controller.add_listener(listener)
	print ("press enter to quit")
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		a=0
		#client.write_register(3601,0)
		controller.remove_listener(listener)

		sys.exit()

#==============================================================================================#
#==============================================================================================#

if __name__ == "__main__":
	main()
