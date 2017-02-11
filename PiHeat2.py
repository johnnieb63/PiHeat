# Raspberry Pi custom appliance timer

# import GPIO module
import RPi.GPIO as GPIO
import I2C_LCD_driver

# import date and time modules
import datetime
import time
from datetime import date
from datetime import timedelta

# set up GPIO pins as outputs
GPIO.setmode(GPIO.BCM)
#GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn heating on
GPIO.setup(27, GPIO.OUT) # Appliance 5/25 volt relay
#GPIO.setup(24, GPIO.OUT) # LED
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn heating off
GPIO.setup(12, GPIO.IN) #low heat condition HEATING IS OFF DUE TO THERMOSTAT
GPIO.setup(16, GPIO.IN) #medium ECO_MODE
GPIO.setup(20, GPIO.IN) #high BLAST HEAT
GPIO.setup(23, GPIO.IN) #60mins constant heat via swith (to be fitted) or via IFTTT
# set heating relay and indicator light off
#GPIO.output(24, False)
GPIO.output(27, False)

MonAMOn = datetime.datetime(1920,1,1,6,0,0)
MonAMOff = datetime.datetime(1920,1,1,7,30,0)
MonAM2On = datetime.datetime(1920,1,1,7,45,0)
MonAM2Off = datetime.datetime(1920,1,1,8,0,0)
MonAM3On = datetime.datetime(1920,1,1,8,15,0)
MonAM3Off = datetime.datetime(1920,1,1,8,30,0)

MonPMOn = datetime.datetime(1920,1,1,15,30,0)
MonPMOff = datetime.datetime(1920,1,1,16,0,0)
MonPM2On = datetime.datetime(1920,1,1,16,30,0)
MonPM2Off = datetime.datetime(1920,1,1,17,30,0)
MonPM3On = datetime.datetime(1920,1,1,18,0,0)
MonPM3Off = datetime.datetime(1920,1,1,21,0,0)

TueAMOn = datetime.datetime(1920,1,1,6,0,0)
TueAMOff = datetime.datetime(1920,1,1,7,30,0)
TueAM2On = datetime.datetime(1920,1,1,7,45,0)
TueAM2Off = datetime.datetime(1920,1,1,8,0,0)
TueAM3On = datetime.datetime(1920,1,1,8,15,0)
TueAM3Off = datetime.datetime(1920,1,1,8,30,0)

TuePMOn = datetime.datetime(1920,1,1,15,30,0)
TuePMOff = datetime.datetime(1920,1,1,16,0,0)
TuePM2On = datetime.datetime(1920,1,1,16,30,0)
TuePM2Off = datetime.datetime(1920,1,1,18,30,0)
TuePM3On = datetime.datetime(1920,1,1,20,0,0)
TuePM3Off = datetime.datetime(1920,1,1,21,0,0)

WedAMOn = datetime.datetime(1920,1,1,6,0,0)
WedAMOff = datetime.datetime(1920,1,1,7,30,0)
WedAM2On = datetime.datetime(1920,1,1,7,45,0)
WedAM2Off = datetime.datetime(1920,1,1,8,0,0)
WedAM3On = datetime.datetime(1920,1,1,8,15,0)
WedAM3Off = datetime.datetime(1920,1,1,8,30,0)

WedPMOn = datetime.datetime(1920,1,1,15,30,0)
WedPMOff = datetime.datetime(1920,1,1,16,0,0)
WedPM2On = datetime.datetime(1920,1,1,16,30,0)
WedPM2Off = datetime.datetime(1920,1,1,17,30,0)
WedPM3On = datetime.datetime(1920,1,1,18,0,0)
WedPM3Off = datetime.datetime(1920,1,1,21,0,0)

ThuAMOn = datetime.datetime(1920,1,1,6,0,0)
ThuAMOff = datetime.datetime(1920,1,1,7,30,0)
ThuAM2On = datetime.datetime(1920,1,1,7,45,0)
ThuAM2Off = datetime.datetime(1920,1,1,8,0,0)
ThuAM3On = datetime.datetime(1920,1,1,8,15,0)
ThuAM3Off = datetime.datetime(1920,1,1,8,30,0)

