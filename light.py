import tsl2591
from ubidots import ApiClient
import time

api = ApiClient("ubidotapiclient goes here 3973029092138321098098")

#while True:
tsl = tsl2591.Tsl2591()  # initialize
full, ir = tsl.get_full_luminosity()  # read raw values (full spectrum and ir spectrum)
lux = tsl.calculate_lux(full, ir)  # convert raw values to lux
#       print lux, full, ir


api.save_collection([
            {'variable': 'ubidot variable here 9832987397', 'value': lux},
            ])

api.save_collection([
            {'variable': 'ubidot variable here 873264872364', 'value': full},
            ])

api.save_collection([
            {'variable': 'ubidot variable here 1235475123', 'value': ir},
            ])
#time.sleep(57)
exit()

