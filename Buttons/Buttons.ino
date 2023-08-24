using namespace std;
#include <string>
#include "dummy.cpp"


class block
{
  public:
    int ledPin;
    block(int _ledPin)
    {
        ledPin = _ledPin;
    }
    void print()
    {
        // Serial.print("Hello");
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
    void turnOn()
    {

    }
    void turnOff()
    {

    }
};

// Create an int called LED_BUILTIN

int LED_BUILTIN2 = 2;
int LED_BUILTIN3 = 3;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN2, OUTPUT);
  pinMode(LED_BUILTIN3, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN2, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN2, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);   

  digitalWrite(LED_BUILTIN3, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  digitalWrite(LED_BUILTIN3, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);   
}
