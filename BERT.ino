// Variables

//Servo myservo; 
                                            //was D1. Arduino timer finished, hot = 0, constant heating is off
int led0 = D4;                              //got a call from IFTTT to turn the constant heating off
int led = D5;                               //60mins of constant heat request led
int hot = 0;
int pushButton = D6;                        //from Arduino and, later-on, from a physical button
//int pos = 0; 
//int analogvalue1;
//int sensor = A0;

void setup()
{
    //Serial.begin(9600);
    Particle.function("gong", gong);
    pinMode(led,OUTPUT);  
    pinMode(led0,OUTPUT);
    //pinMode(led1,OUTPUT);
    Particle.variable("hot", hot);
    pinMode(pushButton, INPUT_PULLDOWN);  
    hot = 0;
    //myservo.attach(D0);
    //pinMode(sensor,INPUT);
    //Particle.variable("analogvalue1", analogvalue1);
}



int gong(String command)
{
    if(command == "60mins")                 //IFTTT sends 60mins to gong, ie here, which sets hot = 1; This command is issued by req.py on c-Pi
    {                               
        digitalWrite(led, HIGH);            //D5 was D1
        delay(2000);
        digitalWrite(led, LOW);             //D5
        //digitalWrite(led1, LOW);          //
        hot = 1;                            //  /todo-api/req.py listens for hot = 1; then sets WebRelay/api/relays/4 state = on (GPIO 23)
        delay(5000);                        //  /todo-api/req.py runs every minute via cron job on c-Pi, this delay will overlap that 1 min delay
        //digitalWrite(led, LOW);           //D5 
    }
    
    if(command == "cancelCall")             //IFTTT variable to cancel the 60 mins of heat and, later-on, a push button too
    {                            
        //digitalWrite(led0, HIGH);         //D4
        hot = 0; 
        delay(5000);
        //digitalWrite(led0, LOW);
    }
}

void loop()
{
//  analogvalue1 = analogRead(sensor);
  
//  if (analogvalue1 > 240)
//  {
//      myservo.write((analogvalue1 - 200)/1.2);    // (3.3 * analogRead(tempPin) * 100.0) / 1024;
//      delay(150);
//  }
//  else
//  if (analogvalue1 < 240)
//  {
//      myservo.write(20);
//      delay(20); 
//  }
//  else
//  if (analogvalue1 > 380)
//  {
//      myservo.write(20);
//      delay(20); 
//  }
  
 
  int pushButtonState; 

  pushButtonState = digitalRead(pushButton);//D6

  if(pushButtonState == HIGH)
  {                                         // If we push down on the push button or receive an input from Arduino pin 8...
    hot = 0;                                // set hot to zero to cancel constant heat, this is done using LEDPIN13 on Arduino. 
                                            // Arduino reset causes ledpin13 to go high which sets hot = 0
    //digitalWrite(led1, HIGH);             //
    delay(20);
    //digitalWrite(led1, LOW);
  }
}
