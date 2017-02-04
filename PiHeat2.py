

# Start the loop that will run until you stop the program or turn off your Raspberry Pi.

while True:


        while (GPIO.input(17) == 1):
                   GPIO.output(24, True)
                   GPIO.output(27, True)
                   mylcd.lcd_display_string("HEAT VIA MOBILE", 1)
                   mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                   time.sleep(2)
                   mylcd.lcd_clear()

        while (GPIO.input(23) == 1):
                   GPIO.output(24, True)
                   GPIO.output(27, True)
                   mylcd.lcd_display_string("1 hour of heat", 1)
                   mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                   time.sleep(2)
                   mylcd.lcd_clear()

        GPIO.output(24, False)
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
                        GPIO.output(24, True)
                        GPIO.output(27, True)
                        time.sleep(3)
                        mylcd.lcd_clear()
                        mylcd.lcd_display_string("going off at:", 1)
                        mylcd.lcd_display_string(whenNextOff[currDay].strftime(dateString2), 2)
                        time.sleep(3)
                        mylcd.lcd_clear()

                   if GPIO.input(12) == GPIO.HIGH:
                        GPIO.output(24, False)
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
                        GPIO.output(24, True)
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
                        GPIO.output(24, False)
                        GPIO.output(27, False)
                        mylcd.lcd_display_string("FINITO!", 1)
                        time.sleep(10)
                        mylcd.lcd_clear()
                   else :
                        while GPIO.input(25) == 1:
                          mylcd.lcd_display_string("BANK MGR :)!", 1)
                          mylcd.lcd_display_string(datetime.datetime.now().strftime(dateString2), 2)
                          GPIO.output(24, False)
                          GPIO.output(27, False)
                          time.sleep(10)
                          mylcd.lcd_clear()

