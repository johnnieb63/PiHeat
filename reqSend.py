import json
import urllib
import time
#def func1():
 #   global myGlobal

while True:
        try:
            url = "https://api.particle.io/v1/devices/250024000d47353136383631/analogvalue1?access_token=3940ba74413bfd2e163ac768c551376b032f3d24"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
            myGlobal = ((parsed_json['result'])/16)
            print "LM35 int. deg C:", myGlobal
            print " "
#           print " "
            time.sleep(2)

            url = "https://api.particle.io/v1/devices/250024000d47353136383631/analogvalue2?access_token=3940ba74413bfd2e163ac768c551376b032f3d24"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
            myGlobal = ((parsed_json['result'])/16)
            print "LM35 ext. deg C:", myGlobal
            print " "
 #          print " " 
            time.sleep(2)

            url = "https://api.particle.io/v1/devices/250024000d47353136383631/analogvalue3?access_token=3940ba74413bfd2e163ac768c551376b032f3d24"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
            myGlobal = (parsed_json['result'])
            print "DHT-11 int. deg C:", myGlobal
            print " "
#           print " " 
            time.sleep(2)

            url = "https://api.particle.io/v1/devices/250024000d47353136383631/analogvalue4?access_token=3940ba74413bfd2e163ac768c551376b032f3d24"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
            myGlobal = (parsed_json['result'])
            print "DHT-11 int. humid %:", myGlobal
            print " "
#           print " " 
            time.sleep(20)

        except URLError, e:
            print "something happened"

