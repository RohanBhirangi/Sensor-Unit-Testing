"""
This program controls the servo (turn table)
This is the code that will be uploaded to
the Arduino board
The Arduino is controlled by the ut_test.py
which prints 'y' or 'n' to the serial port.
This causes the turn table to move clockwise
or anti clockwise
"""


#include <Servo.h>

Servo servo1;
void setup() 
{
  Serial.begin(9600); 
  Serial.println("Start"); 
  servo1.attach(9);
}
void loop() 
{
  if(Serial.available())
  { 
    char check = Serial.read(); 
    Serial.println(check);
    if (check == 'y')
    {
      servo1.writeMicroseconds(2000);
    }
    else if (check == 'n')
    {
      servo1.writeMicroseconds(1500);
    }
   }
  delay(100);
}
