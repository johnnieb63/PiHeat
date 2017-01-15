// This #include statement was automatically added by the Particle IDE.
#include "Ubidots/Ubidots.h"

// This #include statement was automatically added by the Particle IDE.
#include "PietteTech_DHT/PietteTech_DHT.h"

/*
 * FILE:        DHT_example.cpp
 * VERSION:     0.4
 * PURPOSE:     Example that uses DHT library with two sensors
 * LICENSE:     GPL v3 (http://www.gnu.org/licenses/gpl.html)
 *
 * Example that start acquisition of DHT sensor and allows the
 * loop to continue until the acquisition has completed
 * It uses DHT.acquire and DHT.acquiring
 *
 * Change DHT_SAMPLE_TIME to vary the frequency of samples
 *
 * Scott Piette (Piette Technologies) scott.piette@gmail.com
 *      January 2014        Original Spark Port
 *      October 2014        Added support for DHT21/22 sensors
 *                          Improved timing, moved FP math out of ISR
 *      September 2016      Updated for Particle and removed dependency
 *                          on callback_wrapper.  Use of callback_wrapper
 *                          is still for backward compatibility but not used
 */


// system defines
#define DHTTYPE  DHT11              // Sensor type DHT11/21/22/AM2301/AM2302
#define DHTPIN   4         	    // Digital pin for communications
#define DHT_SAMPLE_INTERVAL   60000  // Sample every two seconds

#define TOKEN "i2atVGlr9GD2Z5TXPDLqeH6Xky9xsq"  // Put here your Ubidots TOKEN

Ubidots ubidots(TOKEN);

int value1;
int value2;
int value3;


int sensor1 = A0; //internal
int sensor2 = A1; //tank
int sensor3 = A2; //internal


int analogvalue1; //internal
int analogvalue2; //tank
int analogvalue3; //internal

int digivalue1;
int digivalue2;

/*
 * NOTE: Use of callback_wrapper has been deprecated but left in this example
 *       to confirm backwards compabibility.  Look at DHT_2sensor for how
 *       to write code without the callback_wrapper
 */
//declaration
void dht_wrapper(); // must be declared before the lib initialization

// Lib instantiate
PietteTech_DHT DHT(DHTPIN, DHTTYPE, dht_wrapper);

// globals
unsigned int DHTnextSampleTime;	    // Next time we want to start sample
bool bDHTstarted;		    // flag to indicate we started acquisition
int n;                              // counter

void setup()
{
    //Serial.begin(9600);
    //while (!Serial.available()) {
    //    Serial.println("Press any key to start.");
	//	Particle.process();
    //    delay (1000);
    // }


    DHTnextSampleTime = 0;  // Start the first sample immediately
    
    pinMode(sensor1,INPUT);
    pinMode(sensor2,INPUT);
    pinMode(sensor3,INPUT);

    Particle.variable("analogvalue1", analogvalue1); //internal
    Particle.variable("analogvalue2", analogvalue2); //tank
    Particle.variable("analogvalue3", analogvalue3); //internal
    Particle.variable("digivalue1", digivalue1);
    Particle.variable("digivalue2", digivalue2);

}


/*
 * NOTE:  Use of callback_wrapper has been deprecated but left in this example
 * to confirm backwards compatibility.
 */
// This wrapper is in charge of calling
// must be defined like this for the lib work
void dht_wrapper() {
  DHT.isrCallback();
}

void loop()
{
  // Check if we need to start the next sample
  if (millis() > DHTnextSampleTime) {
	if (!bDHTstarted) {		// start the sample
	    DHT.acquire();
	    bDHTstarted = true;
	}

	if (!DHT.acquiring()) {		// has sample completed?

	    // get DHT status
	    int result = DHT.getStatus(); //may have to set float back to int

	    

	    //Serial.print("Humidity (%): ");
	    //Serial.println(DHT.getHumidity(), 2);

	    //Serial.print("Temperature (oC): ");
	    //Serial.println(DHT.getCelsius(), 2);
	    //ubidots.add("Temperature (oC): ", DHT.getCelsius());
	
        digivalue1 = DHT.getCelsius();
        //delay(2000);
        digivalue2 = DHT.getHumidity();
        //delay(2000);
        ubidots.add("Cavity temp", digivalue1);
        //delay(2000);
        ubidots.add("Cavity humid", digivalue2);
        //delay(2000);
        
        analogvalue1 = analogRead(sensor1);
        //delay(2000);
        analogvalue2 = analogRead(sensor2);
        //delay(2000);
        analogvalue3 = analogRead(sensor3);
        //delay(2000);
        ubidots.add("attic", analogvalue1); //internal
        //delay(2000);
        ubidots.add("attic2", analogvalue2); //tank
        //delay(2000);
        ubidots.add("attic3", analogvalue3); //internal
        //delay(2000);
        ubidots.sendAll();
        //delay(50000);  

    
    	n++;  // increment counter
	    bDHTstarted = false;  // reset the sample flag so we can take another
	    DHTnextSampleTime = millis() + DHT_SAMPLE_INTERVAL;  // set the time for next sample
	}

    }
}
