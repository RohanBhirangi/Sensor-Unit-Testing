import serial
import time

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)

def turn_table_right():
	ser.write("y")
	print "in right"
	print get_acceleration()
	time.sleep(3)

def turn_table_left():
	ser.write("n")
	print "in left"
	print get_acceleration()
	time.sleep(3)

def get_acceleration():
	return 0.0,0.0,9.8

def main():
	time.sleep(3)
	while True: 		
		turn_table_right()
		turn_table_left()
		
if __name__ == '__main__':
	main()