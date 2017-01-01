int led1 = D5;                              //Arduino timer finished, hot = 0, constant heating is off
int led0 = D4;                              //got a call from IFTTT to turn the constant heating off
int led = D1;                               //60mins of constant heat request led

int hot = 0;
int pushButton = D3;                        //from Arduino and, later-on, from a physical button

void setup()
{
    Particle.function("gong", gong);
    pinMode(led,OUTPUT);  
    pinMode(led0,OUTPUT);
    pinMode(led1,OUTPUT);
    Particle.variable("hot", hot);
    pinMode(pushButton, INPUT_PULLUP);  
    hot = 0;
}

int gong(String command)   
{
    if(command == "60mins")                 //IFTTT sends 60mins to gong, ie here, which sets hot = 1;
    {                               
        digitalWrite(led, HIGH); //D1
        delay(2000);
        digitalWrite(led0, LOW);
        digitalWrite(led1, LOW);
        hot = 1;                            //  /todo-api/req.py listens for hot = 1; then sets WebRelay/api/relays/4 state = on (GPIO 23)
        delay(5000);                        //  /todo-api/req.py runs every minute via cron job on c-Pi, this delay will overlap that 1 min delay
        digitalWrite(led, LOW);
    }
    
    if(command == "cancelCall")             //IFTTT variable to cancel the 60 mins of heat and, later-on, a push button too
    {                            
      digitalWrite(led0, HIGH); //D4
        hot = 0; 
        delay(5000);
        digitalWrite(led0, LOW);
    }

}

void loop()
{
  int pushButtonState; 

  pushButtonState = digitalRead(pushButton);

  if(pushButtonState == HIGH)
  {                                         // If we push down on the push button or receive an input from Arduino pin 8...
    hot = 0;                                // set hot to zero to cancel constant heat
    digitalWrite(led1, HIGH);               //D5
    delay(2000);
    digitalWrite(led1, LOW);
  }
  //else
  //{
//    digitalWrite(led1, LOW); 
  //}

}
