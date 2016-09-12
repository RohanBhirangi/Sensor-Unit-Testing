#!C:\Python27\python.exe
import serial
ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
print ser.readline()
while True: 
     check = raw_input("Are you ready? ")
     ser.write(check)
     if(check=='exit'):
     	ser.close()
     	exit()