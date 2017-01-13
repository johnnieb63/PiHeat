// This #include statement was automatically added by the Particle IDE.
#include "Ubidots/Ubidots.h"

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

#include "PietteTech_DHT/PietteTech_DHT.h"  // Uncomment if building in IDE
//#include "PietteTech_DHT.h"                 // Uncomment if building using CLI

// system defines
#define DHTTYPE  DHT11              // Sensor type DHT11/21/22/AM2301/AM2302
#define DHTPIN   4         	    // Digital pin for communications
#define DHT_SAMPLE_INTERVAL   2000  // Sample every two seconds

#define TOKEN "i2-yours-goes-here-sq"  // Put here your Ubidots TOKEN

Ubidots ubidots(TOKEN);

int value1;
int value2;

int sensor1 = A0;
int sensor2 = A1;

int analogvalue1;
int analogvalue2;
int analogvalue3;
int analogvalue4;

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


    //DHTnextSampleTime = 0;  // Start the first sample immediately
    
    pinMode(sensor1,INPUT);
    pinMode(sensor2,INPUT);

    Particle.variable("analogvalue1", analogvalue1);
    Particle.variable("analogvalue2", analogvalue2);
    Particle.variable("analogvalue3", analogvalue3);
    Particle.variable("analogvalue4", analogvalue4);
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
  //if (millis() > DHTnextSampleTime) {
	//if (!bDHTstarted) {		// start the sample
	    DHT.acquire();
	    bDHTstarted = true;
//	}

//	if (!DHT.acquiring()) {		// has sample completed?

	    // get DHT status
	    float result = DHT.getStatus(); //may have to set float back to int

	    

	    //Serial.print("Humidity (%): ");
	    //Serial.println(DHT.getHumidity(), 2);

	    //Serial.print("Temperature (oC): ");
	    //Serial.println(DHT.getCelsius(), 2);
	    //ubidots.add("Temperature (oC): ", DHT.getCelsius());
	    
	
	
	analogvalue1 = analogRead(sensor1);
    delay(2000);
    analogvalue2 = analogRead(sensor2);
    delay(2000);
    analogvalue3 = DHT.getCelsius();
    delay(2000);
    analogvalue4 = DHT.getHumidity();

    ubidots.add("attic", analogvalue1);
    delay(2000);
    ubidots.add("attic2", analogvalue2);
    delay(2000);
    ubidots.add("attic3", analogvalue3);
    delay(2000);
    ubidots.add("humidity", analogvalue4);
    delay(2000);
    ubidots.sendAll();
    delay(50000);  
    
    //	n++;  // increment counter
	  //  bDHTstarted = false;  // reset the sample flag so we can take another
	   // DHTnextSampleTime = millis() + DHT_SAMPLE_INTERVAL;  // set the time for next sample
	//}

    //}
}

