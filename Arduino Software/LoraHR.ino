/*
  First Configuration
  This sketch demonstrates the usage of MKR WAN 1300/1310 LoRa module.
  This example code is in the public domain.
*/

#include <MKRWAN.h>

LoRaModem modem;

unsigned long time1;                  // initialize first R time segment Reference.
unsigned long time2;                  // initialize second R time segment Reference.
unsigned long hrtimer1;                  // initialize first R time segment Reference.
unsigned long hrtimer2;                  // initialize second R time segment Reference.
unsigned long timers1;                  // initialize first R time segment Reference.
unsigned long timers2;                  // initialize second R time segment Reference.
float frec = 0; 
float memfrec = 0; 
int i=0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  while (!Serial);
  // change this to your regional band (eg. US915, AS923, ...)
  if (!modem.begin(EU868)) {
    Serial.println("Failed to start module");
    while (1) {}
  };
  Serial.print("Your module version is: ");
  Serial.println(modem.version());
  Serial.print("Your device EUI is: ");
  Serial.println(modem.deviceEUI());

  int connected;
 connected = modem.joinOTAA("YOUR_APP_EUI", "YOUR_APP_KEY");
  
   modem.minPollInterval(120);

  delay(5000);
  hrtimer1=millis();  
  Serial.println("Start system");
}

void loop() {
  while (modem.available()) {
    Serial.write(modem.read());
  }
  modem.poll();
  
  hrtimer2=millis();  
  while((hrtimer2-hrtimer1)>120000){
  Serial.print("Taking HR:");
  int lec = analogRead(A0);           // Taking the ADC value.
  if(lec > 650)                       // Set the 650 R value reference.
  {
    time2=millis();                   // Taking the second time reference.
    frec+=((60*1000)/(time2-time1));  // Get heart rate in beats per minute.
    time1=millis();                   // Taking the first time reference for the next segment. 
    i++;                              // Add 1 to counter.
    if(i>10)
    {
      frec/=11;                       // Getting the average of 11 frequency samples.
      memfrec = frec;
      Serial.println((int)memfrec);
      i=0;                            // Restart counter
      frec = 0;                       // Restart frecuency value
      hrtimer1=millis();
      hrtimer2=millis();
    }
    delay(100);                       // Wait for the R wave to end, to prevent the algorithm from detecting the same R wave, the entire QRS segment lasts between 60 and 100 milliseconds, a delay of 100 milliseconds will work perfectly.
  }
  }
  timers2=millis();  
  while((timers2-timers1)>120000){
    Serial.println("Sending...");
    if(send((int)memfrec))
    {
      timers2=millis();
      timers1=millis(); 
      break;
    }
    delay(0000);
  };
}

bool send(byte hr){
  int err;
  modem.setPort(3);
  modem.beginPacket();
  modem.print(hr);
  err = modem.endPacket(true);
  if (err > 0) {
    Serial.println("Message sent correctly!");
    return true;
  } else {
    Serial.println("Error sending message :(");
    return false;
  }
  
}
