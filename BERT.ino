// This #include statement was automatically added by the Particle IDE.
#include "Ubidots/Ubidots.h"

#define TOKEN "-----yours here-----"  // Put here your Ubidots TOKEN
                                            
int pushButtonState; 
int led = D5;                               //constant heat request led
int hot = 0;
int pushButton = D6;                        //a physical cancel button
int analogvalue;                            //kitchen
int analogvalue1;                           //tank
int analogvalue2;                           //boiler
int analogvalue3;                           //external
int sensor = A0;                            //kitchen
int sensor1 = A1;                           //tank
int sensor2 = A2;                           //boiler
int sensor3 = A3;                           //external
unsigned int countHeatOnTime;
unsigned int measureTempTime;


Ubidots ubidots(TOKEN);

void setup()
{
    //Serial.begin(9600);
    pinMode(sensor,INPUT);
    pinMode(sensor1,INPUT);
    pinMode(sensor2,INPUT);
    pinMode(sensor3,INPUT);
    Particle.function("gong", gong);
    pinMode(led,OUTPUT);  
    Particle.variable("hot", hot);
    pinMode(pushButton, INPUT_PULLDOWN);  
    hot = 0;
    Particle.variable("analogvalue", analogvalue);
    Particle.variable("analogvalue1", analogvalue1);
    Particle.variable("analogvalue2", analogvalue2);
    Particle.variable("analogvalue3", analogvalue3);
    measureTempTime = 0;
    countHeatOnTime = 0;
}



int gong(String command)
{
    if(command == "60mins")                 //IFTTT sends 60mins to gong, ie here, which sets hot = 1; This command is received by req.py on c-Pi
    {                               
        digitalWrite(led, HIGH);            //D5
        hot = 1;                            //  /todo-api/req.py listens for hot = 1; then sets WebRelay/api/relays/4 state = on (GPIO 23)
        countHeatOnTime = millis() + 1800000; // set the time to end constant heat
    }
    
    if(command == "cancelCall")             //IFTTT variable to cancel the 60 mins of heat and, later-on, a push button too
    {                            
        hot = 0;
        digitalWrite(led, LOW);
    }
}

void loop()
{
  if (millis() > countHeatOnTime) {
	hot = 0; 
	digitalWrite(led, LOW); 
    }
    
  if (millis() > measureTempTime) {
    analogvalue = analogRead(sensor);
    ubidots.add("kitchen", analogvalue);      

    analogvalue1 = analogRead(sensor1);
    ubidots.add("tank", analogvalue1);

    analogvalue2 = analogRead(sensor2);
    ubidots.add("boiler", analogvalue2);

    analogvalue3 = analogRead(sensor3);
    ubidots.add("external", analogvalue3);
    ubidots.sendAll(); 
    measureTempTime = millis() + 60000;     // read sensors again in 1 minute  
    }

  
  pushButtonState = digitalRead(pushButton);//D6

  if(pushButtonState == HIGH) {             // If we push down on the push button
    hot = 0;                                //  
    digitalWrite(led, LOW); 
  }
}
