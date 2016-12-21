# PiHeat
Slave Pi and Controller Pi (S-Pi & C-Pi)

1. Install Flask on C-Pi

Description: S-Pi sends stuff to Flask server running on C-Pi this is done using webrelay.py. webrelay.py is run once a minute using cron.




++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Use of GPIO Pins:

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn off heating

GPIO.setup(27, GPIO.OUT) # Appliance 5/25 volt relay

GPIO.setup(24, GPIO.OUT) # LED

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn on heating

GPIO.setup(12, GPIO.IN) #low heat condition HEATING IS OFF DUE TO THERMOSTAT 

GPIO.setup(16, GPIO.IN) #medium ECO_MODE

GPIO.setup(20, GPIO.IN) #high BLAST HEAT


FOR I2C DISPLAY

i2cdetect -y 1

note address and change bus to 1, line 19 of i2c driver program
