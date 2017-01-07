# PiHeat

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

THE HARDWARE ARCHITECTURE:

1. Controller Pi (c-Pi): runs the timer application PiHeat and Flask

2. Slave Pi (s-Pi): gets room temperature, runs temp2 and sends data to Ubidots

3. Optional: Particle Photo & Arduino Uno


Slave Pi and Controller Pi (S-Pi & C-Pi)

1. Install Flask on C-Pi (http://mattrichardson.com/Raspberry-Pi-Flask/)

Description: S-Pi sends stuff to Flask server running on C-Pi by means of temp2.py.

S-Pi runs: temp2.py. Cron runs temp2.py every minute to send state values via JSON to C-Pi. State values correspond to room temperature.

C-Pi runs: I2C_LCD_driver.py, PiHeat.py, blynk (at start using rc.local), todo-api/relaydefinitions.py, todo-api/webrelay.py (flask server)

PiHeat.py is a monolothic app. It needs breaking-up and refactoring.

Start S-Pi before C-Pi

SSH to C-Pi

```
ps ax
```

should have these entries:

  664 ?        S      0:00 sudo python /home/pi/PiHeat.py
  
  665 ?        S      0:00 sudo python /home/pi/todo-api/webrelay.py
  
  666 ?        Sl     0:00 node /usr/bin/blynk.js dfafasdfdfsavsvddfsfqWR3987797

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

For C-Pi use these GPIO Pins:

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn off heating

GPIO.setup(27, GPIO.OUT) # Appliance 5/25 volt relay

GPIO.setup(24, GPIO.OUT) # LED

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Blynk turn on heating

GPIO.setup(23, GPIO.IN) # IFTTT 60mins of constant heat

GPIO.setup(12, GPIO.IN) #low heat condition HEATING IS OFF DUE TO THERMOSTAT 

GPIO.setup(16, GPIO.IN) #medium ECO_MODE

GPIO.setup(20, GPIO.IN) #high BLAST HEAT

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

FOR I2C DISPLAY

i2cdetect -y 1

note address and change bus to 1, line 19 of i2c driver program

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  DO NOT USE: Breathe LED on S-Pi
  
  Code for breathe.py came from: https://lifebydesignuk.wordpress.com/2013/02/20/how-to-breathing-led-in-python-for-raspberrypi/
  
  install WiringPi-Python: https://github.com/WiringPi/WiringPi-Python :: follow instructions for manual build
  
  auto start breathe.py using rc.local
  
  useful article: http://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
  
  
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  test that temperatures are being sent: curl -i http://localhost:80/WebRelay/api/relays
  
  ```
  curl -i http://192.168.0.112:80/WebRelay/api/relays
  ```
  
  set a state: curl -i -H "Content-Type: application/json" -X PUT -d '{"state":"off"}' http://localhost:80/WebRelay/api/relays/1
  
  ```
  curl -i -H "Content-Type: application/json" -X PUT -d '{"state":"off"}' http://localhost:80/WebRelay/api/relays/1
  ```
  
  To check "hot" variable on Photon
  ```
  particle get your_machine_id_here 3 hot
  ```
  
  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
  
  s-Pi and c-Pi need static IP's
  
  sudo nano /etc/dhcpcd.conf
  
  add this to the bottom of that file and reboot. ifconfig to check
  
  ==================================dhcpcd.conf==================================
  
  interface wlan0
  
  static ip_address=192.168.0.200/24
  
  static routers=192.168.0.1
  
  static domain_name_servers=192.168.0.1
  
  ==================================dhcpcd.conf==================================
  
  Install Blynk
  
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential
sudo npm install -g npm
sudo npm install -g onoff
sudo npm install -g blynk-library
```

  Put  node full_path_to_your_script.js <Auth Token> into /etc/rc.local
  


  NOTE: 

  sudo chmod +x temp2.py and other programs that are being autorun

  S-Pi crontab -e: 

  */1 * * * * sudo python /home/pi/temp2.py

  0 */4 * * * sudo reboot

  C-Pi crontab -e:

  0 */6 * * * sudo reboot

  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Installing s-Pi

relaydefinitions must be referenceable by any program setting relay states i.e.: sample folder
  
  MPL3115A2 notes

  INSTALLING I2C FOR PI

  Getting started you'll have to install the I2C packages for Raspberry Pi, and enable them.
  From a Raspberry Pi terminal use the following commands:
  sudo apt-get install python-smbus
  sudo apt-get install i2c-tools

  Enable the modules by adding them to /etc/modules
  sudo nano /etc/modules
  and add the following two lines:
  i2c-bcm2708
  i2c-dev

  Remove the modules from the blacklist by commenting them out "add # to the front"
  sudo nano /etc/modprobe.d/raspi-blacklist.conf
  Make sure the spi and i2c lines are commented out: 

    "#blacklist spi-bcm2708"
    "#blacklist i2c-bcm2708"

  Lastly, the MPL3115A2 requires a proper repeated start command in it's I2C communication. Raspberry Pi doesn't do this out of the box, but there is a kernel module that can be enabled to make it perform repeated start correctly. Run the following commands to enable repeated start on the Pi:

```
sudo su -
echo -n 1 > /sys/module/i2c_bcm2708/parameters/combined
exit
```

  install pip and smbus

```
sudo apt-get install python-pip
sudo apt-get install i2c-tools
sudo adduser pi i2c
sudo reboot
```
```
sudo i2cdetect -y 1
```
```
sudo apt-get install python-smbus 
```
```
sudo pip install ubidots
```
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


Disable bluetooth on RPi3 on c-Pi

Add dtoverlay=pi3-disable-bt to /boot/config.txt. You need to be on the latest OSMC version for this to work. Then run 
```
sudo systemctl disable brcm43xx.service
```
