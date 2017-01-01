# run this on c-Pi in /todo-api. Use a cronjob to execute every minute. req.py chats to the Photon.
# currently IFTTT is used to provide 60mins of constant heat input signals to the Photon via DO Buttons: one for ON, the other to CANCEL

from urllib2 import Request, urlopen, URLError #import libraries
import json #import json library
import time
import requests
import urllib
from flask import Flask, jsonify, abort, request, render_template
from relaydefinitions import relays, relayIdToPin



#while True:
#   time.sleep(60)      
try:
            url = "https://api.particle.io/v1/devices/device_number/hot?access_token=access_token_blah_blah_blah"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
#           print (parsed_json['result'])
            time.sleep(2)

            if (parsed_json['result']) == 0:
                r = requests.put('http://youripaddress:80/WebRelay/api/relays/4', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}
#               print r.content
#               print "zero if"

            if (parsed_json['result']) == 1:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/4', verify=False, json={"state": "on"})
                headers = {'Content-type': 'application/json'}

except URLError, e:
            print "something happened"


