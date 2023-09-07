#include <LedControl.h>
// Including the required Arduino libraries
#include <MD_Parola.h>
#include <MD_MAX72xx.h>
#include <SPI.h>

// Uncomment according to your hardware type
#define HARDWARE_TYPE MD_MAX72XX::FC16_HW
//#define HARDWARE_TYPE MD_MAX72XX::GENERIC_HW

// Defining size, and output pins
#define MAX_DEVICES 4
#define CS_PIN 3

// Create a new instance of the MD_Parola class with hardware SPI connection
// MD_Parola myDisplay = MD_Parola(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);
//(DIN, CLK, CS, # Devices
// LedControl lc=LedControl(11,13,3,3);
// LedControl lc=LedControl(11,13,3,4);
LedControl lc=LedControl(12,11,10,4);
int buttonState = 0;
int buttonPin = 6;

void setup() {
    // // Intialize the object
    // myDisplay.begin();
     pinMode(buttonPin, INPUT);
    // // Set the intensity (brightness) of the display (0-15)
    // myDisplay.setIntensity(0);

    // // Clear the display
    // myDisplay.displayClear();
    Serial.begin(9600);
    int Compteur_0 = 0;
    for (Compteur_0=0; Compteur_0 <= 4; Compteur_0++);
    { 
      lc.shutdown(Compteur_0, false);
      lc.setIntensity(Compteur_0,8); // Set brightness to a medium value
      lc.clearDisplay(Compteur_0); // Clear the display
    }
    // Serial.println(lc.getDeviceCount());
    // Serial.println("Hello");
    lc.shutdown(0,false);
    // Set brightness to a medium value
    lc.setIntensity(0,8);
    // Clear the display
    lc.clearDisplay(0);
}

void loop() {
  // myDisplay.setTextAlignment(PA_LEFT);
	// myDisplay.print("Left");
	// delay(2000);
	// Serial.println("Hello");
  buttonState = digitalRead(buttonPin);
    if (buttonState == HIGH){
      Serial.println("Hello");
      lc.setLed(0,0,1,true); 	
    }
    else{
      lc.setLed(0,0,1, false);
    }
      
	// myDisplay.setTextAlignment(PA_CENTER);
	// myDisplay.print("Center");
	// delay(2000);

	// myDisplay.setTextAlignment(PA_RIGHT);
	// myDisplay.print("Right");
	// delay(2000);

	// myDisplay.setTextAlignment(PA_CENTER);
	// myDisplay.setInvert(true);
	// myDisplay.print("Invert");
	// delay(2000);

	// myDisplay.setInvert(false);
	// myDisplay.print(1234);
	// delay(2000);
}