"""
This python script should effectively be able to
start and control the turn table while simultaneously
making calls to sensor functions.

The main goal is to automate the entire seash process
(loadkeys, browse, add, upload, execute) using this
python script.
So that the user just has to run this single program
to test the sensor api calls.

For now, this script is not dependent on the Arduino version.
But it would be really cool if we can upload the C code on
to the Arduino board through this python script.
"""

import serial
import time

#Use Py Serial library for communicating with the Arduino
#For mac users, the port should be '/dev/cu.usbmodem1421'
#or '/dev/tty.usbmodem1421'
#For Windows, the port should be COM1 or something similar
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

#This funcation rotates the turn table clockwise for
#3 seconds and calls the dummy get_acceleration function
def turn_table_right():
	ser.write("y")
	print "in right"
	print get_acceleration()
	time.sleep(3)

#This funcation rotates the turn table anit-clockwise for
#3 seconds and calls the dummy get_acceleration function
def turn_table_left():
	ser.write("n")
	print "in left"
	print get_acceleration()
	time.sleep(3)

#A dummy acceleration function since we are not yet able
#to access Sensibility Sensor APIs through Python
def get_acceleration():
	return 0.0,0.0,9.8

def main():
	time.sleep(3)
	while True: 		
		turn_table_right()
		turn_table_left()
		
if __name__ == '__main__':
	main()