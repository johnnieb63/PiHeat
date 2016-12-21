import wiringpi
import time
io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)
io.pinMode(1,io.PWM_OUTPUT)
io.pwmWrite(1,0)
value = 0
increment = 4
increasing = True
count = 0

while count < 1000000000000000:
        io.pwmWrite(1,value)

        if increasing:
                value += increment
                time.sleep(0.01)
        else:
                value -= increment
                time.sleep(0.01)

        if (value >=1024):
                increasing = False

        if (value <= 0):
                increasing = True

        time.sleep(0.002)
        count = count + 1