ThuPMOn = datetime.datetime(1920,1,1,15,30,0)
ThuPMOff = datetime.datetime(1920,1,1,16,0,0)
ThuPM2On = datetime.datetime(1920,1,1,16,30,0)
ThuPM2Off = datetime.datetime(1920,1,1,17,30,0)
ThuPM3On = datetime.datetime(1920,1,1,18,0,0)
ThuPM3Off = datetime.datetime(1920,1,1,21,0,0)

FriAMOn = datetime.datetime(1920,1,1,6,0,0)
FriAMOff = datetime.datetime(1920,1,1,7,30,0)
FriAM2On = datetime.datetime(1920,1,1,7,45,0)
FriAM2Off = datetime.datetime(1920,1,1,8,0,0)
FriAM3On = datetime.datetime(1920,1,1,8,15,0)
FriAM3Off = datetime.datetime(1920,1,1,8,30,0)

FriPMOn = datetime.datetime(1920,1,1,15,30,0)
FriPMOff = datetime.datetime(1920,1,1,16,0,0)
FriPM2On = datetime.datetime(1920,1,1,16,30,0)
FriPM2Off = datetime.datetime(1920,1,1,17,30,0)
FriPM3On = datetime.datetime(1920,1,1,18,0,0)
FriPM3Off = datetime.datetime(1920,1,1,21,0,0)

SatAMOn = datetime.datetime(1920,1,1,6,0,0)
SatAMOff = datetime.datetime(1920,1,1,8,0,0)
SatAM2On = datetime.datetime(1920,1,1,8,45,0)
SatAM2Off = datetime.datetime(1920,1,1,9,0,0)
SatAM3On = datetime.datetime(1920,1,1,9,10,0)
SatAM3Off = datetime.datetime(1920,1,1,9,15,0)

SatPMOn = datetime.datetime(1920,1,1,15,30,0)
SatPMOff = datetime.datetime(1920,1,1,16,0,0)
SatPM2On = datetime.datetime(1920,1,1,16,30,0)
SatPM2Off = datetime.datetime(1920,1,1,17,30,0)
SatPM3On = datetime.datetime(1920,1,1,18,0,0)
SatPM3Off = datetime.datetime(1920,1,1,21,0,0)

SunAMOn = datetime.datetime(1920,1,1,6,0,0)
SunAMOff = datetime.datetime(1920,1,1,8,0,0)
SunAM2On = datetime.datetime(1920,1,1,8,45,0)
SunAM2Off = datetime.datetime(1920,1,1,9,0,0)
SunAM3On = datetime.datetime(1920,1,1,9,10,0)
SunAM3Off = datetime.datetime(1920,1,1,9,15,0)

SunPMOn = datetime.datetime(1920,1,1,15,30,0)
SunPMOff = datetime.datetime(1920,1,1,16,0,0)
SunPM2On = datetime.datetime(1920,1,1,16,30,0)
SunPM2Off = datetime.datetime(1920,1,1,17,30,0)
SunPM3On = datetime.datetime(1920,1,1,18,0,0)
SunPM3Off = datetime.datetime(1920,1,1,21,0,0)


# Store these times in an array for easy access later.
OnTimeAM = [MonAMOn, TueAMOn, WedAMOn, ThuAMOn, FriAMOn, SatAMOn, SunAMOn]
OnTimePM = [MonPMOn, TuePMOn, WedPMOn, ThuPMOn, FriPMOn, SatPMOn, SunPMOn]
OffTimeAM = [MonAMOff, TueAMOff, WedAMOff, ThuAMOff, FriAMOff, SatAMOff, SunAMOff]
OffTimePM = [MonPMOff, TuePMOff, WedPMOff, ThuPMOff, FriPMOff, SatPMOff, SunPMOff]

OnTime2AM = [MonAM2On, TueAM2On, WedAM2On, ThuAM2On, FriAM2On, SatAM2On, SunAM2On]
OnTime2PM = [MonPM2On, TuePM2On, WedPM2On, ThuPM2On, FriPM2On, SatPM2On, SunPM2On]
OffTime2AM = [MonAM2Off, TueAM2Off, WedAM2Off, ThuAM2Off, FriAM2Off, SatAM2Off, SunAM2Off]
OffTime2PM = [MonPM2Off, TuePM2Off, WedPM2Off, ThuPM2Off, FriPM2Off, SatPM2Off, SunPM2Off]

