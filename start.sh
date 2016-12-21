
#!/bin/bash

cd home/pi/
#PiHeat must start before Flask (webrelay)
sudo python /home/pi/PiHeat.py &

sudo python /home/pi/todo-api/webrelay.py &
