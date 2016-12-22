# PiHeat
Slave Pi and Controller Pi (S-Pi & C-Pi)

1. Install Flask on C-Pi (http://mattrichardson.com/Raspberry-Pi-Flask/)

Description: S-Pi sends stuff to Flask server running on C-Pi this is done using temp2.py.

S-Pi runs: breathe.py and temp2.py. Cron runs temp2.py every minute to send state values via JSON to C-Pi

C-Pi runs: I2C_LCD_driver.py, PiHeat.py, blynk (at start using rc.local), todo-api/relaydefinitions.py, todo-api/webrelay.py (flask server)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Use of GPIO Pins:

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn off heating

GPIO.setup(27, GPIO.OUT) # Appliance 5/25 volt relay

GPIO.setup(24, GPIO.OUT) # LED

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn on heating

GPIO.setup(12, GPIO.IN) #low heat condition HEATING IS OFF DUE TO THERMOSTAT 

GPIO.setup(16, GPIO.IN) #medium ECO_MODE

GPIO.setup(20, GPIO.IN) #high BLAST HEAT

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

FOR I2C DISPLAY

i2cdetect -y 1

note address and change bus to 1, line 19 of i2c driver program

Start S-Pi before C-Pi

SSH to C-Pi

$ ps ax 

should have these entries:

  664 ?        S      0:00 sudo python /home/pi/PiHeat.py
  
  665 ?        S      0:00 sudo python /home/pi/todo-api/webrelay.py
  
  666 ?        Sl     0:00 node /usr/bin/blynk.js dfafasdfdfsavsvddfsfqWR3987797
  
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  Breathe LED on S-Pi
  
  install WiringPi-Python: https://github.com/WiringPi/WiringPi-Python :: follow instructions for manual build
  
  auto start breathe.py using rc.local
  
  useful article: http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
  
  
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  test that temperatures are being sent: curl -i http://localhost:80/WebRelay/api/relays
  
  set a state: curl -i -H "Content-Type: application/json" -X PUT -d '{"state":"off"}' http://localhost:80/WebRelay/api/relays/1
