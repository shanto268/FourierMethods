#include <SPI.h>
#include <RF24.h>
#include <RF24Network.h>


const byte Address = "00001";

RF24 radio(7,8); // Create a Radio
RF24Network network(radio);

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    SPI.begin();
    radio.begin();
    radio.openReadingPipe(0, address);
    radio.setDataRate( RF24_2MBPS );
    radio.startListening();
}

void loop() {
  // put your main code here, to run repeatedly:
    if (radio.available()) 
    {
      char text[32] = "";
      radio.read(&text, sizeof(text));
      Serial.println(text);
    }  
}
