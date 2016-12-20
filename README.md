# PiHeat
This project uses 2 x Pi: Slave Pi and Controller Pi (S-Pi & C-Pi)

1. Install Flask on Controller Pi

Description: S-Pi sends room temp states to Flask server running on C-Pi

Use of GPIO Pins:

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn off heating
GPIO.setup(27, GPIO.OUT) # Appliance 5/25 volt relay
GPIO.setup(24, GPIO.OUT) # LED
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn on heating
GPIO.setup(12, GPIO.IN) #low heat condition HEATING IS OFF DUE TO THERMOSTAT 
GPIO.setup(16, GPIO.IN) #medium ECO_MODE
GPIO.setup(20, GPIO.IN) #high BLAST HEAT