OnTime3AM = [MonAM3On, TueAM3On, WedAM3On, ThuAM3On, FriAM3On, SatAM3On, SunAM3On]
OnTime3PM = [MonPM3On, TuePM3On, WedPM3On, ThuPM3On, FriPM3On, SatPM3On, SunPM3On]
OffTime3AM = [MonAM3Off, TueAM3Off, WedAM3Off, ThuAM3Off, FriAM3Off, SatAM3Off, SunAM3Off]
OffTime3PM = [MonPM3Off, TuePM3Off, WedPM3Off, ThuPM3Off, FriPM3Off, SatPM3Off, SunPM3Off]

cTemp = 10
whenNext = OnTime3AM
whenNextOff = OffTime3AM
dateString = '%H:%M:%S'
mylcd = I2C_LCD_driver.lcd()
dateString2 = '%H:%M'
currDay = datetime.date.today().weekday()
tomDay = (datetime.date.today()+ datetime.timedelta(days=1)).weekday()

mylcd.lcd_display_string("Hello World!", 1)
mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString), 2)
mylcd.lcd_display_string("Coffee on?", 2)
time.sleep(5)
mylcd.lcd_clear()

# Start the loop that will run until you stop the program or turn off your Raspberry Pi.

while True:


        #while (GPIO.input(17) == 1):
                   #GPIO.output(24, True)
                   #GPIO.output(27, True)
                   #mylcd.lcd_display_string("HEAT VIA MOBILE", 1)
                   #mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                   #time.sleep(2)
                   #mylcd.lcd_clear()

        while (GPIO.input(23) == 1):
                   #GPIO.output(24, True)
                   GPIO.output(27, True)
                   mylcd.lcd_display_string("1 hour of heat", 1)
                   mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                   time.sleep(2)
                   mylcd.lcd_clear()

        #GPIO.output(24, False)
        GPIO.output(27, False)
        mylcd.lcd_display_string("HEATING IS OFF", 1)
        mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
        time.sleep(3)
        mylcd.lcd_clear()

        if (datetime.datetime.now().strftime(dateString) >= OnTimeAM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OffTimeAM[currDay].strftime(dateString)):
          whenNext = OnTimeAM
          whenNextOff = OffTimeAM
        if (datetime.datetime.now().strftime(dateString) < OnTimeAM[currDay].strftime(dateString)):
          mylcd.lcd_display_string(OnTimeAM[currDay].strftime(dateString2), 2)
          mylcd.lcd_display_string("next on time (1)", 1)

        if (datetime.datetime.now().strftime(dateString) >= OnTime2AM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OffTime2AM[currDay].strftime(dateString)):
          whenNext = OnTime2AM
          whenNextOff = OffTime2AM
        if (datetime.datetime.now().strftime(dateString) > OffTimeAM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OnTime2AM[currDay].strftime(dateString)):
          mylcd.lcd_display_string(OnTime2AM[currDay].strftime(dateString2), 2)
          mylcd.lcd_display_string("next on time (2)", 1)
        if (datetime.datetime.now().strftime(dateString) >= OnTime3AM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OffTime3AM[currDay].strftime(dateString)):
          whenNext = OnTime3AM
          whenNextOff = OffTime3AM
        if (datetime.datetime.now().strftime(dateString) > OffTime2AM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OnTime3AM[currDay].strftime(dateString)):
          mylcd.lcd_display_string((OnTime3AM[currDay].strftime(dateString)), 2)
          mylcd.lcd_display_string("next on time (3)", 1)

        if (datetime.datetime.now().strftime(dateString) >= OnTimePM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OffTimePM[currDay].strftime(dateString)):
          whenNext = OnTimePM
          whenNextOff = OffTimePM
        if (datetime.datetime.now().strftime(dateString) > OffTime3AM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OnTimePM[currDay].strftime(dateString)):
          mylcd.lcd_display_string((OnTimePM[currDay].strftime(dateString2)), 2)
          mylcd.lcd_display_string("next on time (4)", 1)

        if (datetime.datetime.now().strftime(dateString) >= OnTime2PM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OffTime2PM[currDay].strftime(dateString)):
          whenNext = OnTime2PM
          whenNextOff = OffTime2PM
        if (datetime.datetime.now().strftime(dateString) > OffTimePM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OnTime2PM[currDay].strftime(dateString)):
          mylcd.lcd_display_string((OnTime2PM[currDay].strftime(dateString2)), 2)
          mylcd.lcd_display_string("next on time (5)", 1)

        if (datetime.datetime.now().strftime(dateString) >= OnTime3PM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OffTime3PM[currDay].strftime(dateString)):
          whenNext = OnTime3PM
          whenNextOff = OffTime3PM
        if (datetime.datetime.now().strftime(dateString) > OffTime2PM[currDay].strftime(dateString) and datetime.datetime.now().strftime(dateString) < OnTime3PM[currDay].strftime(dateString)):
          mylcd.lcd_display_string((OnTime3PM[currDay].strftime(dateString2)), 2)
          mylcd.lcd_display_string("next on time (6)", 1)

        if (datetime.datetime.now().strftime(dateString) > OffTime3PM[currDay].strftime(dateString)):
          mylcd.lcd_display_string((OnTimeAM[tomDay].strftime(dateString2)), 2)
          mylcd.lcd_display_string("next on tomorrow", 1)
        time.sleep(5)
        mylcd.lcd_clear()


