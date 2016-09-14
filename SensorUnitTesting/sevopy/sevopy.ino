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
    else if (check == 'p')
    {
      servo1.writeMicroseconds(1000);
    }
  }
  delay(100);
}
