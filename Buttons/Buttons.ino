using namespace std;
// #include "dummy.cpp"
// #include <vector>
#include <Vector.h>
#define NUMBER_OF_BLOCKS 5
#define STARTING_PIN 4

class block
{
  public:
    int ledPin;
    block(int _ledPin)
    {
        ledPin = _ledPin;
        setPinmode();
    }
    void blink()
    {
        // Serial.print("Hello");
        digitalWrite(ledPin, HIGH);  // turn the LED on (HIGH is the voltage level)
        delay(1000);                      // wait for a second
        digitalWrite(ledPin, LOW);   // turn the LED off by making the voltage LOW
        delay(1000);    
    }    
  private:
    void setPinmode()
    {
       pinMode(ledPin, OUTPUT);
    }

};

// Create an int called LED_BUILTIN

Vector<block> objects;

void setup() {
  // put your setup code here, to run once:
  for (int i; i < NUMBER_OF_BLOCKS; i++)
  {
    objects.push_back(block(STARTING_PIN + i));
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int i; i < NUMBER_OF_BLOCKS; i++)
  {
    objects[i].blink();
  }
 
}