#Check to see if it's time to run the appliance for the AM hours


#switch on       
        while (whenNext[currDay].strftime(dateString) <= datetime.datetime.now().strftime(dateString) and datetime.datetime.now().strftime(dateString) <= whenNextOff[currDay].strftime(dateString)):
                   if GPIO.input(20) == GPIO.HIGH:
                        mylcd.lcd_display_string("WARP DRIVE!", 1)
                        mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                        #GPIO.output(24, True)
                        GPIO.output(27, True)
                        time.sleep(3)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string("going off at:", 1)
                        mylcd.lcd_display_string(whenNextOff[currDay].strftime(dateString2), 2)
                        time.sleep(3)
                        mylcd.lcd_clear()

                   if GPIO.input(12) == GPIO.HIGH:
                        #GPIO.output(24, False)
                        GPIO.output(27, False)
                        mylcd.lcd_display_string("OFF: THERMOSTAT", 1)
                        mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                        time.sleep(10)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string(whenNext[currDay].strftime(dateString2), 2)
                        mylcd.lcd_display_string("On since:", 1)
                        time.sleep(10)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 1)
                        time.sleep(3)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string(whenNextOff[currDay].strftime(dateString2), 2)
                        mylcd.lcd_display_string("Next off time:", 1)
                        time.sleep(10)
                        mylcd.lcd_clear()

                   if GPIO.input(16) == GPIO.HIGH:
                        mylcd.lcd_display_string("ECO MODE", 1)
                        mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                        #GPIO.output(24, True)
                        GPIO.output(27, True)
                        time.sleep(240)
                        mylcd.lcd_display_string(whenNextOff[currDay].strftime(dateString2), 2)
                        mylcd.lcd_display_string("Next off time", 1)
                        GPIO.output(24, False)
                        GPIO.output(27, False)
                        time.sleep(120)
                        mylcd.lcd_clear()
#switch off 
                   if (whenNextOff[currDay].strftime(dateString) <= datetime.datetime.now().strftime(dateString)):
                        #GPIO.output(24, False)
                        GPIO.output(27, False)
                        mylcd.lcd_display_string("FINITO!", 1)
                        time.sleep(10)
                        mylcd.lcd_clear()
                   #else :
                    #    while GPIO.input(25) == 1:
                     #     mylcd.lcd_display_string("BANK MGR :)!", 1)
                      #    mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                          #GPIO.output(24, False)
                       #   GPIO.output(27, False)
                        #  time.sleep(10)
                         # mylcd.lcd_clear()
